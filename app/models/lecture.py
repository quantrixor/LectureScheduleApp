
from app import db


class Lecture(db.Model):
    __tablename__ = 'lecture'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    lecturer_name = db.Column(db.String)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    room = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'lecturer_name': self.lecturer_name,
            'start_time': self.start_time.strftime('%H:%M'),  # assuming start_time is a time object
            'end_time': self.end_time.strftime('%H:%M'),  # assuming end_time is a time object
            'room': self.room
        }





