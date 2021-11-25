import cls_estrategia
from cls_decision import Decisiones

# Estrategia de pruebas; siempre dice si


class Estrategia_siempre_si(cls_estrategia.Abstract_estrategia):

    def nombre(self):
        return 'siempre si al envido'

    def analiza_envido(self, tipo_envido: Decisiones):
        print(f'tipo envido {tipo_envido}')
        if (tipo_envido == None) or (tipo_envido == Decisiones.SIN_DECISION) :
            decision = Decisiones.LA_FALTA_ENVIDO

        elif tipo_envido == Decisiones.ENVIDO:
            return Decisiones.NO_QUIERO_ENVIDO

        elif tipo_envido == Decisiones.TORNE_ENVIDO:
            return Decisiones.NO_QUIERO_TORNE_ENVIDO

        elif tipo_envido == Decisiones.LA_FALTA_ENVIDO:
            decision = Decisiones.QUIERO_LA_FALTA
            
        return decision


# o_estrategia_siempre_si = type("estrategia1", (object, ), {
#     # datos
#     "nombre": "estrategia siempre si",
#     "id": 1,

#     # funciones
#     "analiza_envido": Estrategia_siempre_si.analiza_envido
# })
