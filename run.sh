python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
FLASK_APP=./app.py FLASK_DEBUG=1 flask run