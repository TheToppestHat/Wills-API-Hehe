import json
import requests

Rand = input("Would you like to have a random task or a custom task? Y or N \n")
if Rand == 'Y' or Rand == 'Yes' or Rand == 'yes' or Rand == 'y':
    API_URL = "http://www.boredapi.com/api/activity/"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json() 
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        data = None

    
elif Rand == 'N' or Rand == 'No' or Rand == 'no' or Rand == 'n':
    custom = input("\nWhat would you like to search a thing to do by? \n1 = Activity Type \n2 = Participants \n3 = Price \n4 = Accessibility\n")
    match custom:
        case "1":
            Activity = input("\nWhat kind of activity would you like to see? \n1- Education\n2- Recreational \n3- Social \n4- DIY \n5- Charity \n6- Cooking \n7- Relaxation \n8- Music \n9- Busywork\n")
            API_URL = f"http://www.boredapi.com/api/activity?activity={Activity}"
        case "2":
            Part = input("\nHow many people are there? \n")
            API_URL = f"http://www.boredapi.com/api/activity?participants={Part}"
        case "3":
            Price = input("\nWhat is the price range you are looking for? 0.1-1 is the range\n")
            API_URL = f"http://www.boredapi.com/api/activity?price={Price}"
        case "4":
            Access = input("\nHow accessible do you need the activity to be? 0.1-1 is the range\n")
            API_URL = f"http://www.boredapi.com/api/activity?accessibility={Access}"


response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json() 
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    data = None


#Here is the output for ANY activity no matter how you request it 
res = []
for key in data.keys() :
    res.append(data[key])

print(data)

if res[3] <= 0.3: price = 'Cheap'
elif res[3] <= 0.5: price = 'Moderate'
elif res[3] <= 0.8: price = 'Expensive'
elif res[3] <= 1: price = 'Really Expensive'

if res[6] <= 0.3: access = 'Very Accessible'
elif res[6] <= 0.5: access = 'Must have some Mobility, but still relatively accessible'
elif res[6] <= 0.8: access = 'Must be Mobile'
elif res[6] <= 1: access = 'Not Accessible'

print(f"\n\n\nHere is the activity requested: \n\nActivity: {res[0]}\nType of Activity: {res[1]} \nParticipants needed: {res[2]} \nPrice: {price}\nLink (If applicable): {res[4]}\nAccessibility: {access}")