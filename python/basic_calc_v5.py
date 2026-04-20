import os 

#main menu faction 
def main_menu():
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. average")
    print("6. all questions")


os.system("clear")
#inputs 
n1=float(input("enter first name:"))
n2=float(input("enter second name:"))
main_menu()
opt = int(input("enter any option: "))

if (opt==1):
    add=n1+n2
    print(f"addition is: {add}") 
elif (opt==2):
    sub=n1-n2
    print(f"subtraction is: {sub}")
elif (opt==3):
    mul=n1*n2
    print(f"multiplication is: {mul}")
elif (opt==4):
    div=n1/n2
    print(f"division is: {div}")
elif (opt==5):
    avg=(n1+n2)/2
    print(f"average is: {avg}")
elif (opt==6):
    add=n1+n2
    sub=n1-n2
    mul=n1*n2
    div=n1/n2
    avg=(n1+n2)/2

    print(f"addition is: {add}")
    print(f"subtraction is: {sub}")
    print(f"multiplication is: {mul}")
    print(f"division is: {div}")
    print(f"average is: {avg}")
else:
    print(":::invalid option:::")