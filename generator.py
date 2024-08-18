import os

from .body import folder_name, title, scripts, style_sheets, html_compressed_script
from .core import total, css_extract
from .vars import *





def write_html(targeted_file_path, folder_name, title, scripts, style_sheets, html_compressed_script, source_file_path, css_main_file=None, js_main_file=None, write_python=False, django=False, ssmt="a", scmt="a", **_):
  """
  file_path = C:/Users/pc/learning
  source = __file__[:-12]  
  """

  script = total(title, scripts, style_sheets, html_compressed_script, django)

  script = "\n".join([line for line in script.splitlines() if line.strip()])

  absolute_path_to_folder = f"{targeted_file_path}/{folder_name}"
  templates = static = ''
  if django: 
    templates = "templates/"; static = "static/"
    os.makedirs(targeted_file_path + "/templates", exist_ok=True)
    os.makedirs(targeted_file_path + "/static", exist_ok=True)
    absolute_path_to_folder = targeted_file_path
  else:
    os.makedirs(absolute_path_to_folder, exist_ok=True)

  absolute_path_to_files = absolute_path_to_folder + "/"

  with open(absolute_path_to_files + f"{templates}{title}.html", "w") as html_file:
    html_file.write(script)

  if write_python:
    with open(absolute_path_to_files + f"{title}.py", "w") as python_file:
      with open(source_file_path, "r") as python_source2:
          string2 = python_source2.read()
          python_file.write("""
  from htmlpy.block import Block
  from htmlpy.generator import write_html

  """ + '\n'.join([line for line in string2.split('\n')[2:] if "create(" not in line]) + """

  write_html(file_name, title, scripts, style_sheets, html_compressed_script)
  """ )

  if scmt:
    os.makedirs(absolute_path_to_files + f"{static}{SCRIPTS_FOLDER_NAME(title)}", exist_ok=True)
    with open(absolute_path_to_files + f"{static}{SCRIPTS_FOLDER_NAME(title)}/{js_main_file or "main"}.js", scmt) as js_file:
      js_file.write("")

  if ssmt:
    os.makedirs(absolute_path_to_files + f"{static}{STYLE_SHEET_FOLDER_NAME(title)}", exist_ok=True)
    with open(absolute_path_to_files + f"{static}{STYLE_SHEET_FOLDER_NAME(title)}/{css_main_file or "main"}.css", ssmt) as css_file:
      if not css_file.isatty(): css_file.write(css_extract(html_compressed_script))

  os.makedirs(absolute_path_to_folder + f"/{static}{IMAGES_FOLDER_NAME}", exist_ok=True)

if __name__ == "__main__":
  write_html("C:/Users/pc/learning", folder_name, title, scripts, style_sheets, html_compressed_script, __file__[:-12] + 'body.py')