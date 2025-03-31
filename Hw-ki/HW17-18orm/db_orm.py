from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


DATABASE_URL = "postgresql://postgres:3618ann@127.0.0.1:5432/orm_ticket_serv_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True)
    date = Column(String(10), nullable=False)
    plases = relationship("EventPlase", back_populates="event", cascade="all, delete") 
    tickets = relationship("Ticket", back_populates="event", cascade="all, delete")


class Plase(Base):
    __tablename__ = "plases"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    events = relationship("EventPlase", back_populates="plase", cascade="all, delete")
    # tickets = relationship("Ticket", back_populates="plase", cascade="all, delete")


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
    # plase_id = Column(Integer, ForeignKey("plases.id", ondelete="CASCADE"))
    event = relationship("Event", back_populates="tickets")
    # plase = relationship("Plase", back_populates="tickets")


def init_db():
    Base.metadata.create_all(engine)



def get_events():
    with SessionLocal() as session:
        return session.query(Event).all()

def get_plases():
    with SessionLocal() as session:
        return session.query(Plase).all()
    

def get_plases_events():
    with SessionLocal() as session:
        plases_ev = session.query(EventPlase.id, Plase.name, Plase.id, Event.title, Event.date)\
                .join(Plase, Plase.id == EventPlase.plase_id) \
                    .join(Event, Event.id == EventPlase.event_id).all()
        return plases_ev


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
        session.delete(del_event)
        session.commit()


def update_event(title, date, id):
    with SessionLocal() as session:
        update_event = session.query(Event).filter(Event.id == id).first()
        update_event.title = title
        update_event.date = date
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
        session.delete(del_ticket)
        session.commit()        
        

def get_tickets():
    with SessionLocal() as session:
        tickets_info = session.query(Ticket.id, Ticket.buyer, Event.title, Event.date) \
            .join(Event, Event.id == Ticket.event_id).all()
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


def delete_plase(id):
    with SessionLocal() as session:
        del_plase = session.query(Plase).filter(Plase.id == id).first()
        session.delete(del_plase)
        session.commit()


def update_plase(plase_id, event_id):
    with SessionLocal() as session:
        update = session.query(EventPlase).filter(EventPlase.event_id == event_id).first()
        update.plase_id = plase_id
        session.commit()

def search_events(query):
    with SessionLocal() as session:
        events = session.query(Event).filter(Event.title.ilike(f"%{query}%")).all()
        return events
    
def search_plases(query):
    with SessionLocal() as session:
        plases = session.query(Plase).filter(Plase.name.ilike(f"%{query}%")).all()
        return plases
    

def search_events_all(query):
    with SessionLocal() as session:
        events = session.query(Event).filter(Event.title.ilike(query)).all()
        return events
    
def search_plases_all(query):
    with SessionLocal() as session:
        plases = session.query(Plase).filter(Plase.name.ilike(query)).all()
        return plases