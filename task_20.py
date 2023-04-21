# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
in_word = list(input("Напишите слово на русском или алглийском языке: ").upper())
print(in_word)

one_point = ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т',)
two_points = ('D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У',)
three_points = ('B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я',)
four_points = ('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы', )
five_points = ('K', 'Ж', 'З', 'Х', 'Ц', 'Ч', )
eight_points = ('J', 'X', 'Ш', 'Э', 'Ю', )
ten_points = ('Q', 'Z', 'Ф', 'Щ', 'Ъ', )

sum_word = 0
for i in range(len(in_word)):
    if in_word[i] in one_point:
        sum_word += 1
    elif in_word[i] in two_points:
        sum_word +=2
    elif in_word[i] in three_points:
        sum_word +=3
    elif in_word[i] in four_points:
        sum_word +=4
    elif in_word[i] in five_points:
        sum_word +=5
    elif in_word[i] in eight_points:
        sum_word +=8
    elif in_word[i] in ten_points:
        sum_word +=10
print(sum_word)