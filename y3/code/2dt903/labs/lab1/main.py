from machine import Pin, ADC
import utime

# Set up the potentiometer on ADC pin (GP26)
potentiometer = ADC(Pin(26))  # GP26 corresponds to ADC0

# Define the voltage reference
VREF = 3.3  # The Pico's ADC reference voltage

def read_potentiometer():
    # Read the ADC value (0 to 4095)
    adc_value = potentiometer.read_u16()  # Returns a 16-bit value (0 to 65535)
    adc_value_12bit = adc_value >> 4      # Convert it to 12-bit resolution (0 to 4095)
    
    # Convert ADC value to voltage
    voltage = (adc_value_12bit / 4095) * VREF
    
    return adc_value_12bit, voltage

while True:   
    # Read the potentiometer values
    adc_value, voltage = read_potentiometer()
    
    # Display the ADC and Voltage
    print("ADC Value: {}".format(adc_value))
    print("Voltage: {:.2f} V".format(voltage))
   
    # Delay for stability
    utime.sleep(0.5)
