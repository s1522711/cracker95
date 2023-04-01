import argparse
parser = argparse.ArgumentParser()
parser.add_argument("key", help = "The keys to validate, each key is seperated by a space", nargs="+", default=[])
args=parser.parse_args()
#print(args.key)

for key_loop in range (len(args.key)):
    key = key_loop - 1
    #print(key)
    #print(args.key[key+1])

    if len(args.key[key]) == 11 or len(args.key[key]) == 23:        
                                           #01234567890123456789012
        if "oem" in args.key[key].lower(): #12996-OEM-0247555-81624
            box1p1 = args.key[key][0] + args.key[key][1] + args.key[key][2]
            box1p2 = args.key[key][3] + args.key[key][4]
            box3 = args.key[key][10] + args.key[key][11] + args.key[key][12] + args.key[key][13] + args.key[key][14] + args.key[key][15] + args.key[key][16]
            box4 = args.key[key][18] +args.key[key][19] + args.key[key][20] + args.key[key][21] + args.key[key][22]
            validity_score = 0

            if 1 <= int(box1p1) <= 366:
                validity_score += 1
            if box1p2 in ["95","96","97","98","99","00","01","02"]:
                validity_score += 1
            if args.key[key][5] == "-" and args.key[key][9] == "-" and args.key[key][17] == "-":
                validity_score += 1
            if sum(int(digit) for digit in str(box3)) % 7 == 0 and box3[0] == "0":
                validity_score += 1
            if len(box4) == 5:
                validity_score += 1
            if len(args.key[key]) == 23:
                validity_score += 1
            
            #print(validity_score)
            if validity_score == 6:
                print("PASS - "+args.key[key])
            else:
                print("FAIL - "+args.key[key])


              #01234567890
        else: #400-5831173
            box1 = args.key[key][0] + args.key[key][1] + args.key[key][2]
            box2 = args.key[key][4] + args.key[key][5] + args.key[key][6] + args.key[key][7] + args.key[key][8] + args.key[key][9] + args.key[key][10]
            validity_score = 0

            if box1 not in ["333","444","555","666","777","888","999"]:
                validity_score += 1
            if args.key[key][3] == "-":
                validity_score += 1
            if sum(int(digit) for digit in str(box2)) % 7 == 0 and int(box2[len(box2)-1]) < 8:
                validity_score += 1
            if len(args.key[key]) == 11:
                validity_score += 1
            
            if validity_score == 4:
                print("PASS - "+args.key[key])
            else:
                print("FAIL - "+args.key[key])
    else:
        print("FAIL (too short) - "+args.key[key])