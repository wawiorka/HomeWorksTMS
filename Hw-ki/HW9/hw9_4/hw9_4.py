"""Напишите программу, которая получает на вход строку
с названием текстового файла и выводит на экран
содержимое этого файла, заменяя все запрещённые слова
звездочками. Запрещённые слова, разделённые символом
пробела, должны храниться в файле stop_words.txt.
(Продолжение). Программа должна находить
запрещённые слова в любом месте файла, даже в середине
другого слова. Замена независима от регистра: если в списке
запрещённых есть слово exam, то замениться должны exam,
eXam, EXAm и другие вариации.
Пример: в stop_words.txt записаны слова: hello email
python the exam wor is
Текст файла для цензуры выглядит так: Hello, World! Python
IS the programming language of thE future. My EMAIL is...
PYTHON as AwESOME!
Тогда итоговый текст: *****, ***ld! ****** ** *** programming
language of *** future. My ***** **... ****** ** awesome!!!!"""


file = "hw9_4.txt"
stop_words_file = "stop_words.txt"

with open(file, "r", encoding='utf-8') as input_file:
    text = input_file.read()

with open(stop_words_file, "r", encoding='utf-8') as stop_words:
    stop_list = stop_words.read().split()

def find_indexes(line, word):
    indexes = []
    temp_line = line.lower()
    i = 0
    while i < len(temp_line):
        j = temp_line.find(word, i)
        if j == -1:
            break
        indexes.append(j)
        i = j + len(word)
    print(indexes)
    return indexes

new_text = text

for word in stop_list:
    indexes = find_indexes(new_text, word)

    for index in indexes:
        new_text = (new_text[:index] + "***" + new_text[index + len(word):])

print(stop_list)
print(new_text)
