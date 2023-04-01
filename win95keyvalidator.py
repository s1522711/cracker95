import argparse
parser = argparse.ArgumentParser()
parser.add_argument("key", help = "The key to validate", type=str, default="none")
args=parser.parse_args()

if args.key == "none":
    print("PLEASE INPUT A KEY")
                                #01234567890123456789012
elif "oem" in args.key.lower(): #12996-OEM-0247555-81624
    box1p1 = args.key[0] + args.key[1] + args.key[2]
    box1p2 = args.key[3] + args.key[4]
    box3 = args.key[10] + args.key[11] + args.key[12] + args.key[13] + args.key[14] + args.key[15] + args.key[16]
    box4 = args.key[18] +args.key[19] + args.key[20] + args.key[21] + args.key[22]
    validity_score = 0

    if 1 <= int(box1p1) <= 366:
        validity_score += 1
    if box1p2 in ["95","96","98","99","00","01","02"]:
        validity_score += 1
    if args.key[5] == "-" and args.key[9] == "-" and args.key[17] == "-":
        validity_score += 1
    if sum(int(digit) for digit in str(box3)) % 7 == 0 and box3[0] == "0":
        validity_score += 1
    if len(box4) == 5:
        validity_score += 1
    if len(args.key) == 23:
        validity_score += 1
    
    #print(validity_score)
    if validity_score == 6:
        print("PASS")
    else:
        print("FAIL")

        
      #01234567890
else: #400-5831173
    box1 = args.key[0] + args.key[1] + args.key[2]
    box2 = args.key[4] + args.key[5] + args.key[6] + args.key[7] + args.key[8] + args.key[9] + args.key[10]
    validity_score = 0

    if box1 not in ["333","444","555","666","777","888","999"]:
        validity_score += 1
    if args.key[3] == "-":
        validity_score += 1
    if sum(int(digit) for digit in str(box2)) % 7 == 0 and int(box2[len(box2)-1]) < 8:
        validity_score += 1
    if len(args.key) == 11:
        validity_score += 1
    
    if validity_score == 4:
        print("PASS")
    else:
        print("FAIL")