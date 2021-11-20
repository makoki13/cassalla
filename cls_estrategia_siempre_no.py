import cls_estrategia
from cls_decision import Decisiones


class Estrategia_siempre_no(cls_estrategia.Abstract_estrategia):

    def nombre(self):
        return 'siempre no al envido'

    def analiza_envido(self, tipo_envido: Decisiones):
        decision: Decisiones
        if (tipo_envido == Decisiones.ENVIDO) or (tipo_envido == Decisiones.TORNE_ENVIDO) or (tipo_envido == Decisiones.LA_FALTA_ENVIDO):
            decision = Decisiones.ME_VOY
        else:
            decision = Decisiones.SIN_DECISION
        return decision


# o_estrategia_siempre_no = type("estrategia2", (object, ), {
#     # datos
#     "nombre": "estrategia siempre no",
#     "id": 2,

#     # funciones
#     "analiza_envido": Estrategia_siempre_no.analiza_envido
# })
