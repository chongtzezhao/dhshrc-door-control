# dhshrc-door-control
This repo contains the code which activates a servo whenever a message is received from the telegram bot, or when it receives commands through a bluetooth socket.

v1.0

Features:
- This repo contains two modes of communication. THe first is through sending messages to a telegram bot, the other is a sending commands through a bluetooth socket.
- Simple and easy to use
- Auto day and time check: Will only activate on weekdays, between 7am and 6.45 pm
- 

Hardware requirements:
- Raspberry pi 3
- microsd card >= 8 gb storage
- Female to male jumper wires
- a servo


How to install:

- These python programs relies on several packages. telepot, pigpio and pybluez
- To set up, navigate to the terminal and enter "sudo python3 -m pip install <package>" for each of the packages
- Download and extract the folder named "door" and place it in your desktop
- Open "startup.txt"
- Open terminal and enter "sudo crontab -e"
- Scroll down to the bottom of the window and copy over the contents from startup.txt
 
