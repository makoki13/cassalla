import cls_palo
import cls_carta
import cls_baraja_safor
import cls_carta_en_juego
import cls_estados_carta
import cls_mano
import cls_tablero
import cls_usuario
import cls_jugador


if __name__ == "__main__":
    # miPalo = cls_palo.Palos
    # miPalo.test()

    # mi_baraja = cls_baraja.Baraja()
    # mi_carta = cls_carta.Carta(1, cls_palo.Palos.ESPADAS, 'as de espadas', 14)
    # mi_baraja.add_carta(mi_carta)
    # mi_carta = cls_carta.Carta(1, cls_palo.Palos.BASTOS, 'as de bastos', 13)
    # mi_baraja.add_carta(mi_carta)

    # mi_baraja.test()

    # baraja = cls_baraja_safor.Baraja_safor()
    # baraja.inicializa()
    # baraja.test()

    # mi_carta = cls_carta.Carta(1, cls_palo.Palos.ESPADAS, 'as de espadas', 14)
    # carta_en_juego = cls_carta_en_juego.Carta_en_juego(
    #     mi_carta, cls_estados_carta.Estados.EN_MANO)
    # carta_en_juego.test()

    # baraja = cls_baraja_safor.Baraja_safor()
    # baraja.inicializa()

    # cls_tablero.Tablero.inicializa(2)

    # mi_mano = cls_mano.Mano()
    # mi_mano.add_carta(baraja.get_carta(0))
    # mi_mano.add_carta(baraja.get_carta(1))
    # mi_mano.add_carta(baraja.get_carta(2))

    # # mi_mano.test()

    # cls_tablero.Tablero.add_mano(mi_mano)

    # mi_mano = cls_mano.Mano()
    # mi_mano.add_carta(baraja.get_carta(3))
    # mi_mano.add_carta(baraja.get_carta(4))
    # mi_mano.add_carta(baraja.get_carta(5))

    # cls_tablero.Tablero.add_mano(mi_mano)

    # cls_tablero.Tablero.print_mano(0)
    # print("---------------------------------")
    # cls_tablero.Tablero.print_mano(1)

    usuario1 = cls_usuario.Usuario(1, 'Makoki')
    print(usuario1.get_nombre())

    usuario2 = cls_usuario.Usuario(1, 'Saisua')
    print(usuario2.get_nombre())

    baraja = cls_baraja_safor.Baraja_safor()
    baraja.inicializa()

    mi_mano = cls_mano.Mano()
    mi_mano.add_carta(baraja.get_carta(1))
    mi_mano.add_carta(baraja.get_carta(2))
    mi_mano.add_carta(baraja.get_carta(3))

    jugador1 = cls_jugador.Jugador(usuario1, 1, mi_mano)

    mi_mano = cls_mano.Mano()
    mi_mano.add_carta(baraja.get_carta(3))
    mi_mano.add_carta(baraja.get_carta(4))
    mi_mano.add_carta(baraja.get_carta(5))

    jugador2 = cls_jugador.Jugador(usuario2, 2, mi_mano)

    jugador1.add_puntos(3)
    jugador2.add_puntos(5)

    print(jugador1.get_puntos())
    print(jugador2.get_puntos())
