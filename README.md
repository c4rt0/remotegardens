# remotegardens.com
Remote garden solution based on micro-controllers (remotegardens.com) 

Many years ago I came up with an idea of completely automatic grow system for various types of plants. Inspired by "The Martian" played by Matt Damon I thought of creating sort of independent plant environment controlled by machines. These days traditional agriculture accounts for, on average, 70 percent of all water withdrawals globally... hydroponics and aeroponics can be organic and solves this problem! Hydroponic gardens can be located at any location, without requirements for large land plots. Appropriately adapted small living (or storage) space can benefit in fresh product on regular basis. If so we can teach our machines to recognise best environment in order to acheive best quality product (i.e based on weight) - we will quickly eliminate the need of standard energy and resources waste. There's a long way ahead of us - let's start here.

In first stage of my aproach I need to implement simple system, which controlls irrigation conditions, but also takes under account certain environment factors (temperature & humidity). Values of most important parameters should be stored online for future investigation and record analysis. Furthermore, certain remote control should be avail in order to influence critical circumstances.

In the future my aim is to implement photoresistors or other light sensing devices to monitor intensity and conditions of photosynthesis, also gas sensors and other sensing mechanisms to fully understand and record growing conditions. Moreover, software will allow user to differentiate between different plant species, with hardcoded initial values for NPK, temperature, humidity, pH and other ratios. Over time this idea will evolve, and new features will be implemented... Now, let's start saving our PLANET.


![](/images/REMOTE_GARDENS.com.jpeg)

Using "Fritzing" app I started playing around with schematics. First result of designing connections with my DHT11 sensor is seen below. I noticed here, that PIN's between DHT11 sensors vary (pins of my model of DHT11 from left : GND/DAT/VCC)

![](/images/Connecting_DHT11_bb.jpg)

Full schematics :

![](/Fritizing/REMOTE_GARDENS_bb.png)
