import db
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)


@app.route('/', methods=['GET'])
def ping():                                       
    return jsonify({'message': 'Сервер Сервиса Резервирования Билетов готов к работе!'}), HTTPStatus.OK


@app.route('/events', methods=['GET'])
def get_events():
    events = db.get_events()
    return jsonify({'Events': events}), HTTPStatus.OK


@app.route('/places', methods=['GET'])
def get_plaсes():
    places = db.get_plaсes()
    return jsonify({'Places': places}), HTTPStatus.OK


# @app.route('/places_events', methods=['GET'])
# def get_places_events():
#     places_ev = db.get_places_events()
#     return jsonify({places_ev}), HTTPStatus.OK


@app.route('/events', methods=['POST'])
def add_event():
    try:
        event = request.get_json()
    except Exception as e:
        return jsonify({'error': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST
    
    if event is None:
        return jsonify({'error': 'body is required'}), HTTPStatus.BAD_REQUEST
    elif event['title'] is None or event['title'] == '':
        return jsonify({'error': 'title is required'}), HTTPStatus.BAD_REQUEST

    try:
        db.add_event(event['title'], event['date'])
        db.add_in_events_places(event['title']) 
        return jsonify({'message': 'Мероприятие добавлено, в т.ч. в events_places'}), HTTPStatus.CREATED
    except Exception as e:
        print(f"Что-то пошло не так! {e}")
                

@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    if id is None or id <= 0:
        return jsonify({'error': 'Invalid id'}), HTTPStatus.BAD_REQUEST   
     
    db.delete_event(id)
    return jsonify({'message': 'Мероприятие удалено'}), HTTPStatus.OK 


@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    if id is None or id <= 0:
        return jsonify({'error': 'Invalid id'}), HTTPStatus.BAD_REQUEST   
    
    try:
        event = request.get_json()
    except Exception as e:
        return jsonify({'error': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST

    if event is None:
        return jsonify({'error': 'body is required'}), HTTPStatus.BAD_REQUEST
    elif event['date'] is None or event['date'] == '':
        return jsonify({'error': 'date is required'}), HTTPStatus.BAD_REQUEST

    db.update_event(event['date'], id)

    return jsonify({'message': 'Дата мероприятия изменена'}), HTTPStatus.OK


@app.route('/events/search/<query>', methods=['GET'])
def search_events(query):
    events = db.search_events(query)
    if len(events) == 0:
        return jsonify({'error': 'Мероприятий не найдено'}), HTTPStatus.BAD_REQUEST   
    return jsonify(events), HTTPStatus.OK
            

@app.route('/events_places', methods=['PUT'])
def update_events_places():
    try:
        event = request.get_json()
    except Exception as e:
        return jsonify({'error': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST

    if event is None:
        return jsonify({'error': 'body is required'}), HTTPStatus.BAD_REQUEST

    db.update_place(event['place_id'], event['event_id'])

    return jsonify({'message': 'Информация о месте проведения мероприятия обновлена'}), HTTPStatus.OK

        
@app.route('/tickets', methods=['POST'])
def reserv_ticket():  
    try:
        ticket = request.get_json()
    except Exception as e:
        return jsonify({'error': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST
    
    if ticket is None:
        return jsonify({'error': 'body is required'}), HTTPStatus.BAD_REQUEST
    elif ticket['event_id'] is None or ticket['event_id'] == '':
        return jsonify({'error': 'event_id is required'}), HTTPStatus.BAD_REQUEST

    db.reserv_ticket(ticket['buyer'], ticket['event_id'])

    return jsonify({'message': 'Билет забронирован'}), HTTPStatus.CREATED


@app.route('/tickets/<int:id>', methods=['DELETE'])
def return_ticket(id):
    if id is None or id <= 0:
        return jsonify({'error': 'Invalid id'}), HTTPStatus.BAD_REQUEST   
     
    db.return_ticket(id)
    return jsonify({'message': 'Билет вернули'}), HTTPStatus.OK   
        

@app.route('/tickets', methods=['GET'])
def get_tickets():
    tickets_info = db.get_tickets()
    return jsonify({'Продано билетов': tickets_info}), HTTPStatus.OK
    

def main():
    try:
        db.init_db()
        print("DB initialized successfully")
    except Exception as e:
        print(f"Error during DB initialization: {e}")

    try:
        app.run(port=5000)
    except Exception as e:
        print(f"Error during Server initialization: {e}")


main()