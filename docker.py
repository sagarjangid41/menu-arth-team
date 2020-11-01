import os
os.system("clear")
os.system("tput setaf 3")
print("\t\t\tLocal > docker")
os.system("tput setaf 7")
while True:
	os.system("tput setaf 4")
	print("""
	1.Runing container
	2.All container
	3.Images 
	4.Launch container
	5.Stop container 
	6.Attach container
	7.Back
	""")
	os.system("tput setaf 7")
	cmd=int(input("Enter your choice \t"))
	if cmd==1:
		print("docker ps")
	elif cmd==2:
		print("docker ps -a")
	elif cmd==3:
		print("docker images")
	elif cmd==4:
		name=input("Enter container name\t")
		image=input("Enter container image name\t")
		print("docker run -it --name {} {}".format(name,image))
	elif cmd==5:
		sname=input("Enter container name\t")
		print("docker stop {}".format(sname))
	elif cmd==6:
		aname=input("Enter Container name\t")
		print("docker attach {}".format(aname))
	elif cmd==7:
		exit()

	else :
		print("Not found")
	input()
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\tLocal > docker")
	os.system("tput setaf 7")
	
