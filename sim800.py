#sim800l class for call , send sms , receive sms send AT command 
from machine import UART 
from time import sleep, sleep_ms 

class SIM800():
    def __init__(self, TX_PIN, RX_PIN, baudrate=9600):
        self.uart = UART(1, baudrate, tx=TX_PIN, rx=RX_PIN)
#for send AT command use this method     
    def send_at_command(self,command):
        self.uart.write(command + "\r\n")
        utime.sleep(1)
        return self.uart.readline()
#-----------------------------------
#for send sms use this method    
    def send_sms(self,phone_number, message ):
        send_at_command('AT+CMGF=1')  
        send_at_command('AT+CMGS="' + phone_number + '"')
        send_at_command(message)
        send_at_command(chr(26))  
#---------------------------------
#for receive sms use this method   
    def read_sms(self):
        self.send_at('AT+CMGL="REC UNREAD"')
#--------------------------------
#for call use this method 
    def call(self,phone_number):
        self.send_at_command('ATD' + phone_number + ';')     
