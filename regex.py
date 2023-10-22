#a-z
#0-9
#. _ 1 time
#@ 1 time
# . 2,3 position
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("enter your email: ")
if re.search(email_condition,user_email):
    print("right email ")
else:
    print("wrong email ")
    