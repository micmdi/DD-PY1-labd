# TODO Напишите функцию find_common_participants
def find_common_participants(list_1, list_2, delimeter = ','):
    list_1 = list_1.split(delimeter)
    list_2 = list_2.split(delimeter)
    common_participants = list(set(list_1).intersection(list_2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, delimeter = '|')
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
