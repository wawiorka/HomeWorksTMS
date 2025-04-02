from flask import Flask, jsonify, request
from http import HTTPStatus

import db

app = Flask(__name__)


@app.route('/', methods=['GET'])
def ping():
    return jsonify({'сообщение': 'Сервер Сервиса Резервирования Билетов готов к работе!'}), HTTPStatus.OK


@app.route('/events', methods=['GET'])
def get_events():
    events = db.get_events()
    return jsonify({'Мероприятия': events}), HTTPStatus.OK


@app.route('/plases2', methods=['GET']) # ?????????????????????????????
def get_plases2():
    plases = db.get_plases2()
    return plases
    # for plase in plases:
    #     return f"ID {plase[0]} - {plase[1]}"


@app.route('/plases', methods=['GET'])
def get_plases():
    plases = db.get_plases()
    return jsonify({'Места': plases}), HTTPStatus.OK


@app.route('/events', methods=['POST'])
def add_event():
    try:
        event = request.get_json()
    except Exception as e:
        return jsonify({'Ошибка': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST
    
    if event is None:
        return jsonify({'Ошибка': 'body is required'}), HTTPStatus.BAD_REQUEST
    elif event['title'] is None or event['title'] == '':
        return jsonify({'Ошибка': 'title is required'}), HTTPStatus.BAD_REQUEST

    db.add_event(event['title'], event['date'])

    return jsonify({'Сообщение': 'Мероприятие добавлено'}), HTTPStatus.CREATED


@app.route('/tickets', methods=['POST'])
def reserv_ticket():  # reserv_ticket(buyer, event_id):
    try:
        ticket = request.get_json()
    except Exception as e:
        return jsonify({'Ошибка': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST
    
    if ticket is None:
        return jsonify({'Ошибка': 'body is required'}), HTTPStatus.BAD_REQUEST
    elif ticket['event_id'] is None or ticket['event_id'] == '':
        return jsonify({'Ошибка': 'event_id is required'}), HTTPStatus.BAD_REQUEST

    db.reserv_ticket(ticket['buyer'], ticket['event_id'])

    return jsonify({'Сообщение': 'Билет забронирован'}), HTTPStatus.CREATED


@app.route('/tickets/<int:id>', methods=['DELETE'])
def return_ticket(id):
    if id is None or id <= 0:
        return jsonify({'Ошибка': 'Invalid id'}), HTTPStatus.BAD_REQUEST   
     
    db.return_ticket(id)
    return jsonify({'Сообщение': 'Билет вернули'}), HTTPStatus.OK    


@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    if id is None or id <= 0:
        return jsonify({'Ошибка': 'Invalid id'}), HTTPStatus.BAD_REQUEST   
    
    try:
        event = request.get_json()
    except Exception as e:
        return jsonify({'Ошибка': f"error during reading request body: {e}"}), HTTPStatus.BAD_REQUEST

    if event is None:
        return jsonify({'Ошибка': 'body is required'}), HTTPStatus.BAD_REQUEST
    elif event['date'] is None or event['date'] == '':
        return jsonify({'Ошибка': 'date is required'}), HTTPStatus.BAD_REQUEST

    db.update_event(event['date'], id)

    return jsonify({'Сообщение': 'Дата мероприятия изменена'}), HTTPStatus.OK


@app.route('/events/hard/<int:id>', methods=['DELETE'])  # ?????????????????
def hard_delete_event(id):
    if id is None or id <= 0:
        return jsonify({'Ошибка': 'Invalid id'}), HTTPStatus.BAD_REQUEST   
     
    db.hard_delete_event(id)
    return jsonify({'Сообщение': 'Мероприятие удалено безвозвратно'}), HTTPStatus.OK    


@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    if id is None or id <= 0:
        return jsonify({'Ошибка': 'Invalid id'}), HTTPStatus.BAD_REQUEST   
     
    db.delete_event(id)
    return jsonify({'Сообщение': 'Мероприятие удалено'}), HTTPStatus.OK 


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
