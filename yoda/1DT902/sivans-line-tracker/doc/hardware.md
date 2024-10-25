# Hardware
## Components
* Raspberry Pico Wifi
* Breadboard
* Ultrasonic-sensor 400cm
* 4 male -> male gpio cables
* Powerbank
* USB-A -> USB-C cable

## Connecting the components
* Press down the Rasberry Pico on the breadboard
![pico on breadboard](..\img\breadbord.jpg)
The rest of the steps are based on the pico being oriented as shown above.

* Press down the ultrasonic-sensor on the breadboard as shown below.
![sensor-på-breadboard](..\img\sensor-på.jpg)

(as far down as possible whether your sensor has 4 or 5 pins)

Raspberry pico wifi pins: 
![raspberry pico pins](..\img\pico-pins.png)

With your four gpio-cables connect the following:
* GND -> Any ground pin
* TRIG -> GP2
* Echo -> GP3
* VCC -> 3V3(OUT)

![Connected raspberry pico](..\img\kopplad-pico.jpg)

* Connect the raspberry pico to your powerbank using the USB-A -> USB-C cable.

![Pico connected to powerbank](..\img\pico-med-powerbank.jpg)

Done!