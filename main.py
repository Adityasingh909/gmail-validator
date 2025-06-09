email = input("Enter your Email: ")  # adityasingh917023@gmail.com
k ,j,l= 0,0,0
if(len(email)>=6):
    if(email[0].isalpha()):
        if(("@" in email) and email.count("@") == 1 and ("gmail" in email)  ):
            if (email.endswith(("@gmail.com", "@gmail.in", "@gmail.co.in"))):
                for i in email:
                    if (i.isalpha()):
                        if i.isupper():
                            k = 1
                    elif i.isspace():
                        j =1
                    elif i.isdigit():
                        continue
                    elif i in ["_" , "@" ,"."]:
                        continue
                    else:
                        l =1
                if(k == 1 or j==1 or l == 1):
                    print("wrong")
                else:
                    print("Right")
            else:
                print("Wrong mail")
        else:
             print("wrong mail !")
    else:
        print("wrong mail !")
else:
    print("wrong mail !")