
from cls_decision import Decisiones


class Puntos:
    @staticmethod
    def get_puntos_envido(decision: Decisiones, tipo_envido: Decisiones,  decision_anterior: Decisiones):
        print()
        print(f'****** decision: {decision} tipo_envido: {tipo_envido} decision anterior: {decision_anterior} ******')
        puntos: int = 0
        #pendiente que no se quiera si era la primera decision (parametro decision anterior)
        if decision == Decisiones.NO_QUIERO:
            if tipo_envido == Decisiones.ENVIDO:
                puntos = 1
            elif tipo_envido == Decisiones.TORNE_ENVIDO:
                if decision_anterior==None:
                    puntos = 1
                else:
                    puntos = 2 #es imposible
            elif tipo_envido == Decisiones.LA_FALTA_ENVIDO:
                if decision_anterior==None:
                    puntos = 1
                else:
                    puntos = 4 #es imposible
        elif decision == Decisiones.QUIERO:
            if tipo_envido == Decisiones.ENVIDO:
                puntos = 2
            elif tipo_envido == Decisiones.TORNE_ENVIDO:
                puntos = 4                
            elif tipo_envido == Decisiones.QUIERO_LA_FALTA:
                # TODO tratarel tema de la falta
                puntos = 30
    
        return puntos
