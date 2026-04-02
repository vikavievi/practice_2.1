import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import urllib.request
import urllib.error
import json
import psutil
import requests
import sys

# 1 код
def zadanie_1(text_widget):
    urls = [
        "https://github.com/",
        "https://www.binance.com/en",
        "https://tomtit.tomsk.ru/",
        "https://jsonplaceholder.typicode.com/",
        "https://moodle.tomtit-tomsk.ru/"
    ]

    text_widget.delete(1.0, tk.END)

    for url in urls:
        try:
            response = urllib.request.urlopen(url, timeout=10)

            status_code = response.getcode()

            if status_code == 200:
                status = "доступен"
            elif status_code == 404:
                status = "не найден"
            elif status_code == 403:
                status = "вход запрещен"
            else:
                status = "доступен"

            text_widget.insert(tk.END, f"{url} – {status} – {status_code}\n")

        except urllib.error.HTTPError as e:
            status_code = e.code

            if status_code == 404:
                status = "не найден"
            elif status_code == 403:
                status = "вход запрещен"
            elif 500 <= status_code < 600:
                status = "не доступен"
            else:
                status = "не доступен"

            text_widget.insert(tk.END, f"{url} – {status} – {status_code}\n")

        except urllib.error.URLError:
            text_widget.insert(tk.END, f"{url} – не доступен – ошибка подключения\n")

        except Exception:
            text_widget.insert(tk.END, f"{url} – не доступен – неизвестная ошибка\n")


# 2 код
def show_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Загрузка CPU: {cpu_percent}%")

    memory = psutil.virtual_memory()
    print(f"Использовано RAM: {memory.used / (1024 ** 3):.1f} ГБ из {memory.total / (1024 ** 3):.1f} ГБ")
    print(f"Загрузка RAM: {memory.percent}%")

    disk = psutil.disk_usage('/')
    print(f"Загрузка диска: {disk.percent}%")
    print(f"Свободно на диске: {disk.free / (1024 ** 3):.1f} ГБ из {disk.total / (1024 ** 3):.1f} ГБ")


def system_monitor_loop(text_widget, root):
    import io
    import sys

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    show_system_info()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    text_widget.insert(tk.END, output)
    text_widget.see(tk.END)

    root.after(10000, lambda: system_monitor_loop(text_widget, root))


# 3 код
URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def load_rates():
    try:
        with urllib.request.urlopen(URL) as response:
            data = json.loads(response.read())
            return data["Valute"]
    except:
        print("Ошибка загрузки курсов! Проверьте интернет.")
        return None


def show_all_currencies(rates):
    if not rates:
        return
    print("\nВСЕ ВАЛЮТЫ")
    for code, info in rates.items():
        print(f"{code}: {info['Name']} - {info['Value']} RUB")


def show_currency_by_code(rates, code):
    if not rates:
        return
    code = code.upper()
    if code in rates:
        info = rates[code]
        print(f"\n{code}: {info['Name']} - {info['Value']} RUB")
    else:
        print(f"Валюта с кодом {code} не найдена!")


