# PosKivy
It is Point Of Sales made by Python and Kivy Technology


### Instalation
- github clone https://github.com/richierh/KivyPos#poskivy
- source ./venv/bin/activate 
- pip install -r requirements.txt
- pip install -r requirements2.txt
- search file main.py in the top level directory
- run python main.py

### Requirements
- Python3 > 3.6
- Kivy > 2.1.0
- KivyMD > 1.0.1

### Build for Android
> buildozer android debug deploy run logcat

## Developer
### HotReload Support
This app has hotreload support , so don't you missed the benefit of it. Hotreload gives you easiness to edit your code especially on UI side / (kv/py) files with live demo. 
How to use it? Run your program / app by just type in the terminal or any IDE you like the command below: 
> DEBUG=1 python hotreload.py
### Developing Technique
This applications use kivymd module/package which is built in already inside kivymd to create project and add view/screen. see this documentations [https://kivymd.readthedocs.io/en/1.1.1/api/kivymd/tools/patterns/create_project/index.html]

to add view for new screen you can use this command in root directory:

> python -m kivymd.tools.patterns.add_view MVC '.' NameScreen

Please remember to always use the word 'Screen' in the last word of the screen name (NameScreen).
For more details ,you can check here 

[https://kivymd.readthedocs.io/en/1.1.1/api/kivymd/tools/patterns/add_view/]


# Need Support
### Help us to contribute by becoming one of what we have provide below :
#### 1. Contributor for Developer
Of course, we always need developers to boosting the development of this application. Take this chance to improving yourself as a profesional

#### 2. Backer / Donations
I would love to have a cup of coffee from you guys :-) . Save this project for the development continuity
<br><img src="/assets/images/BSI.png" width='250'></br>
BSI (Bank Syariah Indonesia) 
Account Bank No 1041478396
Richie Rahmat Hidayat

====================================================================================

<br>Or use Paypal :</br>
<br>[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/gluonITDevelopment?country.x=ID&locale.x=en_US) </br>
<br>GluonIT Software Development</br>

