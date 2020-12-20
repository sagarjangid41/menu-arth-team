import os
os.system("clear")
os.system("tput setaf 3")
print("\t\t\t Cloud AWS")
os.system("tput setaf 7")
while True:
	os.system("tput setaf 4")
	print("""
	
	
    1. Create Key Pair
    2. Create Security Groups
    3. Launch Instance
    4. Create EBS Volume
    5. Attach EBS Volume to Instance
    6. Cloud Front setup
    7.Create S3 bucket
	8.Back
	""")
	os.system("tput setaf 7")
	cmd=int(input("Enter your choice \t"))
	if cmd==1:
        keyname=input("Enter the kye name\t")
		os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
	elif cmd==2:
        groupname=input("Enter the Security Group name\t")
        description=input("Enter the Description\t")
		os.system("aws ec2 create-security-group --group-name {} --description {}".format(groupname,description))
	elif cmd==3:
        image=input("Enter the Image-Id\t")
        instance=input("Enter the instance type\t")
        keyname=input("Enter the keyname\t")
        security=input("Enter the security group name\t")
        count = input("Enter how many Instance launch\t")
		os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-groups {} --count {}".format(image,instance,keyname,security,count))
	elif cmd==4:
        availbility=input("Enter availbility zone\t")
        size =int(input("Enter the size of volume\t"))
        os.system("aws ec2 create-volume --availbility-zone {} --no-encrypted --size {}".format(availbility,size))
	elif cmd==5:
        instance=input("Enter the instance name\t")
        volume=input("Enter the volume name\t")
        os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/xvdf")
	elif cmd==6:
        domain=input("Enter the origin-domain-name\t")
        root=input("Enter the default-root-object\t")
        os.system("aws cloudfront create-distribution --origin-domain-name {} --default-root-object {}".format(domain,root))
	elif cmd==7:
        bucket=input("Enter the Bucket name")
        region=input("Enter the Region name")
		os.system("aws s3api create-bucket --bucket {} --region {}".format(bucket,region))
    elif cmd==8:
        exit()
	else :
		print("Not found")
	input()
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\tLocal > docker")
	os.system("tput setaf 7")
	
