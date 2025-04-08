from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, TIMESTAMP, func, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

DATABASE_URL = "postgresql://postgres:3618ann@127.0.0.1:5432/orm_ticket_server"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True)
    date = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime, default=None)
    plases = relationship("EventPlase", back_populates="event", cascade="all, delete") 
    tickets = relationship("Ticket", back_populates="event", cascade="all, delete")


class Plase(Base):
    __tablename__ = "plases"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    events = relationship("EventPlase", back_populates="plase", cascade="all, delete")


class EventPlase(Base):
    __tablename__ = "events_plases"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"))
    plase_id = Column(Integer, ForeignKey("plases.id", ondelete="CASCADE"))
    event = relationship("Event", back_populates="plases")
    plase = relationship("Plase", back_populates="events")


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    buyer = Column(String(20), nullable=True)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=func.now())
    deleted_at = Column(DateTime, default=None)
    event = relationship("Event", back_populates="tickets")


def init_db():
    Base.metadata.create_all(engine)


def get_events():
    with SessionLocal() as session:
        events_db = session.query(Event).filter(Event.deleted_at == None).all()
        events = list()
        for event in events_db:
            events.append({
                "id": event.id,
                "title": event.title,
                "date": event.date,
                "created_at": event.created_at,
            })
        return events


def get_plases():
    with SessionLocal() as session:
        plases_db = session.query(Plase).all()
        plases = list()
        for plase in plases_db:
            plases.append({
                "id": plase .id,
                "name": plase.name,
            })
        return plases
    

# def get_plases_events():
#     with SessionLocal() as session:
#         plases_ev_db = session.query(EventPlase.id, Plase.name, Plase.id, Event.title, Event.date)\
#                 .join(Plase, Plase.id == EventPlase.plase_id) \
#                     .join(Event, Event.id == EventPlase.event_id).all()
#         plases_ev = list()
#         for pl_ev in plases_ev_db:
#             plases_ev.append({
#                 "id": pl_ev.id,
#                 "name": pl_ev.name,
#                 "plase_id": pl_ev.id,
#                 "title": pl_ev.title,
#                 "date": pl_ev.date,
#             })
#         return plases_ev


def add_event(title, date):
    with SessionLocal() as session:
        event = Event(title = title, date = date)
        session.add(event)
        session.commit()

        
def add_in_events_plases(title):
    with SessionLocal() as session:
        new_id = session.query(Event.id).filter(Event.title == title).first()
        new_ev_pl = EventPlase(event_id = new_id[0], plase_id = None)
        session.add(new_ev_pl)
        session.commit()
    

def delete_event(id):
    with SessionLocal() as session:
        del_event = session.query(Event).filter(Event.id == id).first()
        del_event.deleted_at = func.now()
        session.add(del_event)
        session.commit()


def update_event(date, id):
    with SessionLocal() as session:
        update_event = session.query(Event).filter(Event.id == id).first()
        update_event.date = date
        update_event.updated_at = func.now()
        session.add(update_event)
        session.commit()

def reserv_ticket(buyer, event_id):
    with SessionLocal() as session:
        ticket = Ticket(buyer = buyer, event_id = event_id)
        session.add(ticket)
        session.commit()


def return_ticket(id):
    with SessionLocal() as session:
        del_ticket = session.query(Ticket).filter(Ticket.id == id).first()
        del_ticket.deleted_at = func.now()
        session.add(del_ticket)
        session.commit()  
        

def get_tickets():
    with SessionLocal() as session:
        tickets_info_db = session.query(Ticket.id, Ticket.buyer, Event.title, Event.date) \
            .join(Event, Event.id == Ticket.event_id).filter(Ticket.deleted_at == None).all()
        tickets_info = list()
        for ticket in tickets_info_db:
            tickets_info.append({
                "unique_id": ticket.id,
                "buyer": ticket.buyer,
                "title": ticket.title,
                "date": ticket.date,
            })
        return tickets_info
        

def get_num_tickets(id):
    with SessionLocal() as session:
        num_tickets = session.query(Ticket).filter(Ticket.event_id == id).count()
        event = session.query(Event.title).filter(Event.id == id).all()
        return {
            "num_tickets": num_tickets,
            "event": event,
        }


def add_plase(name):
    with SessionLocal() as session:
        plase = Plase(name = name)
        session.add(plase)
        session.commit()


def update_plase(plase_id, event_id):
    with SessionLocal() as session:
        update = session.query(EventPlase).filter(EventPlase.event_id == event_id).first()
        update.plase_id = plase_id
        session.commit()

def search_events(query):
    with SessionLocal() as session:
        events_db = session.query(Event).filter(Event.title.ilike(f"%{query}%")).all()
        events = list()
        for event in events_db:
            events.append({
                "id": event.id,
                "title": event.title,
            })
        return events
    