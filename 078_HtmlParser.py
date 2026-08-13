
# HTML Parser.
# (-)

# take a string containe html, resolve it, if all html balise open and close correctly : return Ture, if not return False, But if it can be corrected by editing one balise, return the name of the balise.

import re

def htmlPars(line: str) -> bool|str:

    def is_balise_open(balise: str) -> bool:
        return not balise.startswith('</')
    
    def get_balise_name(balise: str) -> str:
        match_name = re.search(r'[a-z]{1,}', balise)
        if match_name == None:
            raise Exception(f'no name found in {balise}')
        return match_name.group(0)
    
    def is_balise_match(balise_a:str, balise_b:str) -> bool:
        return (
            is_balise_open(balise_a) and not is_balise_open(balise_b) and
            get_balise_name(balise_a) == get_balise_name(balise_b)
        )
    
    balises = re.findall(r'<[/]{0,1}[a-z]{1,}>', line)  # get list of string balises (only).

    balises_open = []
    balise_error_catch = None
    for b in balises:

        if is_balise_open(b):  # balise open.
            balises_open.append(b)
            continue

        last_balise_open = balises_open[len(balises_open) - 1]  # balise close and match last open.
        if is_balise_match(last_balise_open, b):
            balises_open.pop()
            continue

        if balise_error_catch == None:  # first error catch.
            balise_error_catch = balises_open.pop()
            continue

        return False  # second error.
    
    if balise_error_catch == None:  # all is valide.
        return True
    
    return get_balise_name(balise_error_catch)  # return the one type balise error.



print(htmlPars('<a></a>'))  # True
print(htmlPars('<a></b>'))  # "a"
print(htmlPars('<a><b></b></a>'))  # True
print(htmlPars('<a><b></c></d>'))  # False
print(htmlPars('<a><b></c><a>'))  # "b"