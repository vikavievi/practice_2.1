n = int(input('Введите вместимость походного рюкзака кг: '))
weshi = {'двухместная палатка': 6,'надувной матрас': 4, 'фонарик': 0.5, 'зонт': 0.8, 'бутылка': 0.6, 'еда': 2,
         'теплый свитер': 2, 'перчатки': 0.2, 'спички': 0.05, 'переносной душ': 1.2, 'солнечные батареи': 3}
sort = sorted(weshi, key=weshi.get, reverse=True)
bag = []
k = 0
for i in sort:
    weight = weshi[i]
    if k + weight <= n:
        bag.append(i)
        k += weight
print(bag)
