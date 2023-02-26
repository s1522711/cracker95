import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", help = "The type of the key, OEM or CDKey", type=str, default="none")
parser.add_argument("-a", "--amount", help = "Amount of cd keys to generate", type=int, default=1)
args=parser.parse_args()

if args.type == "none":
    print("Please provide the type of the key with this argument: --type oem/cdkey")
    exit(1)


if args.type.lower() == "cdkey" or args.type.lower() == "cd":
    for x in range(args.amount):
        pre_dash=""
        post_dash=555555

        while pre_dash=="" or pre_dash==333 or pre_dash==444 or pre_dash==555 or pre_dash==666 or pre_dash==777 or pre_dash==888 or pre_dash==999:
            pre_dash=random.randrange(100,999)

        
        while sum(int(digit) for digit in str(post_dash))%7!=0:
            post_dash=int(str(random.randrange(1,9))+str(random.randrange(1,9))+str(random.randrange(1,9))+str(random.randrange(1,9))+str(random.randrange(1,9))+str(random.randrange(1,9))+str(random.randrange(1,9)))

        print(str(pre_dash)+"-"+str(post_dash))
        
if args.type.lower() == "oem":
    for x in range(args.amount):
        box1=""
        box3=55555
        box4=""
        
        box1=int(str(random.randrange(100,365))+str(random.randrange(95,99)))
        
        try:
            while sum(int(digit) for digit in str(box3)) % 7 != 0:
                box3=int(str(random.randrange(1,9))+str(random.randrange(1,9))+str(random.randrange(1,9))+str(random.randrange(1,9))+str(random.randrange(1,9)))
        except TypeError:
            True
        
        box4 = random.randint(10000,99999)
        
        print(str(box1)+"-OEM-00"+str(box3)+"-"+str(box4))
