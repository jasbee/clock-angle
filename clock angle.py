def clock_angle(h, m):
    hour = (60 * h + m) / 2.0
    minute = 6 * m
    angle = abs(hour - minute)

    if angle > 180:
        angle = 360 - angle
    return angle

x = input('Please enter the time: ')

h = int(x[:-3])
if len(x) is 5:
    m = int(x[3:])
if len(x) is 4:
    m = int(x[2:])

a = int(clock_angle(h, m))

print("The angle between the two clock hands at " + x +
" would be " + str(a) + " degrees.")

input('')
