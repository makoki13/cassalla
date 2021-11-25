from cls_decision import Decisiones, Decision
import cls_usuario
import cls_ronda
#import cls_arbitro
import cls_estados_carta
import lista_estrategias
from cls_carta_en_juego import Carta_en_juego


class Jugador:
    def __init__(self, usuario: cls_usuario.Usuario, ordinal: int):
        self.usuario = usuario
        self.ordinal = ordinal
        self.ronda = None
        self.puntos = 0
        #self.estrategia = lista_estrategias.get_estrategia_a_reu()
        self.estrategia = lista_estrategias.get_estrategia_siempre_si_envido()
        self.decision_envido = None
        self.decision_truc = None

    def add_ronda(self, ronda: cls_ronda.Ronda):
        self.ronda = ronda

    def add_puntos(self, puntos: int):
        self.puntos = self.puntos + puntos

    def get_puntos(self):
        return self.puntos

    def set_puntos(self, puntos: int):
        self.puntos = puntos

    def print_ronda(self):
        for carta in self.ronda.get_cartas():
            carta.print_carta()

    def get_nombre(self):
        return self.usuario.get_nombre()

    def get_ordinal(self):
        return self.ordinal

    # En esta funcion se debe de implementar la inteligencia del jugador
    def juega(self, ronda, tipo_envido: Decisiones, tipo_truc: Decisiones):
        print(f'jugador {self.get_nombre()} juega en la ronda {ronda} con un tipo de envido de {tipo_envido}')        
        if (ronda == 1):
            # evaluamos la ronda       
            carta_a_enviar = Carta_en_juego(None,None)
            if (tipo_envido != Decisiones.DECISION_YA_TOMADA):
                decision = self.estrategia.analiza_envido(tipo_envido)         
                print(f'se ha tomado la decision de {decision}')   
                if (decision == Decisiones.SIN_DECISION):
                    decision = Decisiones.USO_CARTA
                    carta_a_enviar = None
                    for carta in self.ronda.get_cartas():
                        if carta.estado == cls_estados_carta.Estados.EN_MANO:
                            print(f'se mira carta a carta {carta}')
                            carta_a_enviar = carta.carta
                            carta.estado = cls_estados_carta.Estados.EN_TABLERO
                            break            
                else:
                    carta_a_enviar  = None
                    print(f'no se mira carta a carta {decision} con carta {carta_a_enviar}')
                    pass
            else:                
                decision = Decisiones.USO_CARTA
                carta_a_enviar = None
                for carta in self.ronda.get_cartas():
                    print(f'mirando carta {carta.carta.get_nombre()} con estado {carta.estado}')
                    print()
                    print()
                    if carta.estado == cls_estados_carta.Estados.EN_MANO:
                        carta_a_enviar = carta.carta                        
                        print(f'carta a enviar {carta_a_enviar.get_nombre()}')
                        carta.estado = cls_estados_carta.Estados.EN_TABLERO
                        break            
            
        else:
            # TODO este codigo y el de arriba hay que pasarlo a funcion
            decision = Decisiones.USO_CARTA
            carta_a_enviar = None
            for carta in self.ronda.get_cartas():
                if carta.estado == cls_estados_carta.Estados.EN_MANO:
                    carta_a_enviar = carta.carta
                    carta.estado = cls_estados_carta.Estados.EN_TABLERO
                    break


        print(f'enviando carta... {decision}')
        
        return Decision(decision, carta_a_enviar)
        #cls_arbitro.Arbitro.recoge_decision(decision, carta_a_enviar.carta)

    def juego_erroneo(self):
        pass

    def set_decision_envido(self,decision: Decisiones):
        self.decision_envido = decision

    def get_decision_envido(self):
        return self.decision_envido

    def set_decision_truc(self,decision: Decisiones):
        self.decision_truc = decision

    def get_decision_truc(self):
        return self.decision_truc

    def get_puntos_envido(self):
        ronda = self.ronda.get_cartas()
        carta_en_mano: Carta_en_juego
        puntos_envido = 0
        for carta_en_mano in ronda:            
            puntos_envido += carta_en_mano.carta.get_valor_envido()
            print(f'jugador {self.get_nombre()} tiene carta {carta_en_mano.carta.get_nombre()} acum envido {puntos_envido}')
        return puntos_envido
