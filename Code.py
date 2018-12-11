import time
import serial
import smtplib

TO = 'adityapankaj.shaha2015@vit.ac.in'
GMAIL_USER = 'adityapankaj.shaha2015@vit.ac.in'
GMAIL_PASS = 'xxxxxxxx'

SUBJECT = 'The Garbage is about to get full !'
TEXT = 'The Garbage Space is filled more than 75%. Please dump your Garbage'
  
ser = serial.Serial('COM8', 9600)

def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()
    
while True:
    message = ser.readline()
    print(message)
    if message[19] > "7" :
        send_email()
    time.sleep(0.5)
