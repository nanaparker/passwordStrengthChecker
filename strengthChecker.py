# Author: Nana Parker
# Date: 8th March, 2022
# Title: Password Strength Checker

from password_strength import PasswordPolicy
import argparse

parser = argparse.ArgumentParser(description = "Generate QR Codes.")
parser.add_argument("pwd", help="Password to be tested")
args = parser.parse_args()

policy = PasswordPolicy.from_names(
    length=8, uppercase=2,
    numbers=2, special=2
)

# Step 1: Check whether password has all the items stated in 
# the policy

# Step 2: If the password passes the first stage, check the 
# strength of the password

val = policy.password(args.pwd)

if (len(val.test()) > 0):
    for i in range(len(val.test())):
        print("You need to have: "+str(val.test()[i]))
else:
    if (val.strength() > 0.8):
        print("Very Good Password")
    elif (val.strength() > 0.5 and val.strength() < 0.8):
        print("Good Password")
    else:
        print("Weak Password")    
