--1. Представим, что у нас есть таблица "Employees" с полями "Name", "Position", "Department", "Salary".
--● 1Создайте таблицу "Employees" с указанными полями.
CREATE TABLE Employees (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(50),
    position    VARCHAR(30),
    department  VARCHAR(30),
    salary      DECIMAL(10,2)
);

--● 2Вставьте в таблицу несколько записей с информацией о сотрудниках вашей компании.
INSERT INTO employees (name, position, department, salary)
VALUES 
('Иван Иванов', 'Manager', 'Sales', 5000),
('Мария Петрова', 'Разработчик', 'IT', 6000),
('Алексей Смирнов', 'Аналитик', 'Маркетинг', 5500),
('Ольга Кузнецова', 'Дизайнер', 'Дизайн', 5800),
('Сергей Васильев', 'Тестировщик', 'IT', 4200),
('Елена Попова', 'HR-менеджер', 'Кадры', 3300),
('Дмитрий Сидоров', 'Системный администратор', 'IT', 4200),
('Анна Михайлова', 'Бухгалтер', 'Финансы', 4700),
('Павел Федоров', 'Продакт-менеджер', 'Sales', 6500),
('Татьяна Николаева', 'Manager', 'Sales', 5400);

--● 3Измените данные в таблице для каких-то сотрудников.
--Например, изменим должность одного из сотрудников на более высокую.
UPDATE employees 
SET position = 'Fullstack-разработчик', 
salary = 8000 
WHERE name = 'Мария Петрова';

--● 4Добавьте новое поле "HireDate" (дата приема на работу) в таблицу "Employees".
ALTER TABLE employees ADD COLUMN hire_date DATE;

--● 5Добавьте записи о дате приема на работу для всех сотрудников.
UPDATE employees SET hire_date = '2025-03-16';
UPDATE employees SET hire_date = '2025-01-28' WHERE department IN ('Sales', 'IT', 'Кадры');

--● 6Найдите всех сотрудников, чья должность "Manager".
SELECT name FROM employees WHERE position = 'Manager';

--● 7Найдите всех сотрудников, у которых зарплата больше 5000 долларов.
SELECT * FROM employees WHERE salary > 5000;

--● 8Найдите всех сотрудников, которые работают в отделе "Sales".
SELECT name FROM employees WHERE department = 'Sales';

--● 9Найдите среднюю зарплату по всем сотрудникам.
SELECT AVG(salary) AS avg_salary FROM employees;

--● 10Удалите таблицу "Employees".
DROP TABLE employees;


-- через хранимые функции:

--● 6Найдите всех сотрудников, чья должность "Manager".
CREATE OR REPLACE FUNCTION get_position(x_position VARCHAR) 
RETURNS TABLE (get_name VARCHAR) AS $$
BEGIN
    RETURN QUERY  -- из-за отсутствия этой строки долгое время не получалось вывести результат
    SELECT name FROM employees WHERE position ILIKE x_position;
END;
$$ 
LANGUAGE plpgsql;
--DROP ROUTINE get_position(VARCHAR);  -- любимый запрос ;)
SELECT * FROM get_position('Manager'); 


--● 7Найдите всех сотрудников, у которых зарплата больше 5000 долларов.
CREATE OR REPLACE FUNCTION get_salary(DECIMAL) 
RETURNS TABLE (get_name VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT name FROM employees WHERE salary > $1;
END;
$$ 
LANGUAGE plpgsql;
SELECT * FROM get_salary(5000); 


--● 8Найдите всех сотрудников, которые работают в отделе "Sales".
CREATE OR REPLACE FUNCTION get_department(VARCHAR) 
RETURNS TABLE (get_name VARCHAR) AS $$
BEGIN
    RETURN QUERY  
    SELECT name FROM employees WHERE department = $1;
END;
$$ 
LANGUAGE plpgsql;
SELECT * FROM get_department('Sales');


--● 9Найдите среднюю зарплату по всем сотрудникам.
CREATE FUNCTION get_average_salary()
RETURNS NUMERIC AS $$
DECLARE avg_salary NUMERIC;
BEGIN 
    SELECT AVG(salary) INTO avg_salary FROM employees;
    RETURN avg_salary;
END;
$$ LANGUAGE plpgsql;
SELECT get_average_salary() AS avg_salary;