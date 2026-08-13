
# mergeDublon
# /

# take a list of object, {id: value:}, and return a list of same object, but merge object who has the same id, by adding their values.


def mergeDublon(data: list[dict]) -> list[dict]:

    output = dict()

    for current_data in data:
        current_id = current_data['id']
        current_value = current_data['value']

        if current_id in output:
            output[current_id] += current_value
            continue
        output[current_id] = current_value

    return [ { 'id': k, 'value': v } for k,v in output.items() ]
    


print(mergeDublon([
    {'id': 1, 'value': 1},
    {'id': 2, 'value': 1},
    {'id': 2, 'value': 1},
    {'id': 3, 'value': 3}
]))