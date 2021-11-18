import random

import cls_estrategia_siempre_si
import cls_estrategia_siempre_no

estrategias = []


def inicializa():
    # o = cls_estrategia_siempre_si.o_estrategia_siempre_si()
    # estrategias.append(o)
    # o = cls_estrategia_siempre_no.o_estrategia_siempre_no()
    # estrategias.append(o)

    o = cls_estrategia_siempre_si.Estrategia_siempre_si()
    estrategias.append(o)
    o = cls_estrategia_siempre_no.Estrategia_siempre_no()
    estrategias.append(o)


def get_estrategia_a_reu():
    return estrategias[random.randint(0, len(estrategias)-1)]
