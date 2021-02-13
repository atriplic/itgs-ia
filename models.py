from app import db1

class Event1(db1.Model):
    id = db1.Column(db1.Integer, primary_key=True)
    event_name = db1.Column(db1.String(255), nullable=False)
    event_date = db1.Column(db1.String(255), nullable=False)

    def __repr__(self):
        return f'{self.event_name}'
