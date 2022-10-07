# Capitalising the requests
def modifyString(s):
    return s.upper()


guideLine = {"Hey. How are you?": "Hello, I am doing great",
             "Clean my room": "Room is cleaned. It looks tidy now. Job completed",
             "Fetch the newspaper": "Here is your newspaper",
             "Read my shopping list": "You have no items in your shopping list",
             "Add item to my shopping list": "added to your shopping list",
             "How's the weather outside?": "It's pleasant outside. You should take a walk."}
modifiedGuideLine = {}

for key in guideLine:
    modifiedGuideLine[modifyString(key)] = guideLine[key]
