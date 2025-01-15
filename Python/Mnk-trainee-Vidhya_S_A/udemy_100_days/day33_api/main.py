import requests
from datetime import *
from smtplib import *

my_mail = 'savidhya646@gmail.com'
pw = "mtam rzpg shcj xkia"
LAT = 12.971599 #my lat
LNG = 77.594566  #my lng
def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    # if response.status_code == 404 :
    #     raise Exception("not found")
    # instead of the above one request as a build-in method (raise_for_status())
    response.raise_for_status()
    data = response.json()

    iss_lat  = float(data['iss_position']['lattitude'])
    iss_lng = float(data['iss_position']['longitude'])

    if LAT-5 <= iss_lat <= LAT+5 and LNG-5 <= iss_lng <= LNG+5:
        return True
    
def is_night_time():    
    parameters = {
        'lat':LAT,
        'lng' : LNG,
        'formatted': 0,
    }
    response = requests.get('http://api.sunrise-sunset.org/json',params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise =int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])


    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    
    while True:
        time.sleep(60)
        if is_iss_overhead() and is_night_time:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_mail,password = pw)
            connection.sendmail(from_addr=my_mail,to_addr = my_mail,msg ="subject: Lookup!!\n\n The ISS is above u in the sky")
