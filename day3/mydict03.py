mydict={'math':100,'english':200,'science':500}

for i in mydict:
    print(i)
    print(mydict[i])
for mykey,myvalue in mydict.items():
    print('My key is',mykey,' and my value is ',myvalue)