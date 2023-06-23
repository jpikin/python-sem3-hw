# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.


list_1 = [1, 2, 3, 4, 5]
k = 6

# 1 Вариант
closest_num = min(list_1, key=lambda x: abs(x - k))
print(closest_num)


# 2 Вариант
temp = abs(list_1[0]-k)
closest_num2 = 0

for i in list_1:
    if abs(i - k) < temp:
        closest_num2 = i
        temp = abs(i - k)

print(closest_num2)
