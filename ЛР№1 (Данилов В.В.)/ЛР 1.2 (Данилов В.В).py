# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
number_of_lines = 50
number_of_characters = 25
weight_of_one_character = 4
disk_size = 1.44
#Вес книги
weight = pages * number_of_lines * number_of_characters * weight_of_one_character
quantity = disk_size * 1024 * 1024 / weight
print("Количество книг, помещающихся на дискету:", round(quantity, ))
