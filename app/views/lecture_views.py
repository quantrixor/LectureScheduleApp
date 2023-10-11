
from flask import Blueprint, request, jsonify

from app import db
from app.models.lecture import Lecture  # Ensure correct import

app = Blueprint('lectures', __name__, url_prefix='/lectures')


from datetime import datetime


@app.route('/', methods=['POST'])
def create_lecture():
    data = request.get_json()

    title = data.get('title')
    lecturer_name = data.get('lecturer_name')
    room = data.get('room')

    start_time_str = data.get('start_time')
    end_time_str = data.get('end_time')

    try:
        start_time_obj = datetime.strptime(start_time_str, '%H:%M').time()
        end_time_obj = datetime.strptime(end_time_str, '%H:%M').time()
    except ValueError as ve:
        print(str(ve))
        return jsonify({'error': 'Invalid time format'}), 400

    # Insert into DB...
    lecture = Lecture(
        title=title,
        lecturer_name=lecturer_name,
        start_time=start_time_obj,
        end_time=end_time_obj,
        room=room
    )
    db.session.add(lecture)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        # Log the error and/or return a relevant error message to the user
        print(str(e))
        return jsonify({'error': 'An error occurred, please try again later'}), 500

    return jsonify({'message': 'Lecture created successfully'}), 201

@app.route('/', methods=['GET'])
def get_lectures():
    try:
        lectures = [lecture.to_dict() for lecture in Lecture.query.all()]
    except Exception as e:
        print(str(e))
        return jsonify({'error': 'An error occurred, please try again later'}), 500

    return jsonify({'lectures': lectures}), 200

@app.route('/<int:lecture_id>/', methods=['DELETE'])
def delete_lecture(lecture_id):

    lecture = Lecture.query.get(lecture_id)
    if lecture is None:
        return jsonify({'error': 'Lecture not found'}), 404

    db.session.delete(lecture)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({'error': 'An error occurred, please try again later'}), 500

    return jsonify({'message': 'Lecture deleted successfully'}), 200