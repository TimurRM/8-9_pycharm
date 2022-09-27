# def same_by(characteristic, object):
#     list_1 = [characteristic(el) for el in object]
#     return len(object) == list_1.count(0)
# def same_by(characteristic, object):
#     return len(object) == [characteristic(el) for el in object].count(0)
#
#
# values = [0, 2, 11, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

def viny_song(song):
    vowels = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
    lst = [len(list(filter(lambda x: x in vowels, i))) for i in song.split()]
    return ('Пам парам', 'Парам пам-пам')[len(set(lst)) == 1]
#
#
#
# def operation_table(func, row=9, columns=9):
#     for i in range(row):
#         for j in range(columns):
#             print(f'{func(i + 1, j + 1)}', end=' \t')
#         print()
#
#
# operation_table(lambda x, y: x * y, 5)


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
