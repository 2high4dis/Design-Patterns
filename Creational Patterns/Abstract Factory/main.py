from abc import ABC, abstractmethod
from typing import Tuple


class Furniture():
    def hasLegs(self) -> bool:
        return True


class Chair(ABC, Furniture):

    @abstractmethod
    def sit(self) -> str:
        return f'You are sitting on {self.__class__.__name__}'


class Sofa(ABC, Furniture):
    @abstractmethod
    def sit(self) -> str:
        return f'You are sitting on {self.__class__.__name__}'


class Table(ABC, Furniture):
    @abstractmethod
    def sit(self) -> str:
        return f'You are sitting on {self.__class__.__name__}'


class DecoChair(Chair):
    def sit(self) -> str:
        return super().sit()


class ModernChair(Chair):
    def sit(self) -> str:
        return super().sit()


class VictorianChair(Chair):
    def sit(self) -> str:
        return super().sit()


class DecoSofa(Sofa):
    def sit(self) -> str:
        return super().sit()


class ModernSofa(Sofa):
    def sit(self) -> str:
        return super().sit()


class VictorianSofa(Sofa):
    def sit(self) -> str:
        return super().sit()


class DecoTable(Table):
    def sit(self) -> str:
        return super().sit()


class ModernTable(Table):
    def sit(self) -> str:
        return super().sit()


class VictorianTable(Table):
    def sit(self) -> str:
        return super().sit()


class Factory(ABC):
    @abstractmethod
    def createChair(self) -> Chair:
        ...

    @abstractmethod
    def createSofa(self) -> Sofa:
        ...

    @abstractmethod
    def createTable(self) -> Table:
        ...

    @abstractmethod
    def createSet(self) -> Tuple[Chair, Sofa, Table]:
        return self.createChair(), self.createSofa(), self.createTable()


class DecoFactory(Factory):
    def createChair(self) -> Chair:
        return DecoChair()

    def createSofa(self) -> Sofa:
        return DecoSofa()

    def createTable(self) -> Table:
        return DecoTable()

    def createSet(self) -> Tuple[Chair, Sofa, Table]:
        return super().createSet()


class ModernFactory(Factory):
    def createChair(self) -> Chair:
        return ModernChair()

    def createSofa(self) -> Sofa:
        return ModernSofa()

    def createTable(self) -> Table:
        return ModernTable()

    def createSet(self) -> Tuple[Chair, Sofa, Table]:
        return super().createSet()


class VictorianFactory(Factory):
    def createChair(self) -> Chair:
        return VictorianChair()

    def createSofa(self) -> Sofa:
        return VictorianSofa()

    def createTable(self) -> Table:
        return VictorianTable()

    def createSet(self) -> Tuple[Chair, Sofa, Table]:
        return super().createSet()


if __name__ == '__main__':
    factories = [DecoFactory(), ModernFactory(), VictorianFactory()]

    for factory in factories:
        print(f'{factory.__class__.__name__}:')
        for item in factory.createSet():
            print(item.sit())
        print('------------------------------')
