import cls_jugador


class Marcador:
    piedras_por_cama: int
    numero_camas: int
    num_jugadores: int
    jugadores = []

    @staticmethod
    def inicializa(num_jugadores: int, piedras_por_cama: int, numero_camas: int):
        Marcador.num_jugadores = num_jugadores
        Marcador.piedras_por_cama = piedras_por_cama
        Marcador.numero_camas = numero_camas

    @staticmethod
    def add_jugador(jugador: cls_jugador.Jugador):
        Marcador.jugadores.append(jugador)

    def es_ganador(indice_jugador: int):
        num_piedras = Marcador.jugadores(indice_jugador).get_puntos()
        if (num_piedras >= Marcador.piedras_por_cama * Marcador.numero_camas):
            return True
        return False
