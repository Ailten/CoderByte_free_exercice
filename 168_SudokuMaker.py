
# Sudoku maker.
# /

import random
from functools import reduce
import re

class Cel:
    val: int|None
    is_lock: bool
    val_try: list[int]

    def __init__(self, val: int|None = None, is_lock: bool = False):
        self.val = val
        self.is_lock = is_lock
        self.val_try = []


class Sudoku:
    cels: list[list[Cel]]

    def __init__(self):
        self.cels = []
        for y in range(9):
            self.cels.append([])
            for x in range(9):
                self.cels[y].append(Cel())

    def fillLockNums(self, amount: int=1):
        i = 0
        while i < amount:
            x = None
            y = None

            # pick a random pos.
            while True:
                x,y = self.__pickRandomPos()
                if self.cels[y][x].val == None:
                    break
            
            # get val allows (only).
            val_allow = set(range(1, 10))
            val_allow -= set([ c.val for c in self.cels[y]])  # line.
            val_allow -= set([ l[x].val for l in self.cels])  # column.
            chunk_x = x-(x%3)
            chunk_y = y-(y%3)
            val_allow -= set(  # chunk.
                [ e.val for l in
                    [ l[chunk_x:chunk_x+3] for k,l in enumerate(self.cels) if k-(k%3) == chunk_y ]
                for e in l ]
            )

            # check.
            if len(val_allow) == 0:
                raise Exception('Sudoku un-solvable !')
            
            # set val lock.
            index_val_pick = random.randint(0, len(val_allow)-1)
            self.cels[y][x].val = list(val_allow)[index_val_pick]
            self.cels[y][x].is_lock = True

            # increment.
            i += 1

    def solv(self):
        i = 0
        is_back_track = False
        while i < 81:

            # back track over range.
            if i < 0:
                raise Exception('Sudoku un-solvable !')

            # get pos.
            x = i % 9
            y = i // 9
            c = self.cels[y][x]

            # skip lock.
            if c.is_lock:
                i += 1 if not is_back_track else -1
                continue

            # sanitise (if has value from a rollback)
            c.val = None

            # get val allows (only).
            val_allow = set(range(1, 10))
            val_allow -= set([ c.val for c in self.cels[y]])  # line.
            val_allow -= set([ l[x].val for l in self.cels])  # column.
            chunk_x = x-(x%3)
            chunk_y = y-(y%3)
            val_allow -= set(  # chunk.
                [ e.val for l in
                    [ l[chunk_x:chunk_x+3] for k,l in enumerate(self.cels) if k-(k%3) == chunk_y ]
                for e in l ]
            )
            val_allow -= set(c.val_try)  # value already try.

            # trigger back track (if no path further).
            if len(val_allow) == 0:
                c.val = None
                c.val_try = []
                is_back_track = True
                i -= 1
                continue

            # set value pick.
            val_pick = min(val_allow)
            c.val = val_pick
            c.val_try.append(val_pick)

            # increment.
            is_back_track = False
            i += 1
    
    def __pickRandomPos(self) -> tuple[int, int]:
        return (
            random.randint(0, 8),
            random.randint(0, 8)
        )
    
    def returnAsStr(self) -> str:
        output = '┏'+('━┯'*2+'━┳')*2+'━┯'*2+'━┓\n'
        for kl,l in enumerate(self.cels):
            output += '┃'  # first char of line.
            for kc,c in enumerate(l):
                output += ' ' if c.val == None else str(c.val)  # num.
                output += '┃' if kc % 3 == 2 else '│'  # next char num.
            output += '\n'
            if kl != 8:  # next line (without nums).
                if kl % 3 == 2:
                    output += '┣'+('━┿'*2+'━╋')*2+'━┿'*2+'━┫\n'
                else:
                    output += '┠'+('─┼'*2+'─╂')*2+'─┼'*2+'─┨\n'
        output += '┗'+('━┷'*2+'━┻')*2+'━┷'*2+'━┛'
        return output
    
    @staticmethod
    def getFromStr(sudo_str: str) -> "Sudoku":
        sudo_obj = Sudoku()

        lines = sudo_str.split('\n')
        y = 0
        for l in lines:
            vals = re.findall('[1-9 ]', l)
            if vals == None or len(vals) != 9:
                continue
            for x, v in enumerate(vals):
                if v == None or v == ' ':
                    continue
                sudo_obj.cels[y][x].val = int(v)
                sudo_obj.cels[y][x].is_lock = True
            y += 1
            if y == 9:
                break

        return sudo_obj
    
    def verify(self) -> bool:
        for y in range(9):
            for x in range(9):
                v = self.cels[y][x]
                
                # line.
                if v in [ c.val for k,c in enumerate(self.cels[y]) if k != x ]:
                    return False
                
                # column.
                if v in [ l[x].val for k,l in enumerate(self.cels) if k != y ]:
                    return False
                
                # chunk.
                chunk_x = x-(x%3)
                chunk_y = y-(y%3)
                cx = list(range(chunk_x, chunk_x+3))
                cy = list(range(chunk_y, chunk_y+3))
                cx.remove(x)
                cy.remove(y)
                if (
                    v == self.cels[cy[0]][cy[0]] or
                    v == self.cels[cy[0]][cy[1]] or
                    v == self.cels[cy[1]][cy[0]] or
                    v == self.cels[cy[1]][cy[1]]
                ):
                    return False
                
        return True

    

# -----------------> Make.

try_count = 0
while True:
    try_count += 1

    s = Sudoku()

    try:
        s.fillLockNums(42)  # easy.
    except:
        continue

    sudoku_str = s.returnAsStr()

    try:
        s.solv()
    except:
        continue

    if not s.verify():
        continue

    print(f'try build : {try_count}\n')

    print('      Sudoku      ')
    print(sudoku_str)
    print('      Solved      ')
    print(s.returnAsStr())
    break

