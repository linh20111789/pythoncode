
specialLetter = ['!','@','#','$','%','^','&','*']

def split(word):
    return [char for char in word]


def containsLetterAndNumberAndSpecial(input):
    has_letter = False
    has_number = False
    has_special = False
    for x in input:
        if x.isalpha():
            has_letter = True
        elif x.isnumeric():
            has_number = True
        if x in specialLetter:
            has_special = True
            print("Special true")    
        if has_letter and has_number and has_special:
            return True
    return False
    
strInput = input("Enter password: ")
print(strInput)
print(len(strInput))

if len(strInput) > 7 and containsLetterAndNumberAndSpecial(strInput):
    print("Strong password")
else:
    print("Password is not strong")


