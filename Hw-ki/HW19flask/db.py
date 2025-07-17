import psycopg2

DB_CONFIG = {
    "dbname": "ticket_server",
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
                date VARCHAR(15),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP,
                deleted_at TIMESTAMP DEFAULT NULL
            );
        """)

        cur.execute("""
            CREATE TABLE  IF NOT EXISTS plases (
                id SERIAL PRIMARY KEY, 
                name VARCHAR(100) UNIQUE
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
                event_id INT REFERENCES events (id) ON DELETE CASCADE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                deleted_at TIMESTAMP DEFAULT NULL
            );
        """)


def get_events():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, title, date, created_at FROM events WHERE deleted_at IS NULL;")
        events_db = cur.fetchall()
        events = list()
        for event in events_db:
            events.append({
                "id": event[0],
                "title": event[1],
                "date": event[2],
                "created_at": event[3],
            })
        return events
    

def get_plases():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM plases")
        plases_db = cur.fetchall()
        plases = list()
        for plase in plases_db:
            plases.append({
                "id": plase[0],
                "name": plase[1],
            })
        return plases
    

def add_event(title, date):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO events (title, date) VALUES (%s, %s)", (title, date,))


def add_in_events_plases(title):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id FROM events WHERE title ILIKE %s;", [(title,)])
        new_id = cur.fetchall()
        cur.execute("INSERT INTO events_plases (event_id) VALUES (%s)", (new_id[0],))


def reserv_ticket(buyer, event_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO tickets (buyer, event_id) VALUES (%s, %s)", (buyer, event_id,))


def return_ticket(id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE tickets SET deleted_at = CURRENT_TIMESTAMP WHERE id = %s;", (id,))


def update_event(date, id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE events SET updated_at = CURRENT_TIMESTAMP, date = (%s) WHERE id = %s AND deleted_at IS NULL", (date, id, ))


def hard_delete_event(id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM events WHERE id = %s", (id,))


def delete_event(id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE events SET deleted_at = CURRENT_TIMESTAMP WHERE id = %s;", (id,))

def get_plases_events():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""SELECT p.name, p.id, e.title, e.date
                        FROM events_plases AS e_p
                        JOIN plases AS p ON p.id = e_p.plase_id
                        JOIN events AS e ON e.id = e_p.event_id;""")
        pl_ev = cur.fetchall()
        plases_ev = {}
        n = 1
        for p_e in pl_ev:
            plases_ev[n] =  {
                    "name": p_e[0],
                    "id": p_e[1],
                   "title": p_e[2],
                   "date": p_e[3],
            }
            n += 1
        return plases_ev
    

def search_events(query):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM events WHERE title ILIKE %s;", (f"%{query}%",))
        events = cur.fetchall()
        return events
    

    