def show():
    password=input("enter your password.......")
    if len(password) >=4 and "@" in password or "#" in password:
        if len(password)>=4 and  "@"  in password or "#"  in password :
            if password>="a" or password<="z":
                list1=["1","2","3","4","5","6","7","8","9"]
                i=0
                while i<len(list1):
                    if list1[i] in password:
                        print(" your password is strong password")
                        break
                    else:
                        print("num is not found")
                        break
                else:
                    print("num is  found")
            else:
                print("capital alphabet is not found")
        else:
             print("small char is found")
    else:
        print("your simble is not found")
show()






