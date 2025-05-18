import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL = "uremail@gmail.com"
MY_PASSWORD = "urpassword"
MY_LAT = 21.916222
My_LONG = 95.955971


def is_iss_overhead():
    response = requests.get("https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT <= iss_latitude <= MY_LAT+5 and My_LONG-5 <= iss_longitude <= My_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": My_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="to-sender@gmail.com",
            msg="Subject:Look Up👆\n\nThs ISS is above you in the sky."
        )
