N = input("Введите количество IP адресов: ")
if not N.isdigit():
    print("Ошибка")
    exit()
n = int(N)

print("\nВведите IP-адреса:")
ip_adresses = []
for i in range(n):
    ip = input()
    ip_adresses.append(ip)

def ip_to_decimal(ip):
    parts = ip.split('.')
    decimal = 0
    for i in range(4):
        decimal += int(parts[i]) * (256 ** (3 - i))
    return decimal

ip_adresses.sort(key=ip_to_decimal)
print("\nОтсортированные IP-адреса:")
for ip in ip_adresses:
    print(ip)
