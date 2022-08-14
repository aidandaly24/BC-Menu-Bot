from datetime import datetime
from collections import defaultdict


def response(message, data):
    message = message.strip()

    location = None
    if "mac" in message or "mcellroy" in message or "carney" in message:
        location = "Carney's"
    elif "after" in message or "dark" in message or "kevork" in message:
        location = "BC After Dark"
    elif "bean" in message:
        location = "The Bean Counter"
    elif "chocalate" in message or "bar" in message:
        location = "Chocolate Bar"
    elif "coro" in message:
        location = "CoRo Café & Market"
    elif "eagle" in message:
        location = "Eagles' Nest"
    elif "hillside" in message:
        location = "Hillside Café"
    elif "addie" in message:
        location = "The Loft @ Addie's"
    elif "legal" in message:
        location = "Legal Grounds"
    elif "lower" in message or "corcoran" in message:
        location = "Lower Live"
    elif "rat" in message:
        location = "Lyons Hall"
    elif "stu" in message:
        location = "Stuart Dining Hall"
    elif "market" in message:
        location = "The Market @ Corcoran"
    elif "tully" in message or "tullies" in message:
        location = "Tully Cafe"
    else:
        location = "unknown"

    mealTime = None
    if "break" in message:
        mealTime = "BREAKFAST"
    elif "lun" in message:
        mealTime = "LUNCH"
    elif "din" in message:
        mealTime = "DINNER"
    elif "late" in message:
        mealTime = "LATE NIGHT"

    if location == "unknown":
        return f"""The location {message} isn't currently known as a BC dining hall or café.
        This could be an error. If it is feel free to email: dalybu@bc.edu.
        Otherwise please try again."""

    mealsDict = defaultdict(dict)

    for i in range(len(data)):
        mealName = data[i]["Meal_Name"].upper().strip()
        category = data[i]["Menu_Category_Name"].strip()
        foodName = data[i]["Recipe_Print_As_Name"].strip()
        if data[i]["Location_Name"].strip() == location.strip():
            if mealName in mealsDict:
                if category in mealsDict[mealName]:
                    mealsDict[mealName][category].append(foodName)
                else:
                    mealsDict[mealName][category] = [foodName]
            else:
                mealsDict[mealName][category] = [foodName]

    if len(mealsDict) == 0:
        return f"It seems like {location} may be closed today. If this isn't true this may be an error on my end. Please email dalybu@bc.edu letting me know."

    finalMessage = ""

    for meal in mealsDict:
        if mealTime == None:
            finalMessage += meal + ":\n"
            for category in mealsDict[meal]:
                finalMessage += category + ":\n"
                for i, item in enumerate(mealsDict[meal][category]):
                    finalMessage += f"  {(i+1)}. {item}\n"
                finalMessage += "\n"

            finalMessage += "\n"
        else:
            if meal == mealTime:
                finalMessage += meal + ":\n"
                for category in mealsDict[meal]:
                    finalMessage += category + ":\n"
                    for i, item in enumerate(mealsDict[meal][category]):
                        finalMessage += f"  {(i+1)}. {item}\n"
                    finalMessage += "\n"

                finalMessage += "\n"

    return finalMessage
