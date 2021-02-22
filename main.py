import requests
from datetime import datetime , time
import smtplib



my_lat = 25.594095
my_lon = 85.137566

def is_iss_overhead():
    response = requests.get(url = 'http://api.open-notify.org/iss-now.json')
    #response.json is returning a dictionary
    data  = response.json()["iss_position"]
    latitude = float(data["latitude"])
    longitude = float(data["longitude"])
    iss_position = (latitude , longitude)

    #if iss is close to my place
    if my_lat - 5 <= latitude <= my_lat + 5:
        return True

def is_night():

    parameters = {
    "lat" : 25.594095 ,
    "lng" : 85.137566 ,
    "formatted" : 0
    }
    response  = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(":")[0])


    time_now = datetime.now().hour


    #checking if its night 
    if time_now >= sunset or time_now <= sunrise :
        return True







my_email = "trackeriss511@gmail.com"
password = "domd1234"

while True:
    time.sleep(45)#this will automatically run after 45 seconds and check wheather it is over or not
    if is_iss_overhead() and is_night() is True:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email ,password)
            connection.sendmail(
                from_addr= my_email ,
                to_addrs= my_email ,
                msg="subject:Time to look up in the sky \n\n The iss is above you now :"
            )

