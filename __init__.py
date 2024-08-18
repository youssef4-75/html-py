"""

This module can be used with Django or as a standalone tool.
It helps you get started quickly by automating repetitive tasks.
However, be aware that this module primarily opens new files or
edits existing ones, translating your Python code into HTML.
Characters that cannot be written, such as Arabic letters or emojis,
will break your code. Therefore, avoid using such characters unless
you can handle the resulting issues.

Feel free to modify this project as needed.

You can use the create function defined below or directly use write_html
if you have different argument names.it

Note: The create function has a limitation: it requires variables to be
defined within a single line. Otherwise, the variable is ignored, and
you need to pass it manually to the function.
"""

from .generator import write_html


def create(file_path, **kwargs):
    """the file should contain a definition of:
    file_name
    title
    scripts
    style_sheets
    html_compressed_script

    stop reading if `exit` is faced in a line

    better to have this structure: 
        from htmlpy.block import Block
        from htmlpy import create
        # from htmlpy.core import make_django  # optional, if you want to make a django project

        ـ
        targeted_file_path = ...  # path to folder (/ excluded) object Immutable {the folder path you want to create the project in} 
        ـ
        source_file_path = ...  # path to file (.smt included) object Immutable  {usely, it is the current file path}
        ـ
        foldere_name = ...  # str Immutable  {the folder you want to create name}
        ـ
        title = ...  # str Immutable  {the title of the project, the name of the html file to create}
        ـ
        scripts = ...  # tuple[str] Mutable  {scripts to include in the project}
        ـ
        style_sheets = ...  # tuple[str] Mutable  {style sheets to include in the project}
        ـ
        ssmt = ""  # str Mutable {the style sheet modification method, can be either w to rewrite the style sheet, a to add to it, or stay empty to not modify it at all, any other values may raise an error}
        ـ
        scmt = ""  # str Mutable {the script modification method, can be either w to rewrite the style sheet, a to add to it, or stay empty to not modify it at all, any other values may raise an error}
        ـ
        django = True  # bool Immutable {if True, the project will be written as a Django project, otherwise it will be written as a normal html project}
        ـ
        write_python = False  # bool Mutable {if True, a python generator file like the source will be written}
        ـ
        html_compressed_script = ...  # Block[...] Mutable  {the html file written in my own language}
        ـ
        # make_django(html_compressed_script)  # optional made if you want to make a django project
        ـ

        create(__file__)

    """
    with open(file_path, 'r') as f: 
        content = f.readlines()
        for line in content:
            if 'exit' in line: break
            if '=' not in line:continue
            try:
                key, value = line.split('=')
                kwargs[key.strip()] = eval(value)
            except (ValueError, SyntaxError, NameError): continue
        
        write_html(**kwargs)
