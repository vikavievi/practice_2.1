print('начало игры')
print('1. Как дела?')
print('2. Чем ты занимаешься?')
print('3. Чем будешь заниматься на выходных?')
print('4. Спроси меня что-нибудь про спорт')
print('5. Пока')
print('Введите - для выхода из программы')
choice = input('\nВыберете что хотите спросить: ')
def talk_to_krosh():
    global work
    while True:
        match choice:
            case '1':
                print('\nКрош: Всё гуд, у тебя как зёма?')
                input('Вы: ')
                print('\n')
            case '2':
                print('\nКрош: Готовлюсь к турниру (the international)')
                input('\nНажмите enter чтобы продолжить')
            case '3':
                print('\nКрош: Пойду с пациками гонять в футбол')
                input('\nНажмите enter чтобы продолжить')
            case '4':
                answer = input('Крош: Месси или Роналду? ').lower()
                if answer == 'роналду':
                    print('\nКрош: Да я с тобой солидарен')
                    input('\nНажмите enter чтобы продолжить')
                else:
                    print('\nКрош: Ну нееееее')
                    input('\nНажмите enter чтобы продолжить')
            case '5':
                print('\nКрош: Давай откисай малышь')
                break
            case '-':
                work = False
                break


def talk_to_hedgehog():
    global work
    while True:
        print('1) Как дела?')
        print('2) Чем ты занимаешься?')
        print('3) Чем будешь заниматься на выходных?')
        print('4) Спроси меня что-нибудь о ботанике')
        print('5) Пока')
        print('Введите - для выхода из программы')

        choice = input('\nВыберете что хотите спросить: ')

        match choice:
            case '1':
                print('\nЁжик: Как сажа бела, а у тебя как?')

                input('Вы: ')

                print('\n')
            case '2':
                print('\nЁжик: Я ищу умиротворения и иду по стопам Идущего к реке')
                input('\nНажмите enter чтобы продолжить')
            case '3':
                print('\nЁжик: Я живу лишь сейчас и не могу знать что будет проходить потом')
                input('\nНажмите enter чтобы продолжить')
            case'4':
                answer = input('Ёжик: Корневая система, у которой не развит главный корень? ').lower()
                if answer == 'мочковатая':
                    print('\nЁжик: Молодец, правильно!')
                    input('\nНажмите enter чтобы продолжить')
                else:
                    print('\nЁжик: Ты ошибся')
                    input('\nНажмите enter чтобы продолжить')
            case'5':
                print('\nЁжик: Прощай путник')
                break
            case '-':
                work = False
                break


def talk_to_pin():
    global work
    while True:
        print('1) Как дела?')
        print('2) Чем ты занимаешься?')
        print('3) Чем будешь заниматься на выходных?')
        print('4) Спроси меня что-нибудь о механике')
        print('5) Пока')
        print('Введите - для выхода из программы')

        choice = input('\nВыберете что хотите спросить: ')

        match choice:
            case '1':
                print('\nПин: gut, а у тебя как?')

                input('Вы: ')

                print('\n')
            case '2':
                print('\nПин: Я собираю новый сяоми редми поко Икс 4 5джи пр макс сауд')
                input('\nНажмите enter чтобы продолжить')
            case'3':
                print('\nПин: Пойду выгуливать биби')
                input('\nНажмите enter чтобы продолжить')
            case'4':
                answer = input('Пин: Прибор, имеряющий скорость тела? ').lower()
                if answer == 'спидометр':
                    print('\nПин: Ja ja')
                    input('\nНажмите enter чтобы продолжить')
                else:
                    print('\nПин: Nein')
                    input('\nНажмите enter чтобы продолжить')
            case '5':
                    print('\nПин: Давай давай, нужно будет что то создать, ты знаешь')
                    break
            case '-':
                    work = False
                    break

        def talk_to_losash():
            global work
            while True:
                print('1) Как дела?')
                print('2) Чем ты занимаешься?')
                print('3) Чем будешь заниматься на выходных?')
                print('4) Спроси меня что-нибудь о физике')
                print('5) Пока')
                print('Введите - для выхода из программы')

                choice = input('\nВыберете что хотите спросить: ')

                match choice:
                    case '1':
                        print('\nЛосяш: Поразительно, а ты как поживаешь?')

                        input('Вы: ')

                        print('\n')
                    case '2':
                        print('\nЛосяш: Думаю на счет четвёртого закона Ньютона')
                        input('\nНажмите enter чтобы продолжить')
                    case '3':
                        print('\nЛосяш: Буду испытывать четвёртый закон НьютСовунье')
                        input('\nНажмите enter чтобы продолжить')
                    case'4':
                        answer = input('Лосяш: Самопроизвольное перемешивавеществ?').lower()
                        if answer == 'диффузия':
                            print('\nЛосяш: Молодец, мой дорогой друг')
                            input('\nНажмите enter чтобы продолжить')
                        else:
                            print('\nЛосяш: Неверно')
                            input('\nНажмите enter чтобы продолжить')
                    case'5':
                        print('\nЛосяш: До встречи мой милый друг, надеюсь мыувидимся')
                        break
                    case '-':
                        work = False
                        break

        work = True
        while work:
            print("1)Крош\n2)Ёжик\n3)Пин\n4)Лосяш")
            print('5)Выход')

            do = input('Выберите с кем зотите начать диалог: ')
            match do:
                case '1':
                    print('\nКрош: Васааааап мабой\n')
                    talk_to_krosh()
                case '2':
                    print('\nЁжик: Что же тебя привело ко мне?\n')
                    talk_to_hedgehog()
                case '3':
                    print('\nПин: Дада, подай пожалуйста ключ на 7')
                    talk_to_pin()
                case '4':
                    print('\nЛосяш: Здравствуй мой долгожданный друг')
                    talk_to_losash()
                case '5':
                    break
                case _:
                    print('Неверное действие')