# 1)  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        sec = 0
        while sec != 3:
            print(TrafficLight.__color[sec])
            if sec == 0:
                sleep(7)
            elif sec == 1:
                sleep(2)
            elif sec == 2:
                sleep(3)
            sec += 1


progr = TrafficLight()
progr.running()


# 2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass = 25
        self.thickness = 5

    def asph_weight(self):
        asph_weight = self._length * self._width * self.mass * self.thickness / 1000
        print(f'Потребуется {asph_weight} тонн асфальта.')


my_Road = Road(length=float(input('Введите длинну дороги: ')), width=float(input('Введите ширину дороги: ')))
my_Road.asph_weight()


# 3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


b = Position(name='Vlad', surname='Maksimov', position='Lifeguard', wage=100, bonus=200)
print(b.get_full_name())
print(b.get_total_income())


# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'\nМашина {self.name} остановилась'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nТекущая скорость автомобиля: {self.speed} км/ч'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'\nМашина {self.name} едет с превышением скорости'
        else:
            return f'\nТекущая скорость автомобиля: {self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'\nМашина {self.name} едет с превышением скорости'
        else:
            return f'\nТекущая скорость автомобиля: {self.speed} км/ч'


class PoliceCar(Car):

    def angr(self):
        if self.is_police:
            return '\nНам все можно жи есть!'


town = TownCar(speed=60, color='черный', name='Чевролет Нива', is_police=False)
print(town.go(), town.show_speed(), town.turn('налево'), town.stop())

sport = SportCar(speed=100, color='красный', name='Лада Гранта', is_police=False)
print('\n' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar(speed=150, color='коричневый', name='Газель Некст', is_police=False)
print('\n' + work.go(), work.show_speed(), work.turn('направо'), work.turn('налево'), work.stop())

police = PoliceCar(speed=300, color='Белый', name='Меркедец Белибабен', is_police=True)
print('\n' + police.go(), police.show_speed(), police.turn('в занос'), police.angr(), police.stop())


# 5) Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное
# сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):

    def draw(self):
        return f'Отрисовка {self.tittle} ручкой.'


class Pencil(Stationery):

    def draw(self):
        return f'Отрисовка {self.tittle} карандашом.'


class Handle(Stationery):

    def draw(self):
        return f'Отрисовка {self.tittle} маркером.'


a = Stationery('')
b = Pen('рожицы')
c = Pencil('пейзажа')
d = Handle('натюрморта')

print(a.draw())
print(b.draw())
print(c.draw())
print(d.draw())
