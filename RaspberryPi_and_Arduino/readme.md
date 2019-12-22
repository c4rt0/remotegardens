Since pH probe and pH sensor play important role in my project I decided to present instructions on how I managed to connect both in a separate section.
Firstly I feel I need to clarify something that wasn't obvious to me at the very beginnings of this project: 

ph sensor outputs analog signal, while Raspberry Pi accepts only digital inputs.

This misterious sounding sentence became very clear really rapidly. I found out that instead of using analog-to-digital converter (ADC, A/D, or A-to-D)
I could simply use Arduino which I already had in my arsenal. 

Configuration of Arduino as a slave took a little bit of work - included in this folder is a i2c_slave file which was uploaded directly to Arduino through USB.

In order to check connectivity between Arduino and Pi after uploading i2c_slave we execute "sudo i2cdetect -y 1" command on Raspberry (result visible on the picture attached - bottom of terminal)

![](/images/i2c_detection.jpg)
