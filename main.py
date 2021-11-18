# import cls_palo
# import cls_carta
# import cls_baraja_safor
# import cls_carta_en_juego
# import cls_estados_carta
# import cls_ronda
# import cls_tablero
# import cls_usuario
# import cls_jugador

# import cls_arbitro
# import cls_partida
# import cls_tablero
# import cls_marcador
# import cls_usuario
# import cls_jugador

import lista_estrategias
import cls_decision


if __name__ == "__main__":
    # inicio
    # num_jugadores: int = 2
    # cls_tablero.Tablero.inicializa(num_jugadores)
    # cls_marcador.Marcador.inicializa(num_jugadores, 20, 2)
    # cls_partida.Partida.inicializa(cls_tablero.Tablero, cls_marcador.Marcador)
    # cls_arbitro.Arbitro.set_partida(cls_partida.Partida)

    # usuario1 = cls_usuario.Usuario(1, 'Makoki')
    # jugador1 = cls_jugador.Jugador(usuario1, 1)
    # cls_arbitro.Arbitro.add_jugador(jugador1)

    # usuario2 = cls_usuario.Usuario(2, 'Saisua')
    # jugador2 = cls_jugador.Jugador(usuario2, 2)
    # cls_arbitro.Arbitro.add_jugador(jugador2)

    lista_estrategias.inicializa()
    mi_estrategia = lista_estrategias.get_estrategia_a_reu()
    mi_estrategia.analiza_envido(cls_decision.Decisiones.SIN_DECISION)

    # mi_estrategia = cls_estrategia_siempre_si.Estrategia_siempre_si()
    # mi_estrategia.analiza_envido(cls_decision.Decisiones.SIN_DECISION)

    # obj = cls_estrategia_siempre_si.o_estrategia_siempre_si()
    # obj.analiza_envido(cls_decision.Decisiones.ENVIDO)
