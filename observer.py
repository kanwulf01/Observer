from abc import ABCMeta, abstractmethod


class Observable(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """Se subscribe """
       

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """Se desubscribo"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """Se notifico"""

class Subject(Observable):

    def __init__(self):

        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)
    
    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.notify(self, *args, **kwargs)


class Observer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def notify(observable  , *args, **kwargs):
        """Recibe notificaciones"""

class Observerx(Observer):
    def __init__(self, observable, nombre):
        self.nombre = nombre
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("Observer", self.nombre, "Entregado", args, kwargs)


SUBJECT = Subject()

OBSERVERA = Observerx(SUBJECT,"A")
OBSERVERB = Observerx(SUBJECT,"B")

SUBJECT.notify("HELLO WORLD")