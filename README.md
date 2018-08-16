# ifconfig-flask
It is created in order to receive information from the ifconfig by api flask.
Python version - 2.7
## Installation
Create virtualenv with python 2.7
Install from requirements `pip install -r requirements.txt`
Execute app.py by command via virtualenv `python app.py`
### URL's
```/``` - get full info about all interfaces in system
```/interfaces/``` - get all interfaces in system
``` /interfaces/<name>/ ``` - get info about variable interface, if this interface not in system, return error
``` /interfaces/<name>/packets ``` - get rx and tx packets from this interface.