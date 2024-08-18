from typing import Iterable

from .reader import read_block, Block
from .vars import *
from .utilities import *


def total(title, scripts: Iterable[str]|str, style_sheets: Iterable[str]|str, html_compressed_script, django):
    js = django_script(scripts, "\t<script src=\"", "\"></script>", SCRIPTS_FOLDER_NAME(title), "main.js", django_bool=django)
    # f'\t<script src="{SCRIPTS_FOLDER_NAME(title)}/main.js"></script>'
    # for script in scripts:
    #     js += f'\n\t<script src=""></script>'
    css = django_script(style_sheets, "\t\t<link rel=\"stylesheet\" href=\"", "\">", STYLE_SHEET_FOLDER_NAME(title), "main.css", django_bool=django)
    """<link rel="stylesheet" href="second_try/stylesheet/main.css">"""
    loading = "{%load static%}" if django else ""
    script = f'''
<!DOCTYPE html>
<html>
	<head>
    <title>{title}</title>
    {loading}
{css}
    </head>
    <body>
''' + \
	read_block(html_compressed_script)\
    + f'''
    </body>\n{js}
</html>'''
    return script


def css_extract(block: Block):    
    d = block.allClasses()
    f = """
:root{
    --color1: #000000;
    --color2: #000000;
    --color3: #000000;
    --height: auto;
}

body{
    margin: 0px;
    padding: 0px;
}
"""
    for classe in d:
        f += f"""

.{classe} """+"""{
    display: block;
}"""
    return f
    

def make_django(parents_block: Block):
    parents_block.img_django()
    for block in parents_block.nested:
        make_django(block)