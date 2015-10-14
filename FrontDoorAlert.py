
import smtplib
import time
from time import gmtime, strftime, localtime

ID = 'username'
Auth = 'pass'
From = 'something@gmail.com'
to  = '000-000-0000@cingularme.com'  # cingular text message send
   

message = 'Hello, Just Noticed activity near the front door.'
# Fairly straight forward example in 20.12.2. SMTP / smtplib

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.set_debuglevel(1)
server.login(ID,Auth)
server.sendmail(From, to, message)
server.quit()

