import cls_baraja
import cls_carta
import cls_palo


class Baraja_safor(cls_baraja.Baraja):
    def __init__(self):
        super().__init__()

        self.add_carta(cls_carta.Carta(
            1, cls_palo.Palos.ESPADAS, 'as de espadas', 14))

        self.add_carta(cls_carta.Carta(
            1, cls_palo.Palos.BASTOS, 'as de bastos', 13))

        self.add_carta(cls_carta.Carta(
            7, cls_palo.Palos.ESPADAS, 'siete de espadas', 12))

        self.add_carta(cls_carta.Carta(
            7, cls_palo.Palos.OROS, 'siete de oros', 11))

        self.add_carta(cls_carta.Carta(
            3, cls_palo.Palos.BASTOS, 'tres de bastos', 10))
        self.add_carta(cls_carta.Carta(
            3, cls_palo.Palos.COPAS, 'tres de copas', 10))
        self.add_carta(cls_carta.Carta(
            3, cls_palo.Palos.ESPADAS, 'tres de espadas', 10))
        self.add_carta(cls_carta.Carta(
            3, cls_palo.Palos.OROS, 'tres de oros', 10))

        self.add_carta(cls_carta.Carta(
            2, cls_palo.Palos.BASTOS, 'dos de bastos', 9))
        self.add_carta(cls_carta.Carta(
            2, cls_palo.Palos.COPAS, 'dos de copas', 9))
        self.add_carta(cls_carta.Carta(
            2, cls_palo.Palos.ESPADAS, 'dos de espadas', 9))
        self.add_carta(cls_carta.Carta(
            2, cls_palo.Palos.OROS, 'dos de oros', 9))

        self.add_carta(cls_carta.Carta(
            1, cls_palo.Palos.COPAS, 'as de copas', 8))
        self.add_carta(cls_carta.Carta(
            1, cls_palo.Palos.OROS, 'as de oros', 8))

        self.add_carta(cls_carta.Carta(
            12, cls_palo.Palos.BASTOS, 'rey de bastos', 7))
        self.add_carta(cls_carta.Carta(
            12, cls_palo.Palos.COPAS, 'rey de copas', 7))
        self.add_carta(cls_carta.Carta(
            12, cls_palo.Palos.ESPADAS, 'rey de espadas', 7))
        self.add_carta(cls_carta.Carta(
            12, cls_palo.Palos.OROS, 'rey de oros', 7))

        self.add_carta(cls_carta.Carta(
            11, cls_palo.Palos.BASTOS, 'caballo de bastos', 6))
        self.add_carta(cls_carta.Carta(
            11, cls_palo.Palos.COPAS, 'caballo de copas', 6))
        self.add_carta(cls_carta.Carta(
            11, cls_palo.Palos.ESPADAS, 'caballo de espadas', 6))
        self.add_carta(cls_carta.Carta(
            11, cls_palo.Palos.OROS, 'caballo de oros', 6))

        self.add_carta(cls_carta.Carta(
            10, cls_palo.Palos.BASTOS, 'sota de bastos', 5))
        self.add_carta(cls_carta.Carta(
            10, cls_palo.Palos.COPAS, 'sota de copas', 5))
        self.add_carta(cls_carta.Carta(
            10, cls_palo.Palos.ESPADAS, 'sota de espadas', 5))
        self.add_carta(cls_carta.Carta(
            10, cls_palo.Palos.OROS, 'sota de oros', 5))

        self.add_carta(cls_carta.Carta(
            7, cls_palo.Palos.ESPADAS, 'siete de copas', 4))
        self.add_carta(cls_carta.Carta(
            7, cls_palo.Palos.OROS, 'siete de bastos', 4))

        self.add_carta(cls_carta.Carta(
            6, cls_palo.Palos.BASTOS, 'seis de bastos', 3))
        self.add_carta(cls_carta.Carta(
            6, cls_palo.Palos.COPAS, 'seis de copas', 3))
        self.add_carta(cls_carta.Carta(
            6, cls_palo.Palos.ESPADAS, 'seis de espadas', 3))
        self.add_carta(cls_carta.Carta(
            6, cls_palo.Palos.OROS, 'seis de oros', 3))

        self.add_carta(cls_carta.Carta(
            5, cls_palo.Palos.BASTOS, 'cinco de bastos', 2))
        self.add_carta(cls_carta.Carta(
            5, cls_palo.Palos.COPAS, 'cinco de copas', 2))
        self.add_carta(cls_carta.Carta(
            5, cls_palo.Palos.ESPADAS, 'cinco de espadas', 2))
        self.add_carta(cls_carta.Carta(
            5, cls_palo.Palos.OROS, 'cinco de oros', 2))

        self.add_carta(cls_carta.Carta(
            4, cls_palo.Palos.BASTOS, 'cuatro de bastos', 1))
        self.add_carta(cls_carta.Carta(
            4, cls_palo.Palos.COPAS, 'cuatro de copas', 1))
        self.add_carta(cls_carta.Carta(
            4, cls_palo.Palos.ESPADAS, 'cuatro de espadas', 1))
        self.add_carta(cls_carta.Carta(
            4, cls_palo.Palos.OROS, 'cuatro de oros', 1))

    # def get_carta(self,indice: int):
    #    return
