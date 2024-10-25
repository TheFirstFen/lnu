# Assignment 1 2DT903

## Emil Ulvagården (eu222dq@student.lnu.se)

### Part 1

```Powershell

Input signals are 1.75, 2, 3 kHz

f (Sample rate) = 5 kHz

f (Nyquist rate) = 2 * 3 kHz = 6 kHz

f (Sample rate) < f (Nyquist rate)

```

Due to the fact that the sample rate is less than the the Nyquist rate. This means that the sample rate of 5 kHz cant reconstruct the outputs of 1.75, 2 and 3 kHz. 

### Part 2

```Powershell

Vmin = 0.5
Vmax = 5
N = log(16)

Stepsize = (Vmax - Vmin) / (2^N - 1) 

Stepsize = (5 - 0.5) / (2⁴ - 1)  = 4.5 / 15

Step size = 0.3

```

```Powershell

(0000) = 0.5
(0001) = 0.8
(0010) = 1.1
(0011) = 1.4
(0100) = 1.7
(0101) = 2.0
(0110) = 2.3
(0111) = 2.6
(1000) = 2.9
(1001) = 3.2
(1010) = 3.5
(1011) = 3.8
(1100) = 4.1
(1101) = 4.4
(1110) = 4.7
(1111) = 5.0

```

#### 1.8 V

```Powershell

(1000) = 2.9
1.8 < 2.9 --> MSB = 0

(0100) = 1.7
1.8 > 1.7 --> MSB = 1

(0110) = 2.3
1.8 < 2.3 -->B = 0

(0101) = 2.0
1.8 < 2.0 -- MSB = 0

1.8 = (0100)

```

![1.8 V](.\Pic\1_8.jpg)

#### 2.3 V

```Powershell

(1000) = 2.9
2.3 < 2.9 --> MSB = 0

(0100)
2.3 > 1.7 --> MSB = 1

(0110) = 2.3
2.3 >= 2.3 --> MSB = 1

(0111) = 2.6
2.3 < 2.6 --> MSB = 0

2.3 = (0110)

```

![2.3 V](.\Pic\2_3.jpg)

#### 3.0 V

```Powershell

(1000) = 2.9
3.0 > 2.9 --> MSB = 1

(1100) = 4.1
3.0 < 4.1 --> MSB = 0

(1010) = 3.5
3.0 < 3.5 --> MSB = 0

(1001) = 3.2
3.0 < 3.2 --> MSB = 0

3.0 = (1000)

```

![3.0 V](.\Pic\3_0.jpg)

#### 3.8 V

```Powershell

(1000) = 2.9
3.8 > 2.9 --> MSB = 1

(1100) = 4.1
3.8 < 4.1 --> MSB = 0

(1010) = 3.5
3.8 > 3.3125 --> MSB = 1

(1011) = 3.8
3.8 >= 3.8 --> MSB = 1

3.8 = (1011) 

```

![3.8 V](.\Pic\3_8.jpg)

### Part 3

#### First

```Powershell

f = CPU Clock Frequency / ADC Conversion Cycle

f = frequency

CPU Clock Frequency = 48 *10⁶

ADC Conversion Cycle = 96

f = 48 * 10⁶ / 96 = 5 * 10⁵

f = 500 KHz
```

#### Second

```Powershell

Resolution = (Vmax - Vmin) / (2^n -1)

n = 12

Vmax = 3.3 

Vmin = 0

Resolution = 3.3 / (2¹² - 1)

Resolution = 3.3 / 4095

Resolution = 0.00080586= 0.80586 mV 

```

#### Third

```Powershell

from machine import Pin, ADC
import time

Potentiometer = ADC(Pin(26))

VREF = 3.3

while True:
    adc_value = Potentiometer.read_u16()
    
    adc_value_12bit = adc_value >> 4
    
    voltage = (adc_value_12bit / 4095) * VREF
    
    print("ADC Value: ", adc_value_12bit, "\tVoltage: ", voltage)
    
    time.sleep(1)

```

### Pictures

![Raspberry Pi pico breadbord connection](.\Pic\Raspberry_pi_board.jpg)

![Output](.\Pic\Output.jpg)
