# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.


list_1 = [1, 2, 3, 4, 5]
k = 6
closest_num = min(list_1, key=lambda x: abs(x - k))
print(closest_num)