from abc import ABC, abstractmethod


class Abstract_estrategia(ABC):

    @abstractmethod
    def nombre():
        pass

    @abstractmethod
    def analiza_envido(self, envido_actual):
        pass
