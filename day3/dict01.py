mydict={1:1,2:4,3:9,4:16,5:25}

print(mydict.get(1))
print(mydict.get(4))
print(mydict[2])

mydict2={'내가':'만약','트와이스':'정연'}

print(mydict2['내가'])
print(mydict2['트와이스'])

mydict2['SKT T1']='뱅울프'
print(mydict2['SKT T1'])
print(mydict2)

phone_list={}
phone_list['dabin']='01045760460'
phone_list['chunsejin']='01012345678'

print(phone_list['dabin'])
print(phone_list)

phone_list['dabin']='0109999999'
print(phone_list['dabin'])