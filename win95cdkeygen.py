import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--amount", help = "Amount of cd keys to generate", type=int, default=1)
args=parser.parse_args()

print("generating, please wait!")
for x in range(args.amount):
    pre_dash=""
    post_dash=""

    while pre_dash=="" or pre_dash==333 or pre_dash==444 or pre_dash==555 or pre_dash==666 or pre_dash==777 or pre_dash==888 or pre_dash==999:
        pre_dash=random.randrange(100,999)

    try:
        while post_dash!=sum(post_dash)%7==0:
            post_dash=int(str(random.randrange(0,9))+str(random.randrange(0,9))+str(random.randrange(0,9))+str(random.randrange(0,9))+str(random.randrange(0,9))+str(random.randrange(0,9))+str(random.randrange(0,9)))
    except TypeError:
        True

    print(str(pre_dash)+"-"+str(post_dash))
