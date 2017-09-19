import re
from termcolor import colored


shakes = open("details_refactored.txt", "r")
call = open("call.txt", "w")

data = []
email = []
for line in shakes:
    if re.match("Email :", line):
    # if re.match("Company Name :|Email :|Telephone :", line):
        data.append(str(line).split(":"))
        #filter(None, data[1])
        #raw_input()
        # if data[1] is not None:
        #     print data[1]
count = 3000
for value in data:
    filtered = sorted(set(email))
    if count is 0:
        break
    #count -= 1
    if value[1] != "\n":
        # email.append(value[1])
        email.append(value[1])
        #print value[1]
        # call.write(value[1])
# call.close()

# filtered1 = sorted(set(e_mail))
filtered = sorted(set(email))

l_range = 500
r_range = 2000
print colored('Number Of Emails: ' + str(len(filtered[l_range:r_range])), 'red', attrs=['reverse', 'blink'])
# print "Number Of Emails: " + str(len(filtered))
#print filtered[1000:1500]

call.write(str(filtered[l_range:r_range]))
call.close()

with open(r'call.txt', 'r') as infile, open(r'call_filtered.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("\\n", "")
    data = data.replace("'", "")
    data = data.replace("[", "")
    data = data.replace("]", "")
    outfile.write(data)
    outfile.close()

with open(r'call_filtered.txt', 'r') as infile, open(r'call.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace(",", "\n")
    # data = data.replace(" ", "")
    # data = data.replace("\n", "")
    outfile.write(data)
    outfile.close()