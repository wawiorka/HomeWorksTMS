INSERT INTO events (title, date)
VALUES
('CodeFest: Хакатон для начинающих', '2025-04-16'),
('DevTalks: Встречи с профессионалами IT', '2025-04-18'),
('Algorhythm: Конкурс алгоритмических решений', '2025-05-16');


INSERT INTO plaсes (name)
VALUES
('Малый зал кинотеатра'),
('Концертный зал'),
('Конференц-холл главной арены');

INSERT INTO events_plaсes (event_id, plaсe_id)
                VALUES
                (1, 3),
                (2, 1),
                (3, 2);


DROP TABLE events;
DROP TABLE plaсes;
DROP TABLE events_plaсes;
DROP TABLE  tickets;

DELETE FROM events WHERE id = 5;