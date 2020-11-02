file = open('/home/user/Desktop/Friday.txt','w+')
file.write("I am crazy\n")
file.writelines("Beer Friday\n")
file.write("Vodka Friday\n")
file.close()

file = open('/home/user/Desktop/Friday.txt','r')
for each in file:
    print(each)


