from app import db1
db1.create_all()
from models import Event1
from datetime import datetime
e1 = Event1(event_name = "xyz", event_date = datetime.utcnow())