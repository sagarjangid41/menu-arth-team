import os
os.system("clear")
os.system("tput setaf 3")
print("\t\t\tLocal > LVM")
os.system("tput setaf 7")
while True:
	os.system("tput setaf 4")
	print("""
	1.Full configure LVM
2.create PV
3.PV display
4.create VG
5.VG display
6.create LV
7.increase LVM size
8.Mount 
9.decrease LVM size
10.Back
	""")
	os.system("tput setaf 7")
	cmd=int(input("Enter your choice \t"))
	if cmd==1:
		hdd=input("Enter name of Partition\t")
		print("pvcreating...\n ")
		cm="pvcreate {}".format(hdd)
		os.system(cm)
		vgname=input("Create name of vgname\t")
		print("vgcreating...\n")
		cm="vgcreate {} {}".format(vgname,hdd)
		os.system(cm)
		lvname=input("create name of lvname\t")
		lvsize=input("size of lv *in G,M\t")
		print("lvcreating...\n") 
		cm="lvcreate --size {} --name {} {}".format(lvsize,lvname,vgname)
		os.system(cm)
		print("formating... \n")  
		cm="mkfs.ext4 /dev/{}/{} ".format(vgname,lvname)
		os.system(cm)
		print("\n\n Done ")
	elif cmd==2:
		hdd=input("Enter name of Partition\t")
		print("pvcreating...\n")
		cm="pvcreate {}".format(hdd)
		os.system(cm)
		print("\n\n Done ")
	elif cmd==3:
		os.system("pvdisplay")
	elif cmd==4:
		hdd=input("Enter name of PV Partition\t")
		vgname=input("Create name of vgname\t")
		print("vgcreating...\n") 
		cm="vgcreate {} {}".format(vgname,hdd)
		os.system(cm)
		print("\n\n Done ")
	elif cmd==5:
		os.system("vgdisplay")
	elif cmd==6:
		vgname=input("Enter name of Vg\t") 
		lvname=input("create name of lvname\t")
		lvsize=input("size of lv *in G,M\t")
		print("lvcreating...\n")
		cm="lvcreate --size {} --name {} {}".format(lvsize,lvname,vgname)
		os.system(cm)
		print("\n\n Done ")
	elif cmd==7:
		lvexsize=input("Enter Lv extend size *in G,M\t")
		vgname=input("Enter name of VG\t")
		lvname=input("Enter name of LV\t")
		cm="lvextend --size {} /dev/{}/{} ".format(lvexsize,vgname,lvname)
		os.system(cm)
		cm="resize2fs /dev/{}/{}".format(vgname,lvname)
		os.system(cm)
		print("\n\n Done ")
	elif cmd==8:
		partition=input("Enter mount device name\t")
		folder=input("Enter folder name\t")
		cm="mount {} {} ".format(partition,folder)
		os.system(cm)
		print("\n\n Done ")
	elif cmd==9:
		folder=input("Enter Mounted folder name")
		lv=input("Enter LVM name")
		cm = "umount {}".format(folder)
		os.system(cm)
		cm = "e2fsck -f {}".format(lv)
		os.system(cm)
		resize=input("Enter new size *in G,M")
		cm = "resize2fs {} {}".format(lv,resize)
		os.system(cm)
		cm = "lvreduce -L {} {}".format(resize,lv)
		os.system(cm)
	elif cmd==10:
		exit()

	else :
		print("Not found")
	input()
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\tLocal > docker")
	os.system("tput setaf 7")
	
