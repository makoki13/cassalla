import cls_jugador


class Marcador:
    piedras_por_cama: int
    numero_camas: int
    num_jugadores: int
    num_piedras_para_ganar: int
    jugadores = []
    mano_actual = []

    @staticmethod
    def inicializa(num_jugadores: int, piedras_por_cama: int, numero_camas: int):
        Marcador.num_jugadores = num_jugadores
        Marcador.piedras_por_cama = piedras_por_cama
        Marcador.numero_camas = numero_camas
        Marcador.num_piedras_para_ganar = Marcador.piedras_por_cama * Marcador.numero_camas

    # devuelve True si la partida esta completa.
    @staticmethod
    def add_jugador(jugador: cls_jugador.Jugador):
        Marcador.jugadores.append(jugador)
        if (len(Marcador.jugadores) == Marcador.num_jugadores):
            return True
        return False

    @staticmethod
    def get_lista_jugadores():
        return Marcador.jugadores

    @staticmethod
    def add_mano(indice: int):
        Marcador.mano_actual.append(indice)

    @staticmethod
    def add_puntos(jugador: cls_jugador.Jugador, puntos: int):
        for item_jugador in Marcador.jugadores:
            if (item_jugador.get_ordinal() == jugador.get_ordinal()):
                jugador.add_puntos(puntos)
                num_piedras = jugador.get_puntos()
                if (num_piedras > Marcador.num_piedras_para_ganar):
                    jugador.set_puntos(Marcador.num_piedras_para_ganar)

    def get_ganador():
        for item_jugador in Marcador.jugadores:
            num_piedras = item_jugador.get_puntos()
            if (num_piedras >= Marcador.num_piedras_para_ganar):
                return item_jugador
        return None
