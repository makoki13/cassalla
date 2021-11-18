import cls_estrategia
import cls_decision


class Estrategia_siempre_si(cls_estrategia.Abstract_estrategia):

    def analiza_envido(self, tipo_envido: cls_decision.Decisiones):
        print(f"analiza envido . {tipo_envido} en Estrategia_siempre_si")


# o_estrategia_siempre_si = type("estrategia1", (object, ), {
#     # datos
#     "nombre": "estrategia siempre si",
#     "id": 1,

#     # funciones
#     "analiza_envido": Estrategia_siempre_si.analiza_envido
# })
