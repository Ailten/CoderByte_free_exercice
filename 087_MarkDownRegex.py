
# mark down regex.
# /

# take a stirng and cast it an another string, with some patern :
# '#' in front of a line make it as <h1> title.
# '##' make it as <h2>
# '**' outer a string make it as <strong>
# '[Google](https://google.com)' make it an <a href="https://google.com">Google</a>


import re

def MarkDownRegex(document: str) -> str:

    # # -> <h1>.
    document = re.sub(r'((^|\n)# (.*)($|\n))', '\\2<h1>\\3</h1>\\4', document)
    # ## -> <h2>.
    document = re.sub(r'((^|\n)## (.*)($|\n))', '\\2<h2>\\3</h2>\\4', document)
    # ** -> <strong>.
    document = re.sub(r'\*{2}(.*)\*{2}', '<strong>\\1</strong>', document)
    # [link](url) -> <a>.
    document = re.sub(r'\[(.+)\]\((https://.+)\)', '<a href="\\2">\\1</a>', document)
    return document


print(MarkDownRegex(
    '# title\n'+
    '## sub-title\n'+
    'this is a **text strong** and it work.\n'+
    'for more details visite [this web page](https://google.com) and that\'s it.'
))