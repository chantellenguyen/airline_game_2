import requests, json
import math

vacation_list = []
# Pass your API key here

api_key = "1cc72f37ccff0068813610aa29f347d3"

ow_url = "http://api.openweathermap.org/data/2.5/weather?"

print("Welcome to Brie's travel agency!!! Enter 5 cities you would like to travel to!!")
# Pass city name

for i in range(5):
    city = input("Enter city name: ")

    call_url = ow_url + "appid=" + api_key + "&q=" + city

    # Fire a GET request to API

    response = requests.get(call_url)

    # fetch data from JSON response

    data = response.json()

    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        print("Temperature (in celsius) =" + str(math.ceil(current_temperature - 273)))
    else:
        print(" City Not Found ")

    temperature = math.ceil(current_temperature - 273)

    # If the temperature is above 15 degrees, print out "This (city) is a great vacation spot and add that into vacation list

    # else, print out it is too cold to travel there now!

    if (temperature > 15):
        print("This" + str(city) + "is a great vacation spot!!!!")
        vacation_list.append(city)
    else:
        print("This is too cold for vacation!!!!")

passengers = []

print("Here are the recommended vacation spots: ")

# Print out the items in vacation list looking this way
# 1. City name
# 2. City name..
# 3. City name...

for i in range(len(vacation_list)):
    print(str(i + 1) + ". " + vacation_list[i])

# Ask the user what city they would like to fly to

citychoice = input("What city would you like to fly to ma'am/sir? ")

# Ask the person how many people are flying with them

passenger_num = int(input("How many people are flying with you? "))

# based on the number of people, create a for loop and request an input for each name.
# add each passenger name into the passengers list

for i in range(passenger_num):
    passenger_name = input("what's the passenger name? ")
    passengers.append(passenger_name)

# Print out the names in passengers list by saying, "You are traveling with, name1, name2, name3 ... etc"

print("You are travelling with: ")
for p in passengers:
    print(p)

# If the city is in the list, print out "We are preparing your travel vouchers"
# print have a safe flight
if citychoice in vacation_list:
    print("We are preparing your travel vouchers")
    print("Have a safe flight")
else:
    print("Sorry you cannot travel to this city at this time.")

# else
# print out "we cant seem to locate a route for this city"

