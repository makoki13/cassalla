
import cls_jugador
import cls_partida
import cls_carta
import cls_decision
import cls_baraja_safor
import cls_mano
import cls_estados_carta
import cls_carta_en_juego


class Arbitro:
    jugador_en_turno: cls_jugador.Jugador
    indice_jugador_en_turno: int
    partida: cls_partida.Partida
    baraja = cls_baraja_safor.Baraja_safor()

    @staticmethod
    def set_partida(partida: cls_partida.Partida):
        Arbitro.partida = partida

    @staticmethod
    def set_jugador_en_turno(jugador: cls_jugador.Jugador, indice: int):
        Arbitro.jugador_en_turno = jugador
        Arbitro.indice_jugador_en_turno = indice

    @staticmethod
    def get_jugador_en_turno():
        return Arbitro.jugador_en_turno

    ########### metodos operativos ####################

    # cuando estén los slots de jugadores completos se envia un mensaje al primer jugador para que actue
    @staticmethod
    def add_jugador(jugador: cls_jugador.Jugador):
        esta_completa: bool
        esta_completa = Arbitro.partida.add_jugador(jugador)
        if (esta_completa == True):
            print("se inicia la partida")
            Arbitro.inicia_ronda()

    @staticmethod
    def inicia_ronda():
        print("se inicia la ronda")
        print()

        # repartir cartas a los jugadores
        lista_jugadores: list[cls_jugador.Jugador]
        lista_jugadores = Arbitro.partida.get_lista_jugadores()
        for jugador in lista_jugadores:
            mano = cls_mano.Mano()
            for i in range(0, 3):
                carta = Arbitro.baraja.get_carta_aleatoria()
                estado = cls_estados_carta.Estados.EN_MANO
                mano.add_carta(
                    cls_carta_en_juego.Carta_en_juego(carta, estado))
            jugador.add_mano(mano)

        Arbitro.inicia_mano()

        # test purposes
        # for jugador in lista_jugadores:
        #     print(jugador.get_nombre())
        #     jugador.print_mano()

        pass

    @staticmethod
    def inicia_mano():
        Arbitro.partida.inicializa_mano()
        # Arbitro.partida.inicializa_mano_ganada()

        # asigna jugador en turno al primero
        lista_jugadores: list[cls_jugador.Jugador]
        lista_jugadores = Arbitro.partida.get_lista_jugadores()
        Arbitro.set_jugador_en_turno(lista_jugadores[0], 0)
        #print(f'jugador primero: {Arbitro.get_jugador_en_turno().get_nombre()}')

        # enviar mensaje al jugador en turno de que juegue
        Arbitro.jugador_en_turno.juega()

    # el jugador avisa al arbitro de la decision y/o carta jugada
    @staticmethod
    def recoge_decision(decision: cls_decision.Decisiones, carta: cls_carta):
        print(f'juega {Arbitro.jugador_en_turno.get_nombre()}')
        print(decision)
        print(carta.get_nombre())
        print()

        mano = cls_mano.Mano()
        estado = cls_estados_carta.Estados.EN_TABLERO
        mano.add_carta(cls_carta_en_juego.Carta_en_juego(carta, estado))

        Arbitro.partida.add_mano(mano)

        lista_jugadores = Arbitro.partida.get_lista_jugadores()
        if (Arbitro.indice_jugador_en_turno + 1 == len(lista_jugadores)):
            # terminamos la mano
            Arbitro.evalua_jugada()
        else:
            Arbitro.indice_jugador_en_turno = Arbitro.indice_jugador_en_turno + 1
            Arbitro.set_jugador_en_turno(
                lista_jugadores[Arbitro.indice_jugador_en_turno], Arbitro.indice_jugador_en_turno)
            Arbitro.jugador_en_turno.juega()

    @staticmethod
    def evalua_jugada():
        manos: list[cls_mano.Mano]
        manos = Arbitro.partida.get_cartas_mano()
        valores: list[int]
        valores = []
        for mano in manos:
            i = 0
            valor = mano.get_cartas()[0].carta.get_valor()
            print(
                f'{mano.get_cartas()[0].carta.get_nombre()} : valor -> {valor}')
            valores.append(valor)

        valor_tope = 0
        i = 0
        for valor in valores:
            if (valor > valor_tope):
                indice_ganador = i
                valor_tope = valor
                print(
                    f'indice ganador {indice_ganador} ... valor tope {valor_tope}')
            i = i + 1

        lista_jugadores = Arbitro.partida.get_lista_jugadores()
        jugador_ganador = lista_jugadores[indice_ganador]
        print(f'ha vencido {jugador_ganador.get_nombre()}')

        Arbitro.partida.add_mano_ganada(jugador_ganador.get_ordinal())

        hay_vencedor = False
        for jugador in lista_jugadores:
            ordinal = jugador.get_ordinal()
            num_manos_ganadas = Arbitro.partida.get_num_manos_ganadas(ordinal)
            print(f'{jugador.get_nombre()} ha ganado {num_manos_ganadas} manos')
            if (num_manos_ganadas == 2):
                hay_vencedor = True
                ordinal_ganador = ordinal

        if (hay_vencedor == True):
            print()
            print(
                f'¡¡¡ {lista_jugadores[ordinal_ganador-1].get_nombre()} ha ganado la ronda !!!')
            Arbitro.partida.add_puntos(lista_jugadores[ordinal_ganador-1], 3)
            print()
            lista_jugadores = Arbitro.partida.get_lista_jugadores()
            for jugador in lista_jugadores:
                puntos = jugador.get_puntos()
                print(
                    f'jugador {jugador.get_nombre()} tiene {puntos} puntos')

            ganador = Arbitro.partida.get_ganador()
            if (ganador != None):
                print(
                    f'¡¡¡¡ ++++++++++++++++ jugador {ganador.get_nombre()} ha ganado la partida +++++++++++++++++++++++ !!!')
            else:
                Arbitro.partida.inicializa_mano_ganada()
                Arbitro.inicia_ronda()

        else:
            Arbitro.inicia_mano()

    @staticmethod
    def finaliza_partida():
        pass
