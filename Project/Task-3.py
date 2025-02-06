class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} грн"

class RestaurantMenu:
    def __init__(self):
        self.menu = []

    def add_dish(self):
        name = input("Введіть назву страви: ")
        price = float(input("Введіть ціну страви: "))
        dish = Dish(name, price)
        self.menu.append(dish)
        print(f"Страва '{name}' додана до меню.")

    def show_menu(self):
        if not self.menu:
            print("Меню порожнє.")
            return
        print("\nМеню ресторану:")
        for dish in self.menu:
            print(dish)

    def calculate_total(self):
        total = 0
        while True:
            self.show_menu()
            try:
                dish_index = int(input("Виберіть страву за номером (1, 2, 3), або введіть 0 для завершення: ")) - 1
                if dish_index == -1:
                    break
                if dish_index < 0 or dish_index >= len(self.menu):
                    print("Невірний номер страви. Спробуйте ще раз.")
                    continue
                total += self.menu[dish_index].price
                print(f"Ви вибрали {self.menu[dish_index].name}. Поточна сума: {total} грн.")
            except ValueError:
                print("Будь ласка, введіть правильний номер.")
        print(f"\nЗагальна сума вашого замовлення: {total} грн.")

def main():
    restaurant = RestaurantMenu()

    while True:
        print("\nОберіть дію:")
        print("1. Додати страву до меню")
        print("2. Переглянути меню")
        print("3. Оформити замовлення")
        print("4. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            restaurant.add_dish()
        elif choice == '2':
            restaurant.show_menu()
        elif choice == '3':
            restaurant.calculate_total()
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
