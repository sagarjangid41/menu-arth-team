import os
os.system("clear")
os.system("tput setaf 3")
print("\t\t\tLocal > docker")
os.system("tput setaf 7")
while True:
	os.system("tput setaf 4")
	print("""Docker Menu
1.Runing container
2.All container
3.Images 
4.Launch container
5.Stop container 
6.start container
7.Attach container
8.Back
	""")
	os.system("tput setaf 7")
	cmd=int(input("Enter your choice \t"))
	if cmd==1:
		os.system("docker ps")
	elif cmd==2:
		os.system("docker ps -a")
	elif cmd==3:
		os.system("docker images")
	elif cmd==4:
		name=input("Enter container name\t")
		image=input("Enter container image name\t")
		os.system("docker run -it --name {} {}".format(name,image))
	elif cmd==5:
		sname=input("Enter container name\t")
		os.system("docker stop {}".format(sname))
	elif cmd==6:
		sname=input("Enter container name\t")
		os.system("docker start {}".format(sname))
	elif cmd==7:
		aname=input("Enter Container name\t")
		os.system("docker attach {}".format(aname))
	elif cmd==8:
		exit()

	else :
		print("Not found")
	input()
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\tLocal > docker")
	os.system("tput setaf 7")
	
