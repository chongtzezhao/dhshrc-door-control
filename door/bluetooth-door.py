import bluetooth
import pigpio #calling for header file which helps in using GPIOs of PI
from datetime import datetime as dt
from time import sleep
sleep(15)
# CONSTANTS

PIN = 2
PW_MIN = 550
PW_MAX = 2250

disengaged = 1500
engaged = PW_MAX

# FUNCTIONS

def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

def newDatetime():
    return str(dt.now())[:-7]

print(getMAC())

# START CONNECTION

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = bluetooth.PORT_ANY
server_socket.bind(("",port))
server_socket.listen(1)

while 1:
    client_socket,address = server_socket.accept()
    while 1: # inner loop to listen for commands
        data = client_socket.recv(1024).decode()
        
        try:
            with open("door_blue_log.txt", "a") as file:
                file.write(newDatetime() + ',' + data)
                file.write("\n")
        except:
            with open("door_blue_log.txt", "w") as file:
                file.write(newDatetime() + ',' + data)
                file.write("\n")
        data = data.capitalize() # ignores any upper or lowercase
        
        if (data == "Q"):
            client_socket.send('Disconnected.')
            print('Disconnected.')
            break
        
        if dt.today().weekday()>4 or dt.now().hour<7 or dt.now().hour+(dt.now().minute/60)>=6.75+12:
            client_socket.send("Room is out of bounds. Door not unlocked")
            print("Room is out of bounds. Door not unlocked")
            continue
            
        
        if (data == "Open"):
            io = pigpio.pi()
            io.set_servo_pulsewidth(PIN, engaged)
            sleep(0.4)
            io.set_servo_pulsewidth(PIN, disengaged)
            sleep(1)
            io.set_PWM_dutycycle(PIN, 0)
            client_socket.send("Door successfully unlocked")
            print("Door successfully unlocked")
        else:
            client_socket.send('Invalid command.\nSend "open" to unlock door\nSend "q" to disconnect')
            print('Invalid command.\nSend "open" to unlock door\nSend "q" to disconnect')
    
    client_socket.close()
    
