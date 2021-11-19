import cls_estrategia
from cls_decision import Decisiones


class Estrategia_siempre_no(cls_estrategia.Abstract_estrategia):

    def analiza_envido(self, tipo_envido: Decisiones):
        #print(f"analiza envido . {tipo_envido} en Estrategia_siempre_no")
        if (tipo_envido == Decisiones.ENVIDO) or (tipo_envido == Decisiones.TORNE_ENVIDO) or (tipo_envido == Decisiones.LA_FALTA_ENVIDO):
            return Decisiones.ME_VOY


# o_estrategia_siempre_no = type("estrategia2", (object, ), {
#     # datos
#     "nombre": "estrategia siempre no",
#     "id": 2,

#     # funciones
#     "analiza_envido": Estrategia_siempre_no.analiza_envido
# })
