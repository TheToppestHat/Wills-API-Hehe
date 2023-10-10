import json
import requests

Rand = input("Would you like to have a random task or a custom task? Y or N \n")
if Rand == 'Y' or Rand == 'Yes':
    API_URL = "http://www.boredapi.com/api/activity/"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json() 
        
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        data = None
elif Rand == 'N' or Rand == 'No':
    Activity = input("What kind of activity would you like to see? \n1- Education\n2- Recreational \n3- Social \n4- DIY \n5- Charity \n6- Cooking \n7- Relaxation \n8- Music \n9- Busywork\n")

res = []
for key in data.keys() :
    res.append(data[key])

if res[3] <= 0.3: price = 'Cheap'
elif res[3] <= 0.5: price = 'Moderate'
elif res[3] <= 0.8: price = 'Expensive'
else: price = 'Really Expensive'

if res[6] <= 0.3: access = 'Very Accessible'
elif res[6] <= 0.5: access = 'Must have some Mobility, but still relatively accessible'
elif res[6] <= 0.8: access = 'Must be Mobile'
else: access = 'Not Accessible'

print(f"\n\n\nHere is the activity requested: \n\nActivity: {res[0]}\nType of Activity: {res[1]} \nParticipants needed: {res[2]} \nPrice: {price}\nLink (If applicable): {res[4]}\nAccessibility(1-10): {access}")