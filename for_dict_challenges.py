from collections import Counter
from operator import is_not
from functools import partial

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
print('\n'.join(['{}: {}'.format(name, [student['first_name'] for student in students].count(name)) for name in
                 set([student['first_name'] for student in students])]))
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

print('Самое частое имя среди учеников: {}'.format(Counter([student['first_name'] for student in students]).most_common(1)[0][0]))

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
print(
  '\n'.join(
    ['Самое частое имя в классе {}: {}'.format(index, Counter([student['first_name'] for student in students]).most_common(1)[0][0]) for index, students in enumerate(school_students)]
  )
)


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
for school_class in school:
  bool_students = [is_male[name] for name in [students['first_name'] for students in school_class['students']]]
  print('В классе {} {} девочки и {} мальчика.'.format(school_class['class'], bool_students.count(False), bool_students.count(True)))

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
girls = []
boys = []


[school_class['class'] for school_class in school]
for school_class in school:
  boys += [school_class['class'] if is_male[name] else None for name in [students['first_name'] for students in school_class['students']]]
  girls += [school_class['class'] if not is_male[name] else None for name in [students['first_name'] for students in school_class['students']]]
print('Больше всего мальчиков в классе {}'.format(Counter(filter(partial(is_not, None), boys)).most_common(1)[0][0]))
print('Больше всего девочек в классе {}'.format(Counter(filter(partial(is_not, None), girls)).most_common(1)[0][0]))

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a