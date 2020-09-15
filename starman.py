#!/usr/bin/python3
"""By Russell Zachary Feeser | Alta3 Research
A simple Python flask app suitable for turning into a Docker image
"""
## requests and flask are both python library requirements
import requests
from flask import Flask

ASTRO = "http://api.open-notify.org/astros.json"

app = Flask(__name__)

def spaceman():
    r = requests.get(ASTRO)
    return r.json()
            
# if user sends HTTP GET to /astro
@app.route("/astro")
def starpeople():
    return spaceman()
    
# bind to all IP addresses port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
