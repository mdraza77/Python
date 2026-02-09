mail = "mdraza8297@gmail.com"

special = ['#', '$']

if len(mail) < 6:
    print("Invalid Email [length]")
elif not mail[0].isalpha():
    print("Invalid Email [start]")
elif mail.count('@') != 1:
    print("Invalid Email [@ issue]")
elif not (mail.endswith(".com") or mail.endswith(".in")):
    print("Invalid Email [domain]")
elif any(ch in mail for ch in special):
    print("Invalid Email [special char]")
else:
    print("Valid Email")
