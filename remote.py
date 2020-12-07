import os 
import subprocess
os.system("sudo clear")
os.system("tput setaf 3")
print("Remote")
os.system("tput setaf 7")


while True:
	os.system("tput setaf 4")
	print("""
1.Check Ansible connectivity 
2.Configure Web server
3.Httpd authentication
4.Add user
5.Yum configration with dvd
6.Back
	""")
	os.system("tput setaf 7")
	cmd=int(input("Enter your choice \t"))
	if cmd==1:
		print(subprocess.getoutput("ansible all -m ping"))	
	elif cmd==2:
		print(subprocess.getoutput('ansible all -m package -a "name=httpd state=present "'))
		print(subprocess.getoutput('ansible all -m service -a "name=httpd state=started" '))
	elif cmd==3:
		subprocess.getoutput('ansible-playbook httpserver_auth.yml')
	elif cmd==4:
		
		ip=input("Enter remote ip\t")
		user=input("Enter user name\t")
		pas=input("Enter your passwd\t")
		y=subprocess.getstatusoutput("ping -w 2 {}".format(ip)) 
		if y[0]==0:
			file= open("inventory.txt",'a')
			st="\n{} ansible_user={} ansible_ssh_pass={} ansible_connection=ssh".format(ip,user,pas)
			file.write(st)
			file.close()
			cmd="ssh root@{} date".format(ip)
			os.system(cmd)
		else:
			print("Invaild IP")


	elif cmd==5:
		os.system("ansible-playbook yum.yml")
	elif cmd==6:
		exit()

	else :
		print("Not found")
	input()
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\tRemote")
	os.system("tput setaf 7")
	

