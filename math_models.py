import numpy as np

# Вычисление максимальной скорости, которая учитывает длину тормозного пути и высоту на которую может подняться луноход если наедет на кочку некоторой высоты и длины
R_moon = float(1737.1*1000)
M_moon = 7.3477*pow(10, 22)
G = 6.6743 * pow(10, -11)
g_moon = float(G*M_moon/pow(R_moon, 2))
friction = float(0.25) ## трение колёс о поверхность Луны



def overage_sin(h_bump, s_bump):
    return np.sqrt(h_bump/ np.sqrt(pow(h_bump, 2)+pow(s_bump, 2)))

def overage_cos(h_bump, s_bump):
    return 1- pow(overage_sin(h_bump, s_bump), 2)


def max_speed(h_max, h_bump, s_bump, s): ## вычисление максимальной скорости
    v0_s = np.sqrt(s * 2 * friction * g_moon)
    if h_bump!=0 and s_bump!=0:
        v0_h = ((h_max+h_bump)*2*g_moon)/((overage_sin(h_bump, s_bump)- friction*overage_cos(h_bump, s_bump))/
                            overage_sin(h_bump, s_bump) + friction*(overage_cos(h_bump, s_bump)))
        return v0_h, v0_s
    else:
        return 0, v0_s



h_max = float(input("Введите максимальную безопасную высоту на которую может подняться луноход: "))
h_bump = float(input("Введите максимальную высоту кочки: "))
s_bump = float(input("Введите длину кочки в момент отрыва лунохода от неё: "))
s = float(input("Введите безопасную максимальную длину тормозного пути"))

result = max_speed(h_max=h_max, h_bump=h_bump, s_bump=s_bump, s=s)

v0_h = result[0]*3.6 ## перевод в км/ч
v0_s = result[1]*3.6 ## перевод в км/ч

if result[0] == 0:
    print(f"Максимальная скорость (в км/ч): " '%.3f' % v0_s)
else:
    if result[0] > result[1]:
        print("Максимальная скорость (в км/ч): " '%.3f' % v0_s)
    else:
        print("Максимальная скорость: (в км/ч) " '%.3f' % v0_h)






