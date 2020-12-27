import sys
class Critter(object):
    def __str__(self):
        rep="Объект класса Critter\n"
        rep+= "имя: " + self.name + "\n"
        rep+= "настроение: " + self.mood + "\n"
        rep+= "голод:" + str(self.hunger) + "\n"
        rep+= "показатель скуки:" + str(self.boredom) + "\n"
        rep+= "показатель силы:" + str(self.force) + "\n"
        rep+= "показатель здоровья:" + str(self.health) + "\n"
        return rep
        
    def __init__(self, name, hunger=0, boredom = 0,force = 0, health = 20):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.force = force
        self.health = health

    def __pass_time(self):
        self.hunger +=1
        self.boredom += 1
        self.health -= 1
        self.force -= 1

    def talk(self):
        print('Привет! Меня зовут ', self.name, " . Сейчас я чувствую себя ", self.mood, "\n")
        self.__pass_time()

    def eat(self, food = 4):
        food=int(input("Сколько еды ты хочешь мне дать? (дай 4 пожалуйста)"))
        print("Спасибо!")
        self.hunger-=food
        if self.hunger<0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        fun=int(input("Сколько времени ты хочешь со мной поиграть?"))
        print("ОМАГАД!!1!")
        self.force+=fun
        self.boredom-=fun
        self.hunger+=1
        if self.boredom<0:
            self.boredom = 0
        self.__pass_time()
    def train(self):
        health=int(input("Сколько времени ты хочешь со мной тренироваться? "))
        print("Побежали!!")
        self.health+=health
        self.force+=health
        self.__pass_time()
    def nakaz(self):
        print("Зачем?...((")
        self.health-=10
        self.force-=5
        self.hunger+=4
        self.boredom+=4
        self.__pass_time()
        if self.force<0:
            self.force=0
        if self.health <= 0:
            del (self)
            print("Вы отправили животное на тот свет((")
            sys.exit()
    def care(self):
        print("Какую таблетку ты мне хочешь дать?")
        choice=int(input("""
        1 - Супердорогую
        2 - Хорошую
        3 - Обычную
        """))
        if choice == "1":
            self.health+=100
            self.force+=30
            print("Спасибо большое!!")
        elif choice == "2":
            self.health+=50
            self.force+=15
            print("Спасибо!")
        elif choice == "3":
            self.health+=20
            self.force+=6
            print("Спасибо")
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger +self.boredom-(self.health/100)
        if unhappiness <5:
            m = "прекрасно"
        elif 5<=unhappiness<=10:
            m = "норм"
        elif 10<unhappiness<=15:
            m = "пойдет"
        else:
            m = "ужасно"
        return m

def main():
    crit_name=input("Дорогая, как мы назовем зверушку, которая собирается появиться на свет? ")
    if crit_name.isdigit():
        print("Мне не нравится это имя")
    else:
        print("Мне нравится это имя!")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
        ("""
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствиии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        4 - Выйти на пробежку со зверюшкой
        5 - Наказать зверюшку
        6 - Вылечить зверюшку
        Здесь также был добавлен секретный черный ход чтобы посмотреть информацию о зверюшке
        """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        elif choice == "4":
            crit.train()
        elif choice == "5":
            crit.nakaz()
        elif choice == "6":
            crit.care()
        elif choice == "123qwe":
            print(crit)
        else:
            print("Извините, в меню игры нет такого пункта ", choice)

main()

input("\n\nНажмите Enter, чтобы выйти")
