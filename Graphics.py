import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

# График высоты подъёма лунохода относительно скорости, высота кочки = 0.2, длина кочки =0.3
x = np.linspace(0, 5, 100)
def overage_sin(h_bump, s_bump): ## вычисление примерного угла кочки
    return np.sqrt(h_bump/ np.sqrt(pow(0.2, 2)+pow(0.3, 2)))

def overage_cos(h_bump, s_bump):
    return 1- pow(overage_sin(h_bump, s_bump), 2)
y = x**2*((overage_sin(0.2, 0.3)-0.25*(overage_cos(0.2, 0.3)))/
          (overage_sin(0.2, 0.3)+0.25*(overage_cos(0.2, 0.3))))*overage_sin(0.2,0.3)**2/2*1.62

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()


# Вычисление длины тормозного пути относительно скорости
x = np.linspace(0, 5, 100)
y = x**2/(2*0.25*1.62)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()

#  Добавляем подписи к осям:
ax.set_xlabel('скорость (м/c)')
ax.set_ylabel('длина тормозного пути (м)')

plt.show()

