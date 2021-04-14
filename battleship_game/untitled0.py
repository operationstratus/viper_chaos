inp = ""
choices = ["x", "b", "a"]
while not inp in choices:
    inp = input("För abryt tryck x. För förolämpning tryck b eller a: ")

if inp == "a":
    print("Fuck you!")
if inp == "b":
    print("B for bitch!")