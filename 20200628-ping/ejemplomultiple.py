import subprocess as sp

ips = [ "192.168.30.1", "192.168.30.114", "192.168.30.44" ]
results = {}

for ip in ips:
  status,result = sp.getstatusoutput("ping -c1 -w2 " + ip)
  results[ip]=status

for system in results.keys():
  if results[system] == 0:
    print("System " + system + " is UP !")
  else :
    print("System " + system + " is DOWN !")
