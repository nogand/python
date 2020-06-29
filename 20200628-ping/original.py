import subprocess as sp

ip = "192.168.30.1"
status,result = sp.getstatusoutput("ping -c1 -w2 " + ip)

if status == 0:
    print("System " + ip + " is UP !")
else:
    print("System " + ip + " is DOWN !")
