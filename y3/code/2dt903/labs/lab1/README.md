# 2DT903 - Lab 1

## Task 1

```Task1
Nyquist criterion formula: *fs >= 2 x fmax*

f1 = 1.75 kHz
f2 = 2 kHz
f3 = 3 kHz
=> fmax = 3 kHz
given_fs = 5 kHz

compute needed_fs:

needed_fs >= 2 x fmax = 2 x 3 kHz = 6 kHz

=> given_fs < needed_fs

=> The sampling rate of 5 kHz that we have is not enough to perfectly reconstruct to original signal, this according to the Nyquist criterion.
```

## Task 2

```Task2

```

To convert voltages using a **successive approximation-based 4-bit Analog-to-Digital Converter (ADC)**, the ADC sequentially compares the input voltage to midpoints within its range, adjusting the bits in its binary output until it converges on a close digital representation of the input voltage.

In your case:
- **Vmin = 0.5V** corresponds to "0000".
- **Vmax = 5V** corresponds to "1111".
  
Thus, the step size of the ADC is calculated as:

\[
\text{Step size} = \frac{V_{\text{max}} - V_{\text{min}}}{2^n - 1} = \frac{5V - 0.5V}{15} = 0.3V
\]

This means each increment in the digital output represents 0.3V.

### Key Steps of Successive Approximation:
1. Start by assuming the midpoint of the range (approximately half of Vmax).
2. Compare the input voltage to the current midpoint and set a higher or lower bit depending on the result.
3. Continue adjusting one bit at a time from the MSB (most significant bit) to the LSB (least significant bit).
4. After each comparison, refine the approximation of the voltage by adjusting the output bits.

---

### Conversion for Given Voltages:

Let's now convert voltages of **1.8V, 2.3V, 3V, and 3.8V**:

1. **For 1.8V**:
   - Midpoint of 0.5V–5V: 2.75V → 1.8V is lower, so MSB = 0.
   - Midpoint of 0.5V–2.75V: 1.625V → 1.8V is higher, so 2nd bit = 1.
   - Midpoint of 1.625V–2.75V: 2.1875V → 1.8V is lower, so 3rd bit = 0.
   - Midpoint of 1.625V–2.1875V: 1.90625V → 1.8V is lower, so LSB = 0.
   
   Final digital output: **"0110"** (6 in decimal).

2. **For 2.3V**:
   - Midpoint of 0.5V–5V: 2.75V → 2.3V is lower, so MSB = 0.
   - Midpoint of 0.5V–2.75V: 1.625V → 2.3V is higher, so 2nd bit = 1.
   - Midpoint of 1.625V–2.75V: 2.1875V → 2.3V is higher, so 3rd bit = 1.
   - Midpoint of 2.1875V–2.75V: 2.46875V → 2.3V is lower, so LSB = 0.
   
   Final digital output: **"0111"** (7 in decimal).

3. **For 3.0V**:
   - Midpoint of 0.5V–5V: 2.75V → 3.0V is higher, so MSB = 1.
   - Midpoint of 2.75V–5V: 3.875V → 3.0V is lower, so 2nd bit = 0.
   - Midpoint of 2.75V–3.875V: 3.3125V → 3.0V is lower, so 3rd bit = 0.
   - Midpoint of 2.75V–3.3125V: 3.03125V → 3.0V is lower, so LSB = 0.
   
   Final digital output: **"1000"** (8 in decimal).

4. **For 3.8V**:
   - Midpoint of 0.5V–5V: 2.75V → 3.8V is higher, so MSB = 1.
   - Midpoint of 2.75V–5V: 3.875V → 3.8V is lower, so 2nd bit = 0.
   - Midpoint of 2.75V–3.875V: 3.3125V → 3.8V is higher, so 3rd bit = 1.
   - Midpoint of 3.3125V–3.875V: 3.59375V → 3.8V is higher, so LSB = 1.
   
   Final digital output: **"1011"** (11 in decimal).

---

### Diagram:

Imagine a flow like this, where each comparison (midpoint) adjusts a bit in the binary output.

- For **1.8V**, the steps in each comparison would follow: 2.75V, 1.625V, 2.1875V, and 1.90625V, resulting in the binary number "0110".
- Similarly, for **2.3V**, the comparisons narrow down the binary output to "0111".
- For **3.0V**, the steps converge to "1000", and for **3.8V**, the approximation yields "1011".

Would you like a graphical representation for this?

## Task 3

### First

```text
RP2040 Clock frequency = 48 MHz
ADC conversion time = 96 CPU clock cycles per conversion

fs := Clock frequency/Clock cycles per conversion

=> fs = 48 000 000 Hz / 96 = 500 000 Hz = 500 kHz
```

### Second

```text
N = 12 bits
Vmax = 3.3 V
Vmin = 0 V

ADC resolution = (Vmax - Vmin) / (2^N - 1)

=> resolution = (3.3 - 0) / (2^12 - 1) = 3.3 / 4095 = 0.000805861 V = approx 0.81 mV
```

### Third

```python
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
    
    # Display the ADC and Voltage values on the OLED
    print("ADC Value: {}".format(adc_value))
    print("Voltage: {:.2f} V".format(voltage))
    
    # Delay for stability
    utime.sleep(0.5)
```
