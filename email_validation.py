from validate_email import validate_email
import re
from termcolor import colored
call = open("call.txt", "r")
filtred = open("call_filtered.txt", "w")

data = []

for line in call:
    try:
        res = validate_email(str(line[:-1]),verify=True)
        if  res == True:
        # if re.match("Company Name :|Email :|Telephone :", line):
            filtred.write(line[:-1])
            filtred.write("\n")
        #     filtered.write("\n")
            print colored(str(line[:-1]) + " --> Valid", 'green', attrs=['reverse', 'blink'])
            # print str(line[:-1]) + " Valid"
            #data.append(str(line))
    except:
        print colored(str(line[:-1]) + " --> Invalid", 'red', attrs=['reverse', 'blink'])
call.close()
filtred.close()
# is_valid = validate_email('uiu485025@gmail.com',verify=True)
# is_valid = validate_email('uiu025@gmail.com',check_mx=True)