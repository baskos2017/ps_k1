from pyjokes import get_joke
import emoji
import art
from time import sleep
from tqdm import tqdm
from colorama import init, Fore, Back, Style
from prettytable import PrettyTable
from termcolor import colored
import random




"""Функція send_emojis виводить графінчно описані текстово emojis. Функція
my_art_tqdm виводить англійський алфавіт з допомогою модуля art заданим в 
цюому модулі шрифтом paranormal показуючи прогресбар в кожному рядку 
виводу з допомогою модуля tqdm. Функція send_joke з допомогою модулів
pyjokes та colorama виводить вбудовані жарти модуля pyjokes розфарбовучи 
текст та фон  з допомогою модуля colorama. Функція game гра 
камінь-ножиці-папір. Функція game_init користувацький інтерфейс цієї гри.
Функція my_table виводить з допомогою модуля prettytable фільми переможці
цього річного оскара назву студій які зняли ці фільми та імена їх 
продюсерів(вікіпедія) розфарбовуючи вивід з допомогою модуля termcolor в 
заданий колір. Щоб отримати красивий вивід в цій функції не вдалося
дотриматись РЕР8."""




def send_emojis():
    emoji_list = [':grinning_face_with_big_eyes:', ':thumbs_up:', ':fire:',\
                  ':pile_of_poo:', ':rocket:']
    emojis = ' '.join(emoji_list)
    print(emoji.emojize(emojis))

def my_art_tqdm():
    text = ""
    for char in tqdm(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',\
                      'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
                      'w', 'x', 'y', 'z'], ncols=80):
        sleep(0.25)
        text = text + char
        tqdm.write(art.text2art(text, font = 'paranormal'))

def send_joke():
    joke = get_joke()
    print(Fore.YELLOW + Back.RED + joke + Style.RESET_ALL)

def game(choice):
    choices = ['k', 'n', 'p']
    computer_choice = random.choice(choices)

    print("Ваш вибір:", choice)
    print("Вибір комп'ютера:", computer_choice)

    if choice == computer_choice:
        return "Нічия!"
    elif (choice == 'k' and choice == 'n') or \
         (choice == 'n' and choice == 'p') or \
         (choice == 'p' and choice == 'k'):
        return "Ви перемогли!"
    else:
        return "Комп'ютер переміг!"

def game_init():
    while True:
        my_input = input("Введіть ваш вибір (k, n або p)," \
                            "або 'stop', щоб завершити гру: ").lower()
        
        if my_input == 'stop':
            print("Гра завершена.")
            break
        
        if my_input not in ['k', 'n', 'p']:
            print("Неправильний ввід! Спробуйте ще раз.")
            continue

        result = game(my_input)
        print(result)

def my_table():
    mytable = PrettyTable()
    mytable.add_column('Фильм',['Оппенгеймер', 'Американское чтиво',
                                'Анатомия падения', 'Барби',\
                                'Оставленные', 'Убийцы цветочной луны',\
                                'Маэстро', 'Прошлые жизни', \
                                'Бедные-несчастные', 'Зона интересов'])
    mytable.add_column('Кинокомпания(и)', ['Universal Pictures',\
                                           'Orion Pictures, Amazon MGM Studios',\
                                            'Le Pacte, Neon', 'Warner Bros',\
                                            'Miramax, Focus Features',\
                                            'Apple TV+, Paramount Pictures',\
                                            'Netflix', 'A24', \
                                            'Searchlight Pictures', 'A24'])
    mytable.add_column('Продюсер(ы)', ['Эмма Томас, Чарльз Ровен и Кристофер Нолан', 'Бен Леклер, Никос Карамигиос, Корд Джефферсон и Джермейн Джонсон', 'Мари-Анж Люсьяни и Давид Тион', 'Дэвид Хейман, Марго Робби, Том Акерли и Робби Бреннер', 'Марк Джонсон', 'Дэн Фридкин, Брэдли Томас, Мартин Скорсезе и Дэниел Лупи', 'Брэдли Купер, Стивен Спилберг, Фред Бернер, Эми Дернинг и Кристи Макоско Кригер', 'Дэвид Инохоса, Кристин Вашон и Памела Коффлер', 'Эд Гини, Эндрю Лоу, Йоргос Лантимос и Эмма Стоун', 'Джеймс Уилсон'])

    return(colored(mytable, "cyan"))

while True:
    select = input('1 - Цікавий шрифт\n2 - Отримати смайли\n3 - Анекдот?\n'\
                   '4 - Рекомендовані фільми\n5 - Гра\n6 Вихід\n')
    if select == '1':
        print('Цікавий шрифт')
        my_art_tqdm()
    elif select == "2":
        send_emojis()
    elif select =="3":
        send_joke()
    elif select == "4":
        print(my_table())
    elif select == '5':
        game_init()
    elif select == '6':
        break
