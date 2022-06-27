import json,os
list=[]
def password():
    g()
    if len(passwrd)<6:
        print("password must be more than or equals 6 letters")
    else:
        if passwrd[0].isdigit():
            print("password cannot start with digit")
        u=0
        d=0
        s=0
        for i in range(len(passwrd)):
            if passwrd[i] ==" " or passwrd[i]=="/":
                print("password can't include space and '/'")
            if passwrd[i].isupper():
                u+=1
            elif passwrd[i].isdigit():
                d+=1
            elif passwrd[i] in "!@#$%&*%_":
                s+=1
        if u>0 and d>0 and s>0:
            print("valid password")
        else:
            print("weak password!!!\npassword must contain atleast one uppercase and one digit and one special character")
            password()

        confirm_password=input("confirm password:  ")
        if passwrd==confirm_password:
            print("password matched")
            password()
        else:
            print("both password doesn't match")
            password()
def g():
    global list
    global passwrd
    global name
    global file_name
    name=input("enter you name   ")
    passwrd=input("enter password   ")
    file_name="account.json"


def sign_up():
    password()
    if(os.path.isfile("account.json")):
        file=open(file_name,"r")
        dic2=json.load(file)
        for  i in dic2["user"]:
            if i["name"]==name and i["password"]==passwrd:
                print("acount already exist")
                sign_up()
        else:
            descriptions=["dob:  ","gender:  ","address:  ","designation:  ","bio:  "]
            i=0
            dic={}
            d={}
            while i<len(descriptions):
                d[descriptions[i]]=input(descriptions[i])
                i+=1
            dic["name"]=name
            dic["password"]=passwrd
            dic["profile"]=d
            x=dic2["user"]
            x.append(dic)
            with open(file_name,"w+") as file1:
                json.dump(dic2,file1,indent=4)
               
    
                            
    else:
        descriptions=["dob:  ","gender:  ","address:  ","designation:  ","bio:  "]
        j=0
        d1={}
        dic={}
        list=[]
        d={}
        while j<len(descriptions):
            d[descriptions[j]]=input(descriptions[j])
            j+=1
        dic["name"]=name
        dic["password"]=passwrd
        dic["profile"]=d
        list.append(dic)
        d1["user"]=list
        with open(file_name,"w+") as file1:
            json.dump(d1,file1,indent=4)
    
        
    
def log_in():
    g()
    a=open("account.json","r")
    f=json.load(a)
    for i in f["user"]:
        if i["name"]==name:
            if i['password']==passwrd:
                print("Login successful")
                print(i)
                break
            else:
                print("incorrect password")
    else:
        print("incorrect username")


def main():
    option=int(input("Enter 1 for log-in:\nEnter 2 for sign-up: "   ))
    if option==1:
        log_in()
        print(name,"log-in successfully")
    elif option==2:
        sign_up()
        print(name,"sign-up successfully")
    else:
        print("something went wrong!!!")
        print("please try again!!!")
        main()
main()




