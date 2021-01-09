first_name = input("Enter first name.")
last_name = input("Enter last name.")
full_name = first_name+" "+last_name

for i in reversed(range(len(full_name))):
    print(full_name[i],end="")
