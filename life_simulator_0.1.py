import random
import time

player = {
    "здоровье": 100,
    "энергия": 100,
    "счастье": 50,
    "деньги": 50,
    "жильё": "Общага"
}

housing_upgrades = ["Общага", "Однушка", "Квартира", "Дом", "Коттедж", "Особняк"]
housing_costs = [0, 200, 1000, 5000, 15000, 50000]

def clear():
    print("\n" + "=" * 40 + "\n")

def show_stats():
    clear()
    print("Твои статы, бля:")
    for k, v in player.items():
        print(f"{k}: {v}")
    print()

def sleep():
    print("Ты поспал как убитый...")
    player["энергия"] = min(player["энергия"] + 50, 100)
    player["здоровье"] = min(player["здоровье"] + 20, 100)
    player["счастье"] += 5

def work():
    if player["энергия"] < 20:
        print("Ты слишком заебан, иди поспать.")
        return
    job_list = [
        ("Сбор макулатуры", 10),
        ("Разносчик еды", 25),
        ("Курьер WB", 50),
        ("Продавец в DNS", 100),
        ("Фриланс-программист", 200),
        ("IT-инженер", 500)
    ]
    job = random.choice(job_list)
    print(f"Ты поработал: {job[0]} и заработал {job[1]}₽")
    player["деньги"] += job[1]
    player["энергия"] -= 30
    player["здоровье"] -= 5
    player["счастье"] -= 5

def park():
    print("Ты пошёл в парк, подышал воздухом...")
    player["счастье"] += 10
    player["энергия"] -= 10

def market():
    print("На рынке:")
    print("1. Купи шаву (+10 счастья, -20₽)")
    print("2. Купи энергетик (+30 энергии, -30₽)")
    print("3. Ничего не покупать")
    choice = input("Выбор: ")
    if choice == "1" and player["деньги"] >= 20:
        player["счастье"] += 10
        player["деньги"] -= 20
    elif choice == "2" and player["деньги"] >= 30:
        player["энергия"] += 30
        player["деньги"] -= 30
    else:
        print("Ни денег, ни выбора... Классика.")

def upgrade_house():
    current = housing_upgrades.index(player["жильё"])
    if current + 1 >= len(housing_upgrades):
        print("Ты уже в особняке, крут ты ебать.")
        return
    cost = housing_costs[current + 1]
    next_house = housing_upgrades[current + 1]
    print(f"Хочешь переехать в '{next_house}' за {cost}₽?")
    choice = input("1 - Да, 2 - Нет: ")
    if choice == "1" and player["деньги"] >= cost:
        player["деньги"] -= cost
        player["жильё"] = next_house
        player["счастье"] += 20
        print(f"Теперь ты живёшь в {next_house}!")
    else:
        print("Недостаточно бабла или желания. Ну и ладно.")

def main_loop():
    day = 1
    while True:
        show_stats()
        print(f"День {day}. Выбери действие:")
        print("1. Поспать")
        print("2. Работа")
        print("3. Парк")
        print("4. Рынок")
        print("5. Улучшить жильё")
        print("6. Выйти нахуй")

        choice = input(">>> ")
        if choice == "1":
            sleep()
        elif choice == "2":
            work()
        elif choice == "3":
            park()
        elif choice == "4":
            market()
        elif choice == "5":
            upgrade_house()
        elif choice == "6":
            print("Ты вышел... из жизни? Не, просто из игры.")
            break
        else:
            print("Ты чё ввёл, шизоид? Повтори.")
        day += 1
        time.sleep(1)

main_loop()
