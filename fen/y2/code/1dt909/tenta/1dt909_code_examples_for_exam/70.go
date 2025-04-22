package main

type CountingSemaphore struct {
	mutex BinarySemaphore // För ömsesidig uteslutning kring räknaren
	delay BinarySemaphore // För att blockera trådar
	count int             // Antal tillgängliga "slots"
}

func NewCountingSemaphore(initialCount int) *CountingSemaphore {
	s := &CountingSemaphore{
		count: initialCount,
	}
	s.mutex.Signal() // Initiera mutex till olåst
	if initialCount > 0 {
		s.delay.Signal() // Initiera delay till olåst om vi har slots
	}
	return s
}

// P-operation (wait/acquire/down)
func (s *CountingSemaphore) Wait() {
	s.delay.Wait() // Vänta om count <= 0
	s.mutex.Wait() // Ta mutexen för att ändra count
	s.count--      // Minska count
	if s.count > 0 {
		s.delay.Signal() // Om fler slots finns, låt nästa tråd gå in
	}
	s.mutex.Signal() // Släpp mutexen
}

// V-operation (signal/release/up)
func (s *CountingSemaphore) Signal() {
	s.mutex.Wait()    // Ta mutexen för att ändra count
	s.count++         // Öka count
	if s.count == 1 { // Om detta är första lediga slot
		s.delay.Signal() // Låt en väntande tråd gå in
	}
	s.mutex.Signal() // Släpp mutexen
}
