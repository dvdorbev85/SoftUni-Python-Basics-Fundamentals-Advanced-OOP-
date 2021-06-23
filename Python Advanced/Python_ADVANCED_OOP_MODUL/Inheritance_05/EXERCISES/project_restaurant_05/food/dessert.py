from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_restaurant_05.food import Food


class Dessert(Food):
    def __init__(self, name, price, grams, calories: float):
        super().__init__(name, price, grams)
        self.__calories = calories


    @property
    def calories(self):
        return self.__calories