
def split(word):
    return [char for char in word]

strInput = input(" Enter sentence: ").lower()
print(strInput)
listStr = split(strInput)
count = 0
character = input("enter character : ").lower()
for i in listStr:
    if i == character:
        count = count+1

print(f"Number of {character} is ", count)

