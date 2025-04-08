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
    places = relationship("EventPlace", back_populates="event", cascade="all, delete") 
    tickets = relationship("Ticket", back_populates="event", cascade="all, delete")


class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    events = relationship("EventPlace", back_populates="place", cascade="all, delete")


class EventPlace(Base):
    __tablename__ = "events_places"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"))
    place_id = Column(Integer, ForeignKey("places.id", ondelete="CASCADE"))
    event = relationship("Event", back_populates="places")
    place = relationship("Place", back_populates="events")


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    buyer = Column(String(20), nullable=True)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"))
    bought_at = Column(DateTime, default=func.now())
    returned_at = Column(DateTime, default=None)
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


def get_places():
    with SessionLocal() as session:
        places_db = session.query(Place).all()
        places = list()
        for place in places_db:
            places.append({
                "id": place .id,
                "name": place.name,
            })
        return places
    

# def get_places_events():
#     with SessionLocal() as session:
#         places_ev_db = session.query(EventPlace.id, Place.name, Place.id, Event.title, Event.date)\
#                 .join(Place, Place.id == EventPlace.place_id) \
#                     .join(Event, Event.id == EventPlace.event_id).all()
#         places_ev = list()
#         for pl_ev in places_ev_db:
#             places_ev.append({
#                 "id": pl_ev.id,
#                 "name": pl_ev.name,
#                 "place_id": pl_ev.id,
#                 "title": pl_ev.title,
#                 "date": pl_ev.date,
#             })
#         return places_ev


def add_event(title, date):
    with SessionLocal() as session:
        event = Event(title = title, date = date)
        session.add(event)
        session.commit()

        
def add_in_events_places(title):
    with SessionLocal() as session:
        new_id = session.query(Event.id).filter(Event.title == title).first()
        new_ev_pl = EventPlace(event_id = new_id[0], place_id = None)
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
        del_ticket.returned_at = func.now()
        session.add(del_ticket)
        session.commit()  
        

def get_tickets():
    with SessionLocal() as session:
        tickets_info_db = session.query(Ticket.id, Ticket.buyer, Event.title, Event.date) \
            .join(Event, Event.id == Ticket.event_id).filter(Ticket.returned_at == None).all()
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


def add_place(name):
    with SessionLocal() as session:
        place = Place(name = name)
        session.add(place)
        session.commit()


def update_place(place_id, event_id):
    with SessionLocal() as session:
        update = session.query(EventPlace).filter(EventPlace.event_id == event_id).first()
        update.place_id = place_id
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
    