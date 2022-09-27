def viny_song(song):
    vowels = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
    lst = [len(list(filter(lambda x: x in vowels, i))) for i in song.split()]
    return ('Пам парам', 'Парам пам-пам')[len(set(lst)) == 1]



# text = input().split()
# set_1 = set()
# for i in text:
#     count = 0
#     for j in i:
#         if j.lower() in 'еёоуяаюэи':
#             count += 1
#     set_1.add(count)
# if len(set_1) == 1:
#     print('yes')
# else:
#     print('no')
