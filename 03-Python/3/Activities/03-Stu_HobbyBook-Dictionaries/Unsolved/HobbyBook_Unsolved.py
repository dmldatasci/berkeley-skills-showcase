# # Hobby Book: Dictionaries

# In this activity, you will create and access dictionaries that are based on your own hobbies.

# ## Instructions

# 1. Create a dictionary to store the following information:
my_info = {
    "name":"Khaled Karman",
    "age":45000,
    "hobbies":["Movies", "Travel", "happy", "books"],
    "wake":{
        "Mon": "5:30",
        "Teu": "6:00",
        "Wed": "5:30",
        "Thu": "5:30",
        "Fri": "5:30",
        "Sat": "11:30",
    },
}
my_info["age"]

my_info["hobbies"][-2]
my_info["wake"]["Thu"]

for i in range(5):
    print(i)

a_list = [
    "Amanda",
    "Jin",
    "David"
]


messages = []
for x in a_list:
    messages.append("Hello " + x)


messages = ["Hello " + x for x in a_list]


fish = "halibut"

[x for x in fish]

my_info = {
    "name":"Khaled Karman",
    "age":45000,
    "hobbies":["Movies", "Travel", "happy", "books"],
    "wake":{
        "Mon": "5:30",
        "Teu": "6:00",
        "Wed": "5:30",
        "Thu": "5:30",
        "Fri": "5:30",
        "Sat": "11:30",
    },
}
all = []
for x in my_info:
    print(x, my_info[x])
    all.append(my_info[x])
all

[x for x in my_info]

[my_info[x] for x in my_info]

my_info

# * Your name
# * Your age
# * A list of a few of your hobbies
# * A dictionary that includes a few days and the time you typically wake up on those days

# 2. Print out your name, how many hobbies you have, and a time you typically wake up during the week.

# - - -

# © 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
