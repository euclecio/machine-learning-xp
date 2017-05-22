#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import numpy as np

valores = [61.4286, 55.7143, 65.7143, 62.8571, 57.1429, 62.8571, 68.5714, 62.8571, 54.2857, 62.8571, 65.7143, 58.5714, 62.8571, 58.5714, 60.0]

#variancia
v = np.var(valores)

#desvio padrão
d = np.sqrt(v)

#media
m = np.mean(valores)

print('Variância: %s' % (v))
print('Média: %s' % (m))
print('Desvio Padrão: %s' % (d))
