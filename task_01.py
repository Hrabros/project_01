# Есть строка с перечислением песен

my_favorite_songs = 'AWaste a Moment, Staying, Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# решение №1.
my_favorite_songs_1 = 'Waste a Moment, Staying, Alive, A Sorta Fairytale, Start Me Up, New Salvation'.split(',')
my_favorite_songs_1 = my_favorite_songs_1[0] + my_favorite_songs_1[-1]
print (my_favorite_songs_1)

# решение №2

print (my_favorite_songs[0:14]+ ' ' + my_favorite_songs[65:78])