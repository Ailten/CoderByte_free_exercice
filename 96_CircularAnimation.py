
# Circular animation.
# make a circular animation in ascii console.


import time
import os
import math


gradient = ' .:-=+*#%@'
window = (40, 8)  # resolution print ascii.
window_ratio = window[0] / window[1]
frame_rate = 1/30  # frame rate.

center_pos = (window[0]/2, window[1]/2)
r = 0
r_increase = 0.05  # speed panning.
split_waves = 2.5
def distTo(pos_a: tuple, pos_b: tuple) -> float:
    pow_dif_x = abs(pos_a[0] - pos_b[0]) ** 2
    pow_dif_y = abs(pos_a[1] - pos_b[1]) ** 2
    return math.sqrt(pow_dif_x / window_ratio + pow_dif_y)  # use window_ratio for adapt distance on window size.
max_dist_center = distTo(center_pos, (0, 0))

for update_time in range(100):

    frame = ''
    for y in range(window[1]):
        for x in range(window[0]):
            dist_center = distTo(center_pos, (x, y))
            dist_center = dist_center / max_dist_center  # normalise 0~1.
            dist_center = (dist_center - r) % 1  # padding.
            dist_center = (dist_center * split_waves) % 1  # split waves.
            i_gradient = int(dist_center * (len(gradient) - 1))  # cast as index gradient.
            frame += gradient[i_gradient]
        if y < window[1] - 1:
            frame += '\n'

    r += r_increase

    os.system('cls' if os.name == 'nt' else 'clear')
    print(frame)
    time.sleep(frame_rate)

