import argparse
parser = argparse.ArgumentParser()
parser.add_argument("key", help = "The keys to validate, each key is seperated by a space", nargs="+", default=[])
args=parser.parse_args()
#print(args.key)

try:
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
                errors = ""

                if 1 <= int(box1p1) <= 366:
                    validity_score += 1
                else:
                    errors += "first 3 characters are not between 1 and 366, "

                if box1p2 in ["95","96","97","98","99","00","01","02"]:
                    validity_score += 1
                else:
                    errors += "last 2 characters of the first box are not in whitelist, "

                if args.key[key][5] == "-" and args.key[key][9] == "-" and args.key[key][17] == "-":
                    validity_score += 1
                else:
                    errors += "characters number 6 or 10 or 18 are not dashes, "

                if sum(int(digit) for digit in str(box3)) % 7 == 0:
                    validity_score += 1
                else:
                    errors += "sum of the second box isnt devidable by 7, "

                if len(box4) == 5:
                    validity_score += 1
                else:
                    errors += "lenght of the fourth box isnt 5, "

                if len(args.key[key]) == 23:
                    validity_score += 1
                else:
                    errors += "length of key isnt 23, "
                
                if box3[0] == "0":
                    validity_score += 1
                else:
                    errors += "first character in box3 isnt 0."
                
                #print(validity_score)
                if validity_score == 7:
                    print("PASS - "+args.key[key])
                else:
                    print("FAIL - "+args.key[key]+" - "+errors)


                #01234567890
            else: #400-5831173
                box1 = args.key[key][0] + args.key[key][1] + args.key[key][2]
                box2 = args.key[key][4] + args.key[key][5] + args.key[key][6] + args.key[key][7] + args.key[key][8] + args.key[key][9] + args.key[key][10]
                validity_score = 0
                errors = ""

                if box1 not in ["333","444","555","666","777","888","999"]:
                    validity_score += 1
                else:
                    errors =+ "first 3 characters in blacklist, "

                if sum(int(digit) for digit in str(box2)) % 7 == 0:
                    validity_score += 1
                else:
                    errors += "sum of numbers starting from the 4th character isnt devidible by 7, "

                if len(args.key[key]) == 11:
                    validity_score += 1
                else:
                    errors += "length of key isnt 11, "
                
                if int(box2[len(box2)-1]) < 8:
                    validity_score += 1
                else:
                    errors += "last character is bigger than 7."
                
                if validity_score == 4:
                    print("PASS - "+args.key[key])
                else:
                    print("FAIL - "+args.key[key]+" - "+errors)
        else:
            print("FAIL (too short) - "+args.key[key])
except ValueError:
    print("ALLOWED CHARACTERS: 0-9, '-' and the string  'oem' or 'OEM'")