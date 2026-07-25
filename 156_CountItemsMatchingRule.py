
# count items matching a rule.
# https://leetcode.com/problems/count-items-matching-a-rule/


def func(items: list[list[str]], rule_key: str, rule_value: str) -> list[list[str]]:

    dico_type = {
        "type": 0,
        "color": 1,
        "name": 2
    }

    if not rule_key in dico_type:
        raise Exception("rule_key is not valide !")

    return [ item for item in items if item[dico_type.get(rule_key)] == rule_value ]


items = [
    ["phone","blue","pixel"],
    ["computer","silver","lenovo"],
    ["phone","gold","iphone"]
]
print(func(items, "color", "silver"))
print(func(items, "type", "phone"))
