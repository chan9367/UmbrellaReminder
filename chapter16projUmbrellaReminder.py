import requests, bs4
from datetime import datetime
import os
from twilio.rest import Client

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.62422000000004&lon=-73.98326999999995')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

isItRaining = soup.find("p", class_="myforecast-current").getText()

#figure out our own sid and auth token in twilio
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
#replace with your on twilio number and cellphone
myTwilioNumber = '+14955551234'
myCellPhone = '+14955558888'
dt = datetime.datetime.now()

if isItRaining == 'Raining':
    message = client.messages \
        .create(
            from_=myTwilioNumber,
            body='RAINING!!! GET AN UMBRELLA!',
            send_at=datetime(dt.year, dt.month, dt.day, 7, 30, 0),
            schedule_type='fixed',
            to=myCellPhone
        )

    print(message.sid)