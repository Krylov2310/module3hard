thanks='Благодарю за внимание :-)'
def visitka(task,task2, avtor):
    print(task)
    print(task2)
    print(avtor)
    print()


visitka('Дополнительное практическое задание по модулю 3',
        'Задание "Раз, два, три, четыре, пять .... Это не всё?":','Студент Крылов Эдуард Васильевич')
# Исходный код:
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print('Заданный код:', data_structure)


def calculate_structure_sum(data_structure):
    enumeration = 0
    if isinstance(data_structure, str):
        enumeration += len(data_structure)
    elif isinstance(data_structure, (float, int)):
        enumeration += data_structure
    elif isinstance(data_structure, (set, list, tuple)):
        for i in data_structure:
            enumeration += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            enumeration += calculate_structure_sum(key)
            enumeration += calculate_structure_sum(value)
    return enumeration



result = calculate_structure_sum(data_structure)
print('Сумма всех значений:', result)
print()
print(thanks)