# Нули (0043)
# 
# Требуется найти самую длинную непрерывную цепочку нулей в последовательности нулей и единиц.
# 
# Входные данные
# В единственной строке входного файла INPUT.TXT записана последовательность нулей и единиц (без пробелов). Суммарное количество цифр от 1 до 100.
#
# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести искомую длину цепочки нулей.
## ------------------------------------------------------------------------------------------------------------------------------
input_data = open('input.txt', 'r') # Открываем для чтения (литера 'r') файл и кладем его в переменную
data = input_data.read() # Читаем в другую переменную содержимое всего файла

# Разбиваем строку в список (list) с использованием команды сплит (по умолчанию разделитель - пробел)
zeroes_list = data.split('1')
zeroes_list_lens = []
for i in zeroes_list:
    zeroes_list_lens.append(len(i))

result = max(zeroes_list_lens)
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
# Записываем результат сложения и не забываем преобразовать его в строку (иначе будет ошибка)
output_data.write(str(result)) 
# output_data.write(str(int(data[0]) + int(data[1]))) 

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()