def load_groups():
    try:
        with open("save.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}


def save_groups(groups):
    with open("save.json", "w", encoding="utf-8") as file:
        json.dump(groups, file, ensure_ascii=False, indent=2)


def show_all_groups(groups):
    if not groups:
        print("\nНет созданных групп!")
        return
    print("\nВСЕ ГРУППЫ")
    for group_name, currencies in groups.items():
        print(f"\nГруппа '{group_name}':")
        if currencies:
            for code in currencies:
                print(f"  - {code}")
        else:
            print("  (пусто)")


def show_group(groups, rates, group_name):
    if group_name not in groups:
        print(f"Группа '{group_name}' не найдена!")
        return

    currencies = groups[group_name]
    if not currencies:
        print(f"Группа '{group_name}' пуста!")
        return

    print(f"\nКУРСЫ В ГРУППЕ '{group_name}'")
    for code in currencies:
        if code in rates:
            info = rates[code]
            print(f"{code}: {info['Name']} - {info['Value']} RUB")
        else:
            print(f"{code}: (не найден в текущих курсах)")


def create_group(groups):
    name = input("Введите имя новой группы: ")
    if name in groups:
        print("Группа с таким именем уже существует!")
        return
    groups[name] = []
    save_groups(groups)
    print(f"Группа '{name}' создана!")


def add_currency_to_group(groups, rates):
    if not groups:
        print("Сначала создайте хотя бы одну группу!")
        return

    print("Доступные группы:", ", ".join(groups.keys()))
    group_name = input("Введите имя группы: ")

    if group_name not in groups:
        print("Группа не найдена!")
        return

    code = input("Введите код валюты (например, USD, EUR): ").upper()
    if code not in rates:
        print("Валюта с таким кодом не найдена!")
        return

    if code in groups[group_name]:
        print("Такая валюта уже есть в группе!")
        return

    groups[group_name].append(code)
    save_groups(groups)
    print(f"Валюта {code} добавлена в группу '{group_name}'!")


def remove_currency_from_group(groups):
    if not groups:
        print("Нет созданных групп!")
        return

    print("Доступные группы:", ", ".join(groups.keys()))
    group_name = input("Введите имя группы: ")

    if group_name not in groups:
        print("Группа не найдена!")
        return

    if not groups[group_name]:
        print("В этой группе нет валют!")
        return

    print(f"Валюты в группе '{group_name}':", ", ".join(groups[group_name]))
    code = input("Введите код валюты для удаления: ").upper()

    if code in groups[group_name]:
        groups[group_name].remove(code)
        save_groups(groups)
        print(f"Валюта {code} удалена из группы '{group_name}'!")
    else:
        print("Такой валюты нет в этой группе!")


# 4 код
BASE_URL = "https://api.github.com"


def get_user_profile(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ: {username}")
        print(f"Имя: {data.get('name', 'Не указано')}")
        print(f"Ссылка на профиль: {data['html_url']}")
        print(f"Количество репозиториев: {data['public_repos']}")
        print(f"Количество обсуждений: {data.get('public_gists', 0)}")
        print(f"Количество подписок: {data['following']}")
        print(f"Количество подписчиков: {data['followers']}")

    else:
        print(f"Ошибка! Пользователь '{username}' не найден")


def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        print(f" РЕПОЗИТОРИИ ПОЛЬЗОВАТЕЛЯ: {username}")

        if not repos:
            print("Нет репозиториев")
            return

        for i, repo in enumerate(repos, 1):
            print(f"\n{i}. {repo['name']}")
            print(f"Ссылка: {repo['html_url']}")
            print(f"Язык: {repo.get('language', 'Не указан')}")
            print(f"Видимость: {'Публичный' if not repo['private'] else 'Приватный'}")
            print(f"Ветка по умолчанию: {repo['default_branch']}")
            print(f"   Количество просмотров: Требует авторизации")
    else:
        print(f" Не удалось получить репозитории пользователя '{username}'")


def search_repos_by_name(search_query):
    url = f"{BASE_URL}/search/repositories"
    params = {"q": search_query, "sort": "stars", "order": "desc"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f" РЕЗУЛЬТАТЫ ПОИСКА: '{search_query}'")

        if data['total_count'] == 0:
            print("Ничего не найдено")
            return

        print(f"Найдено: {data['total_count']} репозиториев\n")

        for i, repo in enumerate(data['items'][:10], 1):
            print(f"{i}. {repo['name']}")
            print(f"   Владелец: {repo['owner']['login']}")
            print(f"   Ссылка: {repo['html_url']}")
            print(f"   Язык: {repo.get('language', 'Не указан')}")
            print(f"   Звёзд: {repo['stargazers_count']}")

    else:
        print(" Ошибка при поиске")


# интерфейс
class ConsoleRedirect:

    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)

    def flush(self):
        pass


# гл окно
root = tk.Tk()
root.title("Многофункциональное приложение")
root.geometry("900x700")

# вкладки
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# вкладка 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Проверка URL")

btn_check = ttk.Button(tab1, text="Проверить URL", command=lambda: zadanie_1(text_urls))
btn_check.pack(pady=10)

text_urls = scrolledtext.ScrolledText(tab1, height=20, width=80)
text_urls.pack(pady=10, padx=10)

# вкладка 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Системный монитор")

btn_start_monitor = ttk.Button(tab2, text="Запустить мониторинг",
                               command=lambda: system_monitor_loop(text_monitor, root))
btn_start_monitor.pack(pady=10)

text_monitor = scrolledtext.ScrolledText(tab2, height=20, width=80)
text_monitor.pack(pady=10, padx=10)

# вкладка 3
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Курсы валют")

text_currency = scrolledtext.ScrolledText(tab3, height=15, width=80)
text_currency.pack(pady=10, padx=10)

old_stdout = sys.stdout
sys.stdout = ConsoleRedirect(text_currency)


# функции кнопок
def run_load_rates():
    rates = load_rates()
    if rates:
        show_all_currencies(rates)


def run_show_currency():
    code = currency_code_entry.get()
    rates = load_rates()
    show_currency_by_code(rates, code)


def run_create_group():
    groups = load_groups()
    old_stdout_print = sys.stdout
    sys.stdout = old_stdout
    create_group(groups)
    sys.stdout = ConsoleRedirect(text_currency)
    save_groups(groups)


def run_add_currency():
    groups = load_groups()
    rates = load_rates()
    old_stdout_print = sys.stdout
    sys.stdout = old_stdout
    add_currency_to_group(groups, rates)
    sys.stdout = ConsoleRedirect(text_currency)
    save_groups(groups)


def run_remove_currency():
    groups = load_groups()
    old_stdout_print = sys.stdout
    sys.stdout = old_stdout
    remove_currency_from_group(groups)
    sys.stdout = ConsoleRedirect(text_currency)
    save_groups(groups)


def run_show_all_groups():
    groups = load_groups()
    show_all_groups(groups)


def run_show_group():
    groups = load_groups()
    rates = load_rates()
    group_name = group_name_entry.get()
    show_group(groups, rates, group_name)

btn_frame = ttk.Frame(tab3)
btn_frame.pack(pady=5)

ttk.Button(btn_frame, text="Загрузить и показать все валюты", command=run_load_rates).pack(side=tk.LEFT, padx=5)

search_frame = ttk.Frame(tab3)
search_frame.pack(pady=5)
ttk.Label(search_frame, text="Код валюты:").pack(side=tk.LEFT)
currency_code_entry = ttk.Entry(search_frame, width=10)
currency_code_entry.pack(side=tk.LEFT, padx=5)
ttk.Button(search_frame, text="Показать валюту", command=run_show_currency).pack(side=tk.LEFT)

group_frame = ttk.Frame(tab3)
group_frame.pack(pady=5)
ttk.Label(group_frame, text="Название группы:").pack(side=tk.LEFT)
group_name_entry = ttk.Entry(group_frame, width=20)
group_name_entry.pack(side=tk.LEFT, padx=5)
ttk.Button(group_frame, text="Создать группу", command=run_create_group).pack(side=tk.LEFT)

ttk.Button(tab3, text="Показать все группы", command=run_show_all_groups).pack(pady=5)

show_group_frame = ttk.Frame(tab3)
show_group_frame.pack(pady=5)
ttk.Label(show_group_frame, text="Имя группы:").pack(side=tk.LEFT)
show_group_entry = ttk.Entry(show_group_frame, width=20)
show_group_entry.pack(side=tk.LEFT, padx=5)
ttk.Button(show_group_frame, text="Показать группу",
           command=lambda: show_group(load_groups(), load_rates(), show_group_entry.get())).pack(side=tk.LEFT)

add_frame = ttk.Frame(tab3)
add_frame.pack(pady=5)
ttk.Button(add_frame, text="Добавить валюту в группу", command=run_add_currency).pack(side=tk.LEFT, padx=5)

remove_frame = ttk.Frame(tab3)
remove_frame.pack(pady=5)
ttk.Button(remove_frame, text="Удалить валюту из группы", command=run_remove_currency).pack(side=tk.LEFT, padx=5)

# вкладка 4
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="GitHub API")

