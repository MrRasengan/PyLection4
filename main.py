                        #Lambda Функции
# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))


# math(lambda a,b: a + b, 5, 45)


# 1. В списке хранятся числа. 
# Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

#sp = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in sp:
#     if i % 2 == 0:
#         res.append((i, i **2))

# print(res)

# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# sp = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, sp)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

                           #Функции MAP

# list_1 = [x for x in range(1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. 
# Как превратить list строк в list чисел?

# data = '15 21 34 56  1 456 2 3 88'
# print(data)
# # data = data.split()
# # print(data)
# data = list(map(int, data.split()))
# print(data)


                            #Функия Fitr

# data = [15, 85, 23, 96, 8 ,23, 3]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res) 

                           # Функция zip

# Пример:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

                            # Функция enumerate

# Функция enumerate() позволяет пронумеровать набор данных.
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
#print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

                               # Работа с файлами

#  colors = ['red', 'green', 'blue']
#  data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
#  data.writelines(colors) # разделителей не будет
#  data.close()
# ● data.close() — используется для закрытия файла, чтобы разорвать подключение файловой
# переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление в
# существующий файл, а не перезапись файлов.

# Ещё один способ записи данных в файл:
# with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')

# 2. Режим r
# ● Чтение данных из файла:
#  path = 'file.txt'
#  data = open(path, 'r')
#  for line in data:
#  print(line)
#  data.close()


# 3. Режим w
#  colors = ['red', 'green', 'blue']
#  data = open('file.txt', 'w')
#  data.writelines(colors) # разделителей не будет
# data.close()
# ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
# ● В случае перезаписи новые данные записываются, а старые удаляются
