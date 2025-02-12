import json

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} Грн."

    def to_dict(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def from_dict(data):
        return Dish(data["name"], data["price"])

class RestaurantMenu:
    def __init__(self, filename="menu.json"):
        self.menu = []
        self.filename = filename
        self.load_menu()

    def add_dish(self):
        name = input("Назва страви: ")
        price = float(input("Ціна страви: "))
        dish = Dish(name, price)
        self.menu.append(dish)
        print(f"Страва '{name}' тепер в меню.")
        self.save_menu()

    def remove_dish(self):
        if not self.menu:
            print("Меню порожнє.")
            return
        self.show_menu()
        try:
            dish_index = int(input("Введіть номер страви для видалення: ")) - 1
            if 0 <= dish_index < len(self.menu):
                removed_dish = self.menu.pop(dish_index)
                print(f"Страва '{removed_dish.name}' видалена з меню.")
                self.save_menu()
            else:
                print("Невірний номер страви.")
        except ValueError:
            print("Введіть правильний номер.")

    def show_menu(self):
        if not self.menu:
            print("Меню порожнє.")
            return
        print("\nМеню ресторану:")
        for idx, dish in enumerate(self.menu, start=1):
            print(f"{idx}. {dish}")

    def calculate_total(self):
        total = 0
        while True:
            self.show_menu()
            try:
                dish_index = int(input("Виберіть страву за номером, або введіть 0 для завершення: ")) - 1
                if dish_index == -1:
                    break
                if 0 <= dish_index < len(self.menu):
                    total += self.menu[dish_index].price
                    print(f"Ви вибрали {self.menu[dish_index].name}. Поточна сума: {total} грн.")
                else:
                    print("Невірний номер страви.")
            except ValueError:
                print("Введіть правильний номер.")
        print(f"\nЗагальна сума вашого замовлення: {total} грн.")

    def save_menu(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([dish.to_dict() for dish in self.menu], f, ensure_ascii=False, indent=4)

    def load_menu(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.menu = [Dish.from_dict(dish) for dish in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.menu = []

def main():
    restaurant = RestaurantMenu()

    while True:
        print("\nОберіть дію:")
        print("1. Додати страву до меню")
        print("2. Видалити страву з меню")
        print("3. Переглянути меню")
        print("4. Оформити замовлення")
        print("5. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            restaurant.add_dish()
        elif choice == '2':
            restaurant.remove_dish()
        elif choice == '3':
            restaurant.show_menu()
        elif choice == '4':
            restaurant.calculate_total()
        elif choice == '5':
            print("До побачення")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
