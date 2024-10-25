# 1dt902-Luftkontrolls-projekt
## Air Quality project

## Air Quality 

The project is called "air quality project" and the purpose is to measure the indoor air quality in our University by using a microcontroller and sensors. In this project we wanted study the temperature, humidity level, dust particles, and level of toxic gases such as corbon dioxide. The microcontroller rasberry pi pico W is the control unit which gathers data from our different sensors and provides vital information about the quality of the air. The information gathered can be used to identify whether the airquality is of the highest standard or if we need to take actions to improve it. In summary  the air quality project aims to research and promote a healthier school enviroment for both students and staff at our school. 

## Description
The school enviroment is a huge part of a students life. This is where we learn, meet friends and develop as human beings. Because of its importance we wanted to study the Air Quality. With this we do not mean just different hazzardous particles that emerge from different materials in the indoor enviroment but also temperature and humidity. We all have felt the consequenses dehydration at some point in our life and it is not appropiate to have a indoor enviroment that is either to hot, cold och too moist. Espacially in a enviroment where performance of the individual is important. But we also wanted to discover whether the the different values changed during the day, therefore we decided to measure and send data each hour. How is human interaction in the indoor location impact the measured values and how much. 
The airquality can have big impact of how the student is performing. 


Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.


## Prerequisites 

The choice of microcontroller, fist step is to get familier with the Raspberry pi pico W. Here is a guide to get started. 

https://projects.raspberrypi.org/en/projects/get-started-pico-w


# Hardware

[link to doc/hardware](doc/hardware.md)

- Rasberry pi pico w is as microcontroller, store and sends data to a mqtt server and datacace. 

-  Dust sensor optic GP2Y1010AU0F is wired with the breadboard togather with the Rasberry pi pico W, measures the amount of dust particles in the air. 

- DHT11 Sensor is used to measure temparture and humidity in the location. '

- SEN-14193 - CCS811 is a sensor have the ability to sense a large amount of different toxic gases. 

- Breadboard is a device used for building prototypes for test circuits. It is vital for making circuits and conecting, the sensors to the microcontroller. 


## Software 

- Tools 

### Thonny

In the project we used Thonny as IDE. Thonny is a development envioment which supports MicroPython. Thonny makes it possible to controll our  microcontroller and is vital regarding development purposes. 

### MQTT explorer
We used Mqtt explorer to send att data to a mqtt broker. In the Mqtt exlorer we can view data by graphs of our our different subject. 

### Datacake 

Datacake is a IoT plattform which is used to create a IoT application. Datacake acts like a storage system for our data.


## Computer setup 


1. 
- We are able to connect to wifi through our microcontroller with rasberry pi Pico, make sure that your rasberry py is connected correcly and that it Thonny is installed following code was used to [conncent to wifi](src/main.py). Create and object "SSID" and store the Wi-Fi access as seen in the main file. Also create a object "PASSWORD" and store you Wi-Fi password. It is also important to import the required modules.  

2. When connected succefully to your local Wi-fi. It is time to send the data to a MQTT-broker. In the file [MQTT_syn.py](src/MQTT_asy.py). MQTT is a standard for message queing. It works as a standart messaging protocal. Throgh the mqtt protocal we can publish messages and subrscribe to the subject







[docs/setup](doc/setup.md)

- images of the setup 
[docs/images](img)

in the DHT11 images you can se how the DHT11 -sensor is wired   


## Badges 


In the folder img in skärmbild_20230114_233700 you can see a skreenshot of some measures with the DHT11 sensor. 
[docs/images](img)

On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.


## Installation

To download thonny you may visit the official website https://thonny.org and download the latest version for your system. There are then 3 different packeges that needs to be installed. These are installed by first clicking tools in thonny and then selecting manage packages. Click the search bar and type in micropython_mqtt by the author Thorsten von Eicken. The second one is micropython_mqtt_async by the author Thorsten von Eicken. The third and final package is picozero by the author Raspberry Pi Foundation.


## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
If support is needed for the sensors there are dokumentations describing what the sensor can do but also how to connect the cables. The iot services also have there own dokumentations so if there is problem with datacake visit https://docs.datacake.de/ . 

Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.


## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
