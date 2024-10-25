# Sivans line tracker
## Abstract
When going to the club, in many cases there is a long line. These lines are very inconvenient, especially during rough weather. For most clubs, there is no efficient solution solving this problem. Due to this reason, this project aims to solve this problem. Our solution for this is to measure the line and then displaying the results on a website. To do this, we use ultrasonic-sensors to accurately measure distance, then analysing this data and converting it to approximately how many lines are filled. After conversion, the data gets sent to a webserver, which displays it on a website. The website shows how full the line currently is, aswell as historic data of when it is usually full. 


## Background and idea
The concept is to develop a website that provides information about the number of people standing in line at Sivans. It will aid the public in getting an estimate of how many people are currently waiting in line and it will allow them to access the historical data which shows the number of people who waited in line during specific hours. 

The idea behind this project is to assist students in particular who are interested in knowing how long the line is at Sivans. This will enable them to plan when they should start lining up and when they should avoid it.



## Method (links to all project documentation)
### Web design
When the website was first set to be created, there were discussions about what should be displayed and how. Once the content was established, an index, or home page, was created in HTML, which contained all the headers, texts, and buttons that had been decided upon. Subsequently, a history "subpage" was created to present the queue history of previous weeks. To link from the home page to the history page, the two were connected in the HTML index. To facilitate the design work in CSS, different IDs were assigned to various functions.

At the initiation of the CSS development process, a dedicated CSS file was generated and subsequently linked to two HTML files, allowing both pages to have a consistent design. Before starting the website's design, the group discussed the theme it should have. Afterwards, various backgrounds and fonts were tested to find something the group agreed on and which they felt suited the website. Then, a glowing effect was added to all headers and subheaders, along with a border for the text displayed below. Finally, the buttons were designed to behave like buttons when the mouse hovers over them or when clicked.

### Server 
- #### Database
    The database infrastructure was established through the use of SQL, coupled with the sqlite3 library in Python. This combination provided a structured and efficient framework for data management and extensive documentation from the framework. Within this database, a specific table, denoted as 'sivans,' was created to systematically store essential information, including timestamps and distance measurements. This approach ensures a organized database and also enables both retrieval and storage of data.

- #### Nginx, Flask and Linux
    We set up the server using Linux Ubuntu with Nginx as a starting point. To handle the website, we used a combo of Flask and Nginx. Nginx is like the go-between that talks to the outside world, while Flask is the behind-the-scenes worker that deals with user data and sends it back and forth.

    Flask, which is based on Python, is the brain. It deals with all the requests and responses, making sure the sub-routes have the real-time and past queue lengths ready for the user to read it.

    Nginx acts like a middleman between the internet and the backend server,  it makes sure external requests get to Flask without any errors.


### Hardware configuration
The goal for this project was to be able to measure the line at Sivans. In the beginning, the idea was to measure this by taking photographs with a camera and then processing them with a color mask to identify where people were.

![sivans kö med kamera](.\img\sivans-kamera.png)

The connected raspberry pico would then send this data to our web server using the LoRa network. This would need a LoRa-unit, but seemed like a simple solution at the time.

However, after talking to Sivans, it was clear a camera was not allowed to be used. Therefore we replanned the hardware to use an ultrasonic-sensor instead. This sensor sends pulses of ultrasound and can then detect when it comes back. 

![sivans kö med ultraljudsensor](.\img\sivans-sensor.png)

Using some code, this can easily output a distance instead.
```python
import utime
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(10)
   trigger.low()
   utime.sleep_us(100)
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print(distance)
   return distance

while True:
    ultra()
    utime.sleep(1)
```

(code from https://www.tomshardware.com/how-to/raspberry-pi-pico-ultrasonic-sensor)

It was later noticed that this sensor could only measure up to 5,6 meters, which meant the sensor itself wasn't enough to measure the entire line. For this reason, we replanned the hardware once again. This time two separate raspberry picos with one ultrasonic-sensor each was used. With this configuration, it was possible to measure the entire line with high quality results.

![sivans line with two sensors](.\img\sivans-sensor2.png)

Another change which was made was to use the schools wifi to send the data instead of LoRa. This made for easy configuration and no unnecessary extra hardware.
```python
ssid = 'myssid'
password = 'mypassword'
url = 'myurl'
data = {'name': value}
datajson = json.dumps(data)
headers = {'Content-Type': 'application/json'}

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    if wlan.isconnected() == True:
        return True
    return False

def send_data(datajson):
    sent = urequests.patch(url, data=datajson, headers=headers)
    print(sent.text)
```
It was now possible to measure distances using the pico and send it to the server. The two picos send data simultaneously in the form of dictionaries. The dictionary contains the name of the pico as well as it's value. This leads to easy separation of values from the two picos. For this to work outside of sivans however, the raspberry pico had to be directly connected to power. For this two powerbanks were bought, one for each of the raspberry picos. With a rasberry pico connected to a powerbank and a file named "main.py" stored on the pico, it will run automatically whenever it is connected to power. This meant a computer was no longer needed to measure the distance. 

One problem which occurred was with making the pico "sleep". In micropython there are different kinds of sleep: sleep, lightsleep and deepsleep. The sleep-function is quite unefficient and still draws a lot of power. The deepsleep turned out to not be supported on the raspberry pico, which lead to lightsleep being the best option. Lightsleep draws less power than sleep and is supported. There is however a problem with lightsleep too. While programming the pico, the code editor Thonny was used. Thonny worked great to program in until using the lightsleep-function, where it turned out that it was not supported. This meant the function had to be tried out while not connected to the computer.


#### Power Draw
The raspberry pico is connected to a powerbank with 5000mAh. The pico is said to draw 50mA and the sensor 2mA. This leads to an expected battery life of 96,15 hours per charge, which is way more than the approximately 5 hours needed. Thus, no further calculations regarding lowering power draw were made.

## Results (show pictures)
### Hardware
The resulting hardware worked as intended. The raspberry pico uses the ultrasonic-sensor to accurately measure distance.

![pico-kopplad](.\img\kopplad-pico.jpg)

After getting the distance it converts this to an integer which describes how many lines in front of the pico was empty. After converting these values it then sends to corresponding data to the web server. 

Once the webserver recieves the data it displays this on the website as intended.

![hemsida](.\img\hemsida.png)

The website also shows the history of the last four weeks. The history is displayed using a graph as shown below.

![hemsida-historik](.\img\hemsida-historik.png)

### User-to-Device Web Link: Illustrated Connectivity Flow
Below is a flow chart showing how everything is connected from the user that is on the webpage to the IOT device.

![flow-chart](.\img\flow_chart.png)

In total, the project went as expected. Almost all of the project requirements were met. There were a couple of downsides however, the first being that the chassis never got built. The chassis wasn't prioritized since it didn't seem relevant compared to completing the software. Also, the project was never tested during an actual night at Sivans. This was because once the software was done, Sivans was closed and opened after the project was due. The sensor was tested at sivans however, to ensure it could be applied there.


## Documentation
- [Requirements](.\doc\requirements.md)
- [Documentation](.\doc\documentation.md)
- [Project plan](.\doc\project_plan.md)
- [Time log](.\doc\timelog.md)
- [Hardware setup](.\doc\hardware.md)
- [Tests](.\doc\tests.md)
- [Setup](.\doc\setup.md)
- [Links](.\doc\links.md)