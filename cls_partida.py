
import cls_arbitro
import cls_tablero
import cls_marcador


class Partida:
    id: int
    arbitro: cls_arbitro.Arbitro
    tablero: cls_tablero.Tablero
    marcador: cls_marcador

    @staticmethod
    def inicializa(arbitro: cls_arbitro.Arbitro, tablero: cls_tablero.Tablero, marcador: cls_marcador.Marcador):
        Partida.id = 0  # provisional
        Partida.arbitro = arbitro
        Partida.tablero = tablero
        Partida.marcador = marcador

    def start():
        pass
