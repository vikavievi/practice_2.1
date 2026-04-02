shop = {
    'Молочная продукция':
        {
        'Молоко':
            {
            'price': 89.78,
            'description': 'Очень вкусное',
            },
        'Сыр':
            {
            'price': 195.98,
            'description': 'С дырками',
            },
        'Масло':
            {
            'price': 100,
            'description': 'Подсолнечное',
            }
        },
    'Соки':
        {
        'J7 яблоко':
            {
            'price': 165.98,
            'description': 'Классика вкуса',
            },
        'Фрутик вишня':
            {
            'price': 99,
            'description': 'Мой любимый вкус',
            },
        },
    'Готовая еда':
        {
        'Онигири':
            {
            'price': 64.87,
            'description': 'Из спара',
            },
        'Салат “Алабама”':
            {
            'price': 119.99,
            'description': 'Американ-салат',
            },
        'Морковка по корейский':
            {
            'price': 77.87,
            'description': 'Очень острая',
            },
        }
    }
work = True
print('\nмагазин спар у техникума\n')
while work:
    print("Категории:")
    category = list(shop)

    for i in range(len(category)):
        print(f'{i + 1})', end=" ")
        print(category[i])
    print('0 - Выход')

    c = input("Выберете номер категории: ")

    match c:
        case '0':
            work = False
        case '1' | '2' | '3':
            while True:
                category_index = int(c) - 1
                selected_category = category[category_index]
                products = list(shop[selected_category])
                for i, product in enumerate(products):
                    print(f'{i + 1})', end=" ")
                    print(product)

                print('0 - Выход')

                print('Введите - для возврата назад')

                product_choice = input('Выберете действие: ')

                match product_choice:
                    case '0':
                        work = False
                        break
                    case '1' | '2' | '3' if int(product_choice) <= len(products):
                        product_index = int(product_choice) - 1
                        selected_product = products[product_index]
                        product_info = shop[selected_category][selected_product]

                        print('\n', selected_product, sep="")
                        print('Цена:', product_info['price'])
                        print('Описание:', product_info['description'])
                        input('Для возврата к продуктам нажмите Enter')
                    case'-':
                        break

        case _:
            print('Данной категории не существует')