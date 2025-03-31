# Разработка схемы базы данных для мероприятий, мест и билетов

import psycopg2

DB_CONFIG = {
    "dbname": "ticket_serv_db",
    "user": "postgres",
    "password": "3618ann",
    "host": "127.0.0.1",
    "port": "5432"
}


def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE  IF NOT EXISTS events (
                id SERIAL PRIMARY KEY, 
                title VARCHAR(100) UNIQUE,
                date VARCHAR(15)
            );
        """)

        cur.execute("""
            CREATE TABLE  IF NOT EXISTS plases (
                id SERIAL PRIMARY KEY, 
                name VARCHAR(100) UNIQUE,
                nums_tickets INT
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS events_plases (
                id SERIAL PRIMARY KEY,
                event_id INT REFERENCES events (id) ON DELETE CASCADE,
                plase_id INT REFERENCES plases (id) ON DELETE CASCADE
            );
        """)

        cur.execute("""
            CREATE TABLE  IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY,
                buyer VARCHAR(20),
                event_id INT REFERENCES events (id) ON DELETE CASCADE
            );
        """)
    

def content_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO events (title, date)
                VALUES 
                ('CodeFest: Хакатон для начинающих', '2025-04-16'),
                ('DevTalks: Встречи с профессионалами IT', '2025-04-18'),
                ('Algorhythm: Конкурс алгоритмических решений', '2025-05-16'),
                ('TechLab: Мастер-классы по новым технологиям', '2025-07-16'),
                ('Hack & Learn: Обучающие сессии по программированию', '2025-06-06'),
                ('Open Source Jam: Создание проектов с нуля', '2025-07-08'),
                ('Debugging Day: Поиск и исправление ошибок в коде', '2025-08-10'),
                ('Game Dev Challenge: Создание игр за 48 часов', '2025-05-26'),
                ('AI Bootcamp: Погружение в искусственный интеллект', '2025-05-30'),
                ('Code Review Night: Обсуждение и анализ кода', '2025-06-17');
        """)

        cur.execute("""
            INSERT INTO plases (name, nums_tickets)
                VALUES 
                ('Малый зал кинотеатра', 100),
                ('Концертный зал', 150),
                ('Конференц-холл главной арены', 50),
                ('Актовый зал университета', 50),
                ('Главная библиотека', 30)
        """)

        cur.execute("""
            INSERT INTO events_plases (event_id,plase_id)
                VALUES
                (1, 4),
                (2, 2),
                (3, 5),
                (4, 3),
                (5, 1),
                (6, 3),
                (7, 5),
                (8, 1),
                (9, 4),
                (10, 4);
        """)

def get_events():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM events")
        events = cur.fetchall()
        return events
    
def get_plases():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM plases")
        plases = cur.fetchall()
        return plases


def get_plases_events():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""SELECT p.name, p.id, e.title, e.date
                        FROM events_plases AS e_p
                        JOIN plases AS p ON p.id = e_p.plase_id
                        JOIN events AS e ON e.id = e_p.event_id;""")
        plases_ev = cur.fetchall()
        return plases_ev
    

def add_event(title, date):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO events (title, date) VALUES (%s, %s)", (title, date,))


def add_in_events_plases(title):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id FROM events WHERE title ILIKE %s;", [(title,)])
        new_id = cur.fetchall()
        cur.execute("INSERT INTO events_plases (event_id) VALUES (%s)", (new_id[0],))


def add_plase(name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO plases (name) VALUES (%s)", (name,))


def delete_event(id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.executemany("DELETE FROM events WHERE id = %s", [(id,)])


def delete_plase(id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.executemany("DELETE FROM plases WHERE id = %s", [(id,)])



def update_event(title, date, id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE events SET title = (%s), date = (%s) WHERE id = %s", (title, date, id, ))

def update_plase(plase_id, ivent_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE events_plases SET plase_id = %s WHERE event_id = %s", (plase_id, ivent_id, ))


def reserv_ticket(buyer, ivent_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO tickets (buyer, event_id) VALUES (%s, %s)", (buyer, ivent_id,))
        # t_n = cur.execute("SELECT COUNT(buyer) AS t_n FROM tickets WHERE event_id = %s", (ivent_id, ))
        # print(type(t_n))
        # print(f"Количество проданных билетов - {int(t_n)}")


def return_ticket(id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.executemany("DELETE FROM tickets WHERE id = %s", [(id,)])


def search_events(query):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM events WHERE title ILIKE %s;", (f"%{query}%",))
        events = cur.fetchall()
        return events
    

def search_plases(query):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM plases WHERE name ILIKE %s;", (f"%{query}%",))
        plases = cur.fetchall()
        return plases
    

def get_num_tickets(id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT COUNT(id) FROM tickets WHERE event_id = %s", (id,))
        num_tickets = cur.fetchall()
        
        cur.execute("SELECT title FROM events WHERE id = %s", (id,))
        event = cur.fetchall()

        return {
            "num_tickets": num_tickets,
            "event": event
        }

def get_tickets():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""SELECT t.id, t.buyer, e.title, e.date
                        FROM tickets AS t
                        JOIN events AS e ON e.id = t.event_id;""")
        tickets_info = cur.fetchall()
        return tickets_info
    