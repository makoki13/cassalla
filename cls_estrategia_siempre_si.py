import cls_estrategia
from cls_decision import Decisiones


class Estrategia_siempre_si(cls_estrategia.Abstract_estrategia):

    def analiza_envido(self, tipo_envido: Decisiones):
        if (tipo_envido == Decisiones.ENVIDO) or (tipo_envido == Decisiones.TORNE_ENVIDO) or (tipo_envido == Decisiones.LA_FALTA_ENVIDO):
            return Decisiones.QUIERO


# o_estrategia_siempre_si = type("estrategia1", (object, ), {
#     # datos
#     "nombre": "estrategia siempre si",
#     "id": 1,

#     # funciones
#     "analiza_envido": Estrategia_siempre_si.analiza_envido
# })
