"""3. Напишите программу, которая считывает текст из
файла (в файле может быть больше одной строки) и выводит
в новый файл самое часто встречаемое слово в каждой
строке и число – счётчик количества повторений этого слова
в строке."""

file = 'hw9_3.txt'

with open(file, encoding='utf-8') as list1:
    for line in list1:
        line = line.lower()
        dict_temp = {}
        for word in line.split():
            if word not in dict_temp:
                dict_temp[word] = 1
            elif word in dict_temp:
                dict_temp[word] += 1

        max_quantity = 1

        for key, value in dict_temp.items():
            quantity = dict_temp[key]
            if quantity > max_quantity:
                max_quantity = quantity
                word_with_max_quantity = key

        with open('res_hw9_3.txt', 'a', encoding='utf-8') as modify_file:
            most_popular = (word_with_max_quantity + " " + str(max_quantity) + "\n")
            modify_file.write(most_popular)