text_github = scrolledtext.ScrolledText(tab4, height=15, width=80)
text_github.pack(pady=10, padx=10)

def run_get_user_profile():
    username = github_username_entry.get()
    old_stdout_print = sys.stdout
    sys.stdout = ConsoleRedirect(text_github)
    get_user_profile(username)
    sys.stdout = old_stdout_print


def run_get_user_repos():
    username = github_username_entry.get()
    old_stdout_print = sys.stdout
    sys.stdout = ConsoleRedirect(text_github)
    get_user_repos(username)
    sys.stdout = old_stdout_print


def run_search_repos():
    query = github_search_entry.get()
    old_stdout_print = sys.stdout
    sys.stdout = ConsoleRedirect(text_github)
    search_repos_by_name(query)
    sys.stdout = old_stdout_print

github_frame = ttk.Frame(tab4)
github_frame.pack(pady=5)

ttk.Label(github_frame, text="Имя пользователя:").pack(side=tk.LEFT)
github_username_entry = ttk.Entry(github_frame, width=20)
github_username_entry.pack(side=tk.LEFT, padx=5)
ttk.Button(github_frame, text="Показать профиль", command=run_get_user_profile).pack(side=tk.LEFT, padx=5)
ttk.Button(github_frame, text="Показать репозитории", command=run_get_user_repos).pack(side=tk.LEFT, padx=5)

search_github_frame = ttk.Frame(tab4)
search_github_frame.pack(pady=5)

ttk.Label(search_github_frame, text="Поиск репозиториев:").pack(side=tk.LEFT)
github_search_entry = ttk.Entry(search_github_frame, width=30)
github_search_entry.pack(side=tk.LEFT, padx=5)
ttk.Button(search_github_frame, text="Искать", command=run_search_repos).pack(side=tk.LEFT, padx=5)


sys.stdout = old_stdout

root.mainloop()