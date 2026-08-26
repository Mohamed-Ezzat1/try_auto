age = int(input("enter age "))
id = input("do you have any id y/n ")
res = input("are you a residrent y/n ")


if age >= 18 :
    age_check = True
else :
    age_check =False

if id == "y" :
    id_check = True
else :
    id_check =False

if res == "y" :
    res_check = True
else :
    res_check =False

if age_check and id_check and res_check :
    print("elgible")
else:
    if not id_check :
        print("not eligible by id")
    if not age_check :
        print("not eligible by age")
    if not res_check :
        print("not eligible by res")
    