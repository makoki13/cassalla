from enum import Enum


class Estados(Enum):
    EN_MANO = 1
    EN_TABLERO = 2
    USADA = 3

    def test():
        for estado in Estados:
            print(estado)
