#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import numpy as np

valores = [26.087, 25.8979, 33.5068, 34.6514, 35.1127, 31.9149, 31.3167, 34.7568, 31.2057, 37.7732, 35.0676, 34.4009, 36.4204, 39.5421, 36.862]

#variancia
v = np.var(valores)

#desvio padrão
d = np.sqrt(v)

#media
m = np.mean(valores)

print('Variância: %s' % (v))
print('Média: %s' % (m))
print('Desvio Padrão: %s' % (d))
