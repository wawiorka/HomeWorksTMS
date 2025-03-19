-- Задача 1: Создание и заполнение таблиц
-- ● Создайте таблицу authors с полями id, first_name и last_name. Используйте PRIMARY KEY для поля id
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);


-- ● Создайте таблицу books с полями id, title, author_id и publication_year. Используйте PRIMARY KEY для поля id и
-- FOREIGN KEY для поля author_id, ссылаясь на таблицу authors
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(30), 
    author_id INT REFERENCES authors(id),
    publication_year INT
);


-- ● Создайте таблицу sales с полями id, book_id и quantity.
-- Используйте PRIMARY KEY для поля id и FOREIGN KEY для поля book_id, ссылаясь на таблицу books
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    book_id INT,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books(id)
);


-- ● Добавьте несколько авторов в таблицу authors
INSERT INTO authors (first_name, last_name)
VALUES 
('Uladzimier', 'Karatkievic'),
('Janka', 'Maur'),
('Sviatlana', 'Aleksijevic'),
('Jakub', 'Kolas'),
('Ivan', 'Mielez'),
('Alaiza', 'Pashkievic'),
('Vincent', 'Dunin-Marcinkievic');


--DROP TABLE authors;
--DROP TABLE books;
--DROP TABLE sales;


-- ● Добавьте несколько книг в таблицу books, указывая авторов из таблицы authors
INSERT INTO books (title, author_id, publication_year)
VALUES
('Belarusian violin', 6, 1906),
('A New Land', 4, 1923),
('Simon the Musician', 4, 1925),
('Polesia Robinsons', 2, 1929),
('Little Traveller_s Book', NULL, 1522),
('Ksty', NULL, 2006),
('TVT', 2, 1949),
('Pan Tadeusz', NULL, 1834),
('King Stakh_s Wild Hunt', 1, 1964),
('The Black Castle Alshanski', 1, 1980);

-- ● Добавьте записи о продажах книг в таблицу sales
INSERT INTO sales (book_id, quantity)
VALUES
(1, 23),
(2, 57),
(4, 80),
(5, 33),
(6, 54),
(8, 158),
(9, 251),
(10, 200);


-- Задача 2: Использование JOIN
-- ● Используйте INNER JOIN для получения списка всех книг и их авторов.
SELECT books.title, authors.first_name, authors.last_name
FROM books
JOIN authors ON authors.id = books.author_id;


-- ● Используйте LEFT JOIN для получения списка всех авторов и их книг (включая авторов, у которых нет книг).
SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON authors.id = books.author_id;


-- ● Используйте RIGHT JOIN для получения списка всех книг и их авторов, включая книги, у которых автор не указан
SELECT books.title, authors.first_name, authors.last_name
FROM authors
RIGHT JOIN books ON authors.id = books.author_id;


-- Задача 3: Множественные JOIN
-- ● Используйте INNER JOIN для связывания таблиц authors, books и sales, 
-- чтобы получить список всех книг, их авторов и продаж
SELECT b.title, a.first_name, a.last_name, s.quantity
FROM books AS b
JOIN authors AS a
ON a.id = b.author_id
JOIN sales AS s
ON b.id = s.book_id;


-- ● Используйте LEFT JOIN для связывания таблиц authors, books и sales, чтобы получить 
-- список всех авторов, их книг и продаж (включая авторов без книг и книги без продаж)
SELECT a.first_name, a.last_name, b.title, s.quantity
FROM authors AS a
LEFT JOIN books AS b
ON a.id = b.author_id
LEFT JOIN sales AS s
ON b.id = s.book_id;


-- Задача 4: Агрегация данных с использованием JOIN
--● Используйте INNER JOIN и функции агрегации для определения общего количества проданных книг каждого автора
SELECT a.first_name, a.last_name, SUM(s.quantity) AS sum_quantity
FROM authors AS a
JOIN books AS b
ON a.id = b.author_id
JOIN sales AS s
ON b.id = s.book_id
GROUP BY a.first_name, a.last_name;


--● Используйте LEFT JOIN и функции агрегации для 
--определения общего количества проданных книг каждого автора, включая авторов без продаж
SELECT a.first_name, a.last_name, SUM(s.quantity) AS sum_quantity
FROM authors AS a
LEFT JOIN books AS b
ON a.id = b.author_id
LEFT JOIN sales AS s
ON b.id = s.book_id
GROUP BY a.first_name, a.last_name;


--Задача 5: Подзапросы и JOIN
--● Найдите автора с наибольшим количеством проданных книг, используя подзапросы и JOIN
SELECT MAX(sum_quantity)
FROM (SELECT a.first_name, a.last_name, SUM(s.quantity) AS sum_quantity
FROM authors AS a
LEFT JOIN books AS b
ON a.id = b.author_id
LEFT JOIN sales AS s
ON b.id = s.book_id
GROUP BY a.first_name, a.last_name);


SELECT authors.first_name, authors.last_name, SUM(sales.quantity) FROM authors, books, sales
WHERE authors.id = books.author_id AND books.id = sales.book_id
GROUP BY authors.first_name, authors.last_name;

--● Найдите книги, которые были проданы в количестве, превышающем среднее количество продаж всех книг,
--используя подзапросы и JOIN