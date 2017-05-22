#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import numpy as np

valores = [53.8324, 53.8324, 67.6357, 53.8324, 53.8324, 53.8324, 53.8324, 53.8324, 53.8324, 53.8324, 53.8324, 53.8324, 69.186, 53.8324, 53.8324]

#variancia
v = np.var(valores)

#desvio padrão
d = np.sqrt(v)

#media
m = np.mean(valores)

print('Variância: %s' % (v))
print('Média: %s' % (m))
print('Desvio Padrão: %s' % (d))
