# TODO  Напишите функцию count_letters
def count_letters(stix):
    nijniy_registr = stix.lower()
    kolichestvo_bukv = {}
    for character in nijniy_registr:
        if character.isalpha():
            if character in kolichestvo_bukv:
                kolichestvo_bukv[character] += 1
            else:
                kolichestvo_bukv[character] = 1
    return kolichestvo_bukv
# TODO Напишите функцию calculate_frequency

def calculate_frequency(kolichestvo_bukv):
    vsego_simvolov = sum(kolichestvo_bukv.values())
    chastota_simvolov ={}
    for tekushiy_simvol, bukva in kolichestvo_bukv.items():
        chastota_simvolov[tekushiy_simvol] = bukva / vsego_simvolov
    return chastota_simvolov

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
tekushiy_slovar = count_letters(main_str)
chastota_bukv = calculate_frequency(tekushiy_slovar)

for simvoli, chastota in chastota_bukv.items():
    print(f"{simvoli}: {chastota:.2f}")