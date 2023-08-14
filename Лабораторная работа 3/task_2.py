# TODO Напишите функцию find_common_participa
def find_common_participants(stroka_1,stroka_2,razdelitel="|"):

   familii_1 = stroka_1.split(razdelitel)
   familii_2 = stroka_2.split(razdelitel)
   res = set(familii_1).intersection(familii_2)
   return res
   #common = {x for x in familii_1 if x in familii_2}
    #return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group,participants_second_group,razdelitel="|")
print(sorted(result))

