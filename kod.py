import collections

filename = 'path/to/your/file.txt'
total_count = 0
frequency = collections.defaultdict(int)

# Открываем файл для чтения
with open(filename, 'r', encoding='utf-8') as file:
    # Проходим по каждой строке в файле
    for line in file:
        # Увеличиваем общий счетчик
        total_count += len(line)
        # Обновляем мапу частоты встречаемости символов
        for char in line:
            frequency[char] += 1

# Проходим по каждой записи в мапе и рассчитываем процент встречаемости
for char, count in frequency.items():
    frequency[char] = (count / total_count) * 100

# Сортируем мапу по значениям в убывающем порядке
frequency = {char: freq for char, freq in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}

# Выводим результат
for char, freq in frequency.items():
    print(f"{char} — {freq:.2f}%")