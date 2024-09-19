# 2DT903 - Lab 1

## Task 1

In order to determine whether we can reconstruct the original signal after discretization, we need to apply the **Nyquist-Shannon sampling theorem**. This theorem states that for a signal to be perfectly reconstructed from its samples, the sampling rate must be at least **twice** the maximum frequency present in the signal. In other words, if *fmax* is the maximum frequency in the signal, the sampling rate *fs* must satisfy the condition:

*fs >= 2 x fmax*

### Given Information:
- The signal *x(t)* consists of sine waves with frequencies: 1.75 kHz, 2 kHz, and 3 kHz.
- The sampling rate *fs = 5* kHz.

### Maximum Frequency in the Signal:
The highest frequency component in the signal is 3 kHz.

### Nyquist Criterion:
According to the Nyquist-Shannon theorem, the minimum sampling rate required to reconstruct the signal is:

*fs >= 2 x fmax = 2 x 3 kHz = 6 kHz*

However, the given sampling rate is 5 kHz, which is **less than** the required 6 kHz. This means that the sampling rate does **not satisfy** the Nyquist criterion.

### Conclusion:
Since the sampling rate of *5* kHz is less than the required *6* kHz, we will not be able to perfectly reconstruct the original signal. **Aliasing** will occur, which means that higher frequency components (like the *3* kHz component) will be "folded" into lower frequencies, distorting the signal after discretization.

## Task 2

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


