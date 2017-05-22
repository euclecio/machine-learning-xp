#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import numpy as np

valores = [56.8182, 79.5455, 70.1923, 68.1818, 61.3636, 52.2727, 65.7143, 61.4286, 62.8571, 64.2857, 68.2692, 66.3462, 62.5, 67.0455, 72.7273]

#variancia
v = np.var(valores)

#desvio padrão
d = np.sqrt(v)

#media
m = np.mean(valores)

print('Variância: %s' % (v))
print('Média: %s' % (m))
print('Desvio Padrão: %s' % (d))
