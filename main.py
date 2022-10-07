import datetime
from logicReq import cleaner, newspaper
from guide import modifiedGuideLine, guideLine

nextClean = ""
timeC = ""
day = 0
shoppingList = []
repeat = True

print("Hi, You can ask me questions like this\n")
for key in guideLine:
    print(key)

print("\n")
while repeat:
    a = input("Enter : ")

    # Room cleaning
    if a.upper() == "CLEAN MY ROOM":
        currentTime = datetime.datetime.now()
        currentTimeC = currentTime.time()
        if nextClean == "":
            nextClean, timeC = cleaner(currentTime, a)
        elif currentTimeC > nextClean.time():
            nextClean, timeC = cleaner(currentTime, a)
        elif currentTimeC < nextClean.time():
            timeS = currentTime
            if timeS.minute < timeC.minute:
                value = timeS.minute
                value = value + 60
                print(f"Room was just cleaned {value - timeC.minute} minutes ago. I hope its not dirty")
            else:
                print(f"Room was just cleaned {timeS.minute - timeC.minute} minutes ago. I hope its not dirty")

    # Fetching newspaper
    elif a.upper() == "FETCH THE NEWSPAPER":
        currentTime = datetime.datetime.now()
        day = newspaper(currentTime, day, a)

    # Shopping list
    elif a.upper() == "READ MY SHOPPING LIST":
        if not shoppingList:
            print(modifiedGuideLine[a.upper()])
        else:
            print("Here is your shopping list.")
            for item in shoppingList:
                print(item)

    # Adding to shopping list
    elif "ADD" in a.upper() and "TO MY SHOPPING LIST" in a.upper():
        item = a.upper().removeprefix("ADD ")
        item = item.removesuffix(" TO MY SHOPPING LIST")
        if item.capitalize() in shoppingList:
            print(f'You already have {item.capitalize()} on your shopping list')
        else:
            print(f'{item.capitalize()} added to your shopping list')
            shoppingList.append(item.capitalize())

    # Basic requests
    elif a.upper() in modifiedGuideLine:
        print(modifiedGuideLine[a.upper()])

    # Unknown requests
    else:
        print("Hmm.. I don't know that")

    question = input("\nHi, do you have another request for me\nYes/No\n")
    if question.upper() == "YES" or question.upper() == "Y":
        continue
    else:
        repeat = False
