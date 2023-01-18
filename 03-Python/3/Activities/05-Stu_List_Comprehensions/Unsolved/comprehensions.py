names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)


# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = [x.lower() for x in names]
lowercased
# @TODO: Use a list comprehension to create a list of title cased names
# https://www.tutorialspoint.com/python/string_title.htm
title_cased = [x.title() for x in names]
title_cased
invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in title_cased]

for invitation in invitations:
    print(invitation)

print(f"Dear {names[0]}, please come to the wedding this Saturday!")
print(f"Dear {names[1]}, please come to the wedding this Saturday!")
print(f"Dear {names[2]}, please come to the wedding this Saturday!")
print(f"Dear {names[3]}, please come to the wedding this Saturday!")
print(f"Dear {names[4]}, please come to the wedding this Saturday!")
