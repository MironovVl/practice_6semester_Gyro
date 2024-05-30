import matplotlib.pyplot as plt
from collections import deque
import random
import time

# Создание очереди для хранения последних значений
n = 200  # Количество последних значений для отображения
values1 = deque(maxlen=n)
values2 = deque(maxlen=n)
values3 = deque(maxlen=n)
values4 = deque(maxlen=n)
values5 = deque(maxlen=n)
x_values = deque(maxlen=n)

# Создание окна графика и линий для обновления значений
plt.ion()
fig, ax = plt.subplots()

# line1, = ax.plot([], [], label='До фильтрации')
# line2, = ax.plot([], [], label='Гироскоп')
# line3, = ax.plot([], [], label='Гироскоп')
line4, = ax.plot([], [], label='Крен')
line5, = ax.plot([], [], label='Тангаж')

ax.legend()


# Функция для обновления графика
def update_plot(new_value1, new_value2,new_value3,new_value4,new_value5,i):
    values1.append(new_value1)
    values2.append(new_value2)
    values3.append(new_value3)
    values4.append(new_value4)
    values5.append(new_value5)
    x_values.append(i)

    # line1.set_xdata(x_values)
    # line1.set_ydata(values1)
    #
    # line2.set_xdata(x_values)
    # line2.set_ydata(values2)
    #
    # line3.set_xdata(x_values)
    # line3.set_ydata(values3)
    line4.set_xdata(x_values)
    line4.set_ydata(values4)
    line5.set_xdata(x_values)
    line5.set_ydata(values5)
    ax.relim()
    ax.autoscale_view()

    fig.canvas.draw()
    fig.canvas.flush_events()

    # ax.set_ylim(-120, 120)



# plt.ioff()
# plt.show()