INSERT INTO events (title, date)
VALUES
('CodeFest: Хакатон для начинающих', '2025-04-16'),
('DevTalks: Встречи с профессионалами IT', '2025-04-18'),
('Algorhythm: Конкурс алгоритмических решений', '2025-05-16');


INSERT INTO plases (name)
VALUES
('Малый зал кинотеатра'),
('Концертный зал'),
('Конференц-холл главной арены');

INSERT INTO events_plases (event_id, plase_id)
                VALUES
                (1, 3),
                (2, 1),
                (3, 2);


DROP TABLE events;
DROP TABLE plases;
DROP TABLE events_plases;
DROP TABLE  tickets;

DELETE FROM events WHERE id = 5;