from abc import ABC, abstractmethod


class Transport(ABC):
    '''
    Transport Interface implements operations
    that all of its subclasses must perform
    '''
    @abstractmethod
    def deliver(self) -> str:
        return self.__class__.__name__


class Truck(Transport):
    def deliver(self) -> str:
        return f'{super().deliver()} - Deliver by road'


class Ship(Transport):
    def deliver(self) -> str:
        return f'{super().deliver()} - Deliver by sea'


class Logistic(ABC):
    '''
    Class Logistics implements a fabric method
    which returns Transport class instance.
    '''
    transports = []

    @abstractmethod
    def factory_method(self):
        pass

    def create_transport(self) -> str:
        transport = self.factory_method()
        self.transports.append(transport)

        result = f'New {transport.__class__.__name__} was created.'

        return result

    def all_transports(self) -> str:
        return '\n'.join(transport.deliver() for transport in self.transports)


class LogisticRoad(Logistic):
    def factory_method(self) -> Transport:
        return Truck()


class LogisticSea(Logistic):
    def factory_method(self) -> Transport:
        return Ship()


if __name__ == '__main__':
    logistics = [LogisticRoad(), LogisticSea()]

    for logistic in logistics:
        print(logistic.create_transport())
        print(logistic.all_transports())
        print('------------------------------')
