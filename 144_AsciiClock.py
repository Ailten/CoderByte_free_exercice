
# ascii clock.
# /

# make a clock in ascii.


import math

class AsciiClock:
    hour: int
    minute: int

    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def addMinute(self, minute_to_add: int):
        self.minute += minute_to_add
        hour_to_add = self.minute // 60
        if hour_to_add != 0:
            self.minute = self.minute % 60
            self.addHour(hour_to_add)

    def addHour(self, hour_to_add: int):
        self.hour = (self.hour + hour_to_add) % 24

    # can't substract minutes and hour.

    def getStrValue(self) -> str:
        return f'{str(self.hour).rjust(2, "0")}:{str(self.minute).rjust(2, "0")}'
    
    def getStrClock(self, clock_size: tuple[int,int]=(33,11)) -> str:
        block_char = (' ', '=')
        hour_char = 'H'
        minute_char = 'M'
        rayon = clock_size[0] // 2
        rayon_y = clock_size[1] // 2
        ratio = clock_size[0] / clock_size[1]
        
        hour_angle = (self.hour / 24) * 360
        minute_angle = (self.minute / 60) * 360

        def dist(pos_a:tuple[int,int], pos_b:tuple[int,int]) -> float:
            dif_abs = (
                pow(abs(pos_a[0] - pos_b[0]) , 2),
                pow(abs(pos_a[1] * ratio - pos_b[1] * ratio) , 2)
            )
            return math.sqrt(dif_abs[0] + dif_abs[1])
        
        def isPosInAngle(pos:tuple[int,int], angle:int, range_valid:float=5.0) -> bool:
            angle_pos = math.atan2(pos[0], pos[1] * ratio)
            angle_pos = (math.pi + angle_pos) / (2*math.pi)
            angle_pos = 1.0 - angle_pos
            angle_pos *= 360
            return abs(angle_pos - angle) < range_valid

        return (
            '\n'.join([ 
                ''.join([ (
                    block_char[0] if dist((c, l), (rayon, rayon_y)) > rayon else
                    hour_char if isPosInAngle((c-rayon,l-rayon_y), hour_angle) else
                    minute_char if isPosInAngle((c-rayon,l-rayon_y), minute_angle) else
                    block_char[1]
                ) for c in range(clock_size[0])]) 
                for l in range(clock_size[1]) 
            ])
        )

    def getStrFullClock(self) -> str:
        clock_size = (22, 11)
        clock = self.getStrClock(clock_size=clock_size)
        value = self.getStrValue()
        space_value = (clock_size[0] - len(value)) // 2
        return (
            '╔'+('═'*clock_size[0])+'╗\n║' +
            '║\n║'.join([ l for l in clock.split('\n') ]) +
            '║\n║'+(' '*space_value)+value+(' '*(clock_size[0]-len(value)-space_value)) +
            '║\n╚'+('═'*clock_size[0])+'╝'
        )



# ------> demo.

import os
import time

my_clock = AsciiClock(hour=0, minute=0)
for i in range(60*24):
    print(my_clock.getStrFullClock())

    time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')

    my_clock.addMinute(1)

print('end')
