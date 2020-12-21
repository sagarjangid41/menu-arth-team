import os
import subprocess
import getpass
os.system("sudo clear")
os.system("tput setaf 3")	
print("\t\tWelcome \n")
os.system("tput setaf 7")
system = input("Choose system (remote/local)\t")
if  system=="remote":
	os.system("python3 remote.py")
else :
	while True:
		os.system("tput setaf 4")
		print(""" My manu
			  1.Date 
			  2.Cal
			  3.Lvm
			  4.Docker
			  5.Hadoop
			  6.AWS
			  7.Exit
		""")
		os.system("tput setaf 7")
		cmd = int(input("Enter your choice \t"))
		if cmd == 1:
			print(subprocess.getoutput("sudo date"))
		elif cmd==2 :
			print(subprocess.getoutput("sudo cal"))
		elif cmd==3 :
			os.system("sudo python3 lvm.py")
		elif cmd==4 :
			os.system("sudo python3 docker.py")
		elif cmd==5 :
			print("hadoop")
		elif cmd ==6:
			os.system("python3 aws.py")
		elif cmd==7:
			exit()
		else :
			print("Not found")
		input()
		os.system("sudo clear")
		os.system("tput setaf 3")
		print("\t\t\tLocal")
		os.system("tput setaf 7")

