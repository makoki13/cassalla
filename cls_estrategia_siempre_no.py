import cls_estrategia
import cls_decision


class Estrategia_siempre_no(cls_estrategia.Abstract_estrategia):

    def analiza_envido(self, tipo_envido: cls_decision.Decisiones):
        print(f"analiza envido . {tipo_envido} en Estrategia_siempre_no")


# o_estrategia_siempre_no = type("estrategia2", (object, ), {
#     # datos
#     "nombre": "estrategia siempre no",
#     "id": 2,

#     # funciones
#     "analiza_envido": Estrategia_siempre_no.analiza_envido
# })
