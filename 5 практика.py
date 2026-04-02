word = input("Введите ваш текст:").split()
count = {}
for i in word:
    if i in count:
        count[i] += 1
        else:
            count[i] = 1
        
