
# Life Game With Puls.
# adventofcode 2021 day 11


map = (
'4341347643\n'+
'5477728451\n'+
'2322733878\n'+
'5453762556\n'+
'2718123421\n'+
'4237886115\n'+
'5631617114\n'+
'2217667227\n'+
'4236581255\n'+
'4482627641'
)
map = [ [ int(c) for c in list(l) ] for l in map.split('\n')]


def calcNewFrame(current_map: list[list[str]]) -> tuple[list[list[str]], int]:

    output = []
    for y in range(len(current_map)):
        output.append([])
        for x in range(len(current_map[y])):
            current_cel = current_map[y][x]

            current_cel += 1
            output[y].append(current_cel)

    flash_count = 0

    is_find_a_puls = True
    while is_find_a_puls:
        is_find_a_puls = False

        for y in range(len(output)):
            for x in range(len(output[y])):
                current_cel = output[y][x]
                if current_cel >= 10:
                    is_find_a_puls = True
                    flash_count += 1
                    output[y][x] = 0

                    adj_pos = [
                        (-1,-1), ( 0,-1), ( 1,-1),
                        (-1, 0),          ( 1, 0),
                        (-1, 1), ( 0, 1), ( 1, 1)
                    ]
                    adj_index = [ (x+ap[0], y+ap[1]) for ap in adj_pos ]  # add pos flash.
                    adj_index = [ ai for ai in adj_index if (  # filter out of range.
                        ai[0] >= 0 and ai[0] < len(output[0]) and
                        ai[1] >= 0 and ai[1] < len(output)
                    ) ]
                    for ai in adj_index:
                        current_value_ai = output[ai[1]][ai[0]]
                        if current_value_ai == 0:
                            continue
                        output[ai[1]][ai[0]] += 1

    return (output, flash_count)



def checkFullFlash(map: list[list[str]]) -> bool:
    return sum([ sum(l) for l in map]) == 0



flash_total = 0
i = 0
while True:
    map, flash_increment = calcNewFrame(map)
    flash_total += flash_increment

    # check V2.
    if sum([ sum(l) for l in map]) == 0:
        step = i + 1
        print(f'--- all flash at : {step} ---')
        break

    #print('---------------------')
    #print('---')
    #print('\n'.join([''.join([ str(c) for c in l ]) for l in map]))

    i += 1

#print(f'total flash : {flash_total}')