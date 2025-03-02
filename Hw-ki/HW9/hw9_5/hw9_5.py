"""5. В текстовый файл построчно записаны фамилия и имя
учащихся класса и оценка за контрольную. Вывести на экран
всех учащихся, чья оценка меньше трёх баллов."""



with open("students.txt", "r", encoding='utf-8') as file:

    data = file.readlines()

    for line in data:
        # Разделяем строчку на фамилию, имя и оценку
        surname, name, grade = line.strip().split()

        grade = int(grade)

        if grade < 3:
            print(surname, name)