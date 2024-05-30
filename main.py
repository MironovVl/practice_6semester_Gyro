import math
import serial
import numpy as np
from xlwt import Workbook
import matplotlib.pyplot as plt
from plot import update_plot
from visual import visual

wb = Workbook()
a1 = visual()
sheet1 = wb.add_sheet("Sheet 1")
headers = ['ax', 'ay', 'az', 'gx', 'gy', 'gz']
for cols, header in enumerate(headers):
    sheet1.write(0, cols, header)

ser = serial.Serial('COM3', 38400)

for _ in range(15):
    response = ser.readline()

list_of_integers = []
line = 0

# "нули" ускорения
default_ax = default_ay = default_az = 0
default_gx = default_gy = default_gz = 0
for _ in range(20):
    response = ser.readline()
    decoded_response = response.decode('utf-8')
    list_of_integers = (np.fromstring(decoded_response, dtype=int, sep='\t').tolist())
    default_ax += list_of_integers[0] / 20
    default_ay += list_of_integers[1] / 20
    default_az += list_of_integers[2] / 20
    default_gx += list_of_integers[3] / 20
    default_gy += list_of_integers[4] / 20
    default_gz += list_of_integers[5] / 20

Vx = Vy = Vz = 0  # скорости
angle1 = angle2 = angle3 = 0
deltaTime = 0.0014286
sensitivity = 5

while line < 5000:
    line += 1
    # print(line)
    response = ser.readline()
    decoded_response = response.decode('utf-8')
    # print(decoded_response[:-1])
    if decoded_response.startswith('Start'):
        break
    list_of_integers = (np.fromstring(decoded_response, dtype=int, sep='\t').tolist())
    for i in range(len(list_of_integers)):
        sheet1.write(line, i, list_of_integers[i])
    ax, ay, az, gx, gy, gz = list_of_integers
    # update_plot(ax, ay, az, 2*gx, gy,line)
    # speed
    if abs(ax - default_ax) > sensitivity:
        Vx += deltaTime * (ax - default_ax)
    if abs(ay - default_ay) > sensitivity:
        Vy += deltaTime * (ay - default_ay)
    if abs(az - default_az) > sensitivity:
        Vz += deltaTime * (az - default_az)

    # углы по гироскопу
    if abs(gx - default_gx) > sensitivity:
        angle1 += deltaTime * (gx - default_gx)
    if abs(gy - default_gy) > sensitivity:
        angle2 += deltaTime * (gy - default_gy)
    if abs(gz - default_gz) > sensitivity:
        angle3 += deltaTime * (gz - default_gz)

    # углы по акселерометру
    sumAccelerator = (ax ** 2 + ay ** 2 + az ** 2) ** 0.5
    gamma = math.asin(az / sumAccelerator)
    theta = -math.asin(ax / (sumAccelerator * math.cos(gamma)))

    template = '{:.' + str(2) + 'f}'
    print(template.format(angle1), template.format(angle2), template.format(angle3), end=' | ')
    print(template.format(gamma * 180 / math.pi), template.format(theta * 180 / math.pi), end='  |  ')
    print(list_of_integers, end=' ')
    print('')
    # visual.moveAvi(a1, gamma * 180 / math.pi, theta * 180 / math.pi)
    # update_plot(theta* 180 / math.pi,gamma* 180 / math.pi,0,line)
    # update_plot(angle1, angle2, angle3, line)
    update_plot(angle1, angle2, angle3, -gamma * 180 / math.pi, theta * 180 / math.pi, line)

plt.ioff()
plt.show()
ser.close()
wb.save("data.xls")
