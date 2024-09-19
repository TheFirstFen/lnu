from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import utime

# Set up I2C communication for the OLED
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)  # Adjust GP pins based on your connection
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

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
    # Clear the OLED display
    oled.fill(0)
    
    # Read the potentiometer values
    adc_value, voltage = read_potentiometer()
    
    # Display the ADC and Voltage values on the OLED
    oled.text("ADC Value: {}".format(adc_value), 0, 0)
    oled.text("Voltage: {:.2f} V".format(voltage), 0, 16)
    
    # Update the OLED display
    oled.show()
    
    # Delay for stability
    utime.sleep(0.5)

