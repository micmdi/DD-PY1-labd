list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]


new_list = len(list_players) // 2

first_team = list_players[:new_list]
second_team = list_players[new_list:]

print(first_team)
print(second_team)
