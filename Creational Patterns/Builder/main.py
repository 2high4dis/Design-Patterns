from abc import ABC, abstractmethod


class Car:
    def __init__(self) -> None:
        self.parts = {}

    def add(self, part: dict) -> None:
        self.parts.update(part)

    def __str__(self) -> str:
        return '\n'.join(f'{k}: {v}' for k, v in self.parts.items())


class Builder(ABC):
    @property
    @abstractmethod
    def car(self) -> None:
        ...

    @abstractmethod
    def setSeats(self) -> None:
        ...

    @abstractmethod
    def setEngine(self) -> None:
        ...

    @abstractmethod
    def setTripComputer(self) -> None:
        ...

    @abstractmethod
    def setGPS(self) -> None:
        ...


class CarBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    @property
    def car(self) -> Car:
        car = self._car
        self.reset()
        return car

    def setSeats(self) -> None:
        self._car.add({'Seats': 4})

    def setEngine(self) -> None:
        self._car.add({'Engine': 'Cool engine'})

    def setGPS(self) -> None:
        self._car.add({'GPS': 'The latest GPS'})

    def setTripComputer(self) -> None:
        self._car.add({'Trip Computer': 'The latest trip computer'})


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def minimal_complectation(self) -> None:
        self.builder.setSeats()
        self.builder.setEngine()

    def full_complectation(self) -> None:
        self.minimal_complectation()
        self.builder.setGPS()
        self.builder.setTripComputer()


if __name__ == '__main__':
    director = Director()

    builder = CarBuilder1()
    director.builder = builder

    print('Standart basic car: ')
    director.minimal_complectation()
    print(builder.car)

    print('-'*40)

    print('Full complectation car:')
    director.full_complectation()
    print(builder.car)

    print('-'*40)

    print('Custom seatless car:')
    builder.setEngine()
    builder.setGPS()
    builder.setTripComputer()
    print(builder.car)
