# timer.ru
#
# Author: Samuel Berg
# Date: 10-Sep-2019

def timer
    start_time = Time.now
    yield
    puts "Elapsed time: #{Time.now - start_time}s"
end

timer() do
    puts "I am doing something slow..."
    sleep(5)
    puts "I am done :)"
end
