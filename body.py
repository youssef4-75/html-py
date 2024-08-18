from .block import Block

folder_name = "something"

title = "test"

scripts = tuple()

style_sheets = tuple()

html_compressed_script = Block("main", nested=[
    Block("header", "header", nested=[
      Block("back_button", "button", nested=[
        Block("back_icon", "img")
      ]),
      Block("toolbar")
    ]),


    Block("content", nested=[
      Block("app_image-space", nested=[
        Block("app_image", "img")
      ]),
      Block("body")
    ])

  ])

