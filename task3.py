# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.



rus_dict = {1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
            2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
            3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
            4: ['Й', 'Ы'],
            5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
            8: ['Ш', 'Э', 'Ю'],
            10: ['Ф', 'Щ', 'Ъ']}
eng_dict = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
            2: ['D', 'G'],
            3: ['B', 'C', 'M', 'P'],
            4: ['F', 'H', 'V', 'W', 'Y'],
            5: ['K'],
            8: ['J', 'X'],
            10: ['Q', 'Z']}

k = input().upper()

def score_counter(lang_dict, word):
    total_score = 0
    for i in range(len(word)):
        for key, item in lang_dict.items():
            if word[i] in item:
                total_score += key
    return total_score

if ord(k[0]) > 122:
    print(score_counter(rus_dict, k))
else: print(score_counter(eng_dict, k)) 