
import cls_jugador
import cls_partida
import cls_carta
import cls_decision
import cls_baraja_safor
import cls_ronda
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
            Arbitro.inicia_jugada()

    @staticmethod
    def inicia_jugada():
        Arbitro.partida.inicia_contador_rondas()
        print("se inician las rondas")
        print()

        # repartir cartas a los jugadores
        lista_jugadores: list[cls_jugador.Jugador]
        lista_jugadores = Arbitro.partida.get_lista_jugadores()
        for jugador in lista_jugadores:
            ronda = cls_ronda.Ronda()
            # TODO Que no se repitan las cartas :-D
            for i in range(0, 3):
                carta = Arbitro.baraja.get_carta_aleatoria()
                estado = cls_estados_carta.Estados.EN_MANO
                ronda.add_carta(
                    cls_carta_en_juego.Carta_en_juego(carta, estado))
            jugador.add_ronda(ronda)

        Arbitro.inicia_ronda()

        pass

    # Se trata de el envite entre dos cartas
    @staticmethod
    def inicia_ronda():
        # TODO hay que poner un contador de ronda actual

        Arbitro.partida.inicializa_ronda()

        # asigna jugador en turno al primero
        lista_jugadores: list[cls_jugador.Jugador]
        lista_jugadores = Arbitro.partida.get_lista_jugadores()
        Arbitro.set_jugador_en_turno(lista_jugadores[0], 0)
        # print(f'jugador primero: {Arbitro.get_jugador_en_turno().get_nombre()}')

        # enviar mensaje al jugador en turno de que juegue
        Arbitro.jugador_en_turno.juega(Arbitro.partida.get_ronda_actual())

    # el jugador avisa al arbitro de la decision y/o carta jugada
    @staticmethod
    def recoge_decision(decision: cls_decision.Decisiones, carta: cls_carta):
        print(f'juega {Arbitro.jugador_en_turno.get_nombre()}')
        print(decision)
        print()

        if (decision == cls_decision.Decisiones.USO_CARTA):
            print(carta.get_nombre())
            ronda = cls_ronda.Ronda()
            estado = cls_estados_carta.Estados.EN_TABLERO
            ronda.add_carta(cls_carta_en_juego.Carta_en_juego(carta, estado))

            Arbitro.partida.add_ronda(ronda)

            lista_jugadores = Arbitro.partida.get_lista_jugadores()
            if (Arbitro.indice_jugador_en_turno + 1 == len(lista_jugadores)):
                # terminamos la ronda
                Arbitro.evalua_jugada()
            else:
                Arbitro.indice_jugador_en_turno = Arbitro.indice_jugador_en_turno + 1
                Arbitro.set_jugador_en_turno(
                    lista_jugadores[Arbitro.indice_jugador_en_turno], Arbitro.indice_jugador_en_turno)
                Arbitro.jugador_en_turno.juega(
                    Arbitro.partida.get_ronda_actual())

        # solo se puede envidar en la primera ronda
        # TODO poner un contador de puntos de envido y otro de truc
        elif decision == cls_decision.Decisiones.ENVIDO:
            pass

        elif decision == cls_decision.Decisiones.QUIERO:
            pass

        # asignamos los puntos en juego al otro jugador
        elif decision == cls_decision.Decisiones.ME_VOY:
            pass

    @ staticmethod
    def evalua_jugada():
        rondas: list[cls_ronda.Ronda]
        rondas = Arbitro.partida.get_cartas_ronda()
        valores: list[int]
        valores = []
        for ronda in rondas:
            i = 0
            valor = ronda.get_cartas()[0].carta.get_valor()
            print(
                f'{ronda.get_cartas()[0].carta.get_nombre()} : valor -> {valor}')
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

        Arbitro.partida.add_ronda_ganada(jugador_ganador.get_ordinal())

        hay_vencedor = False
        for jugador in lista_jugadores:
            ordinal = jugador.get_ordinal()
            num_rondas_ganadas = Arbitro.partida.get_num_rondas_ganadas(
                ordinal)
            print(f'{jugador.get_nombre()} ha ganado {num_rondas_ganadas} rondas')
            if (num_rondas_ganadas == 2):
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
                Arbitro.partida.inicializa_ronda_ganada()
                Arbitro.inicia_jugada()

        else:
            Arbitro.inicia_ronda()

    @ staticmethod
    def finaliza_partida():
        pass
