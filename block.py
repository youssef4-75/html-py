from .vars import IMAGES_FOLDER_NAME
from Haddadi_lib.tree import Tree
from .utilities import decide_path_formula


class Block:
  def __init__(self, name_, type_='div', pre_text: str = '',post_text: str='',
      classes: tuple[str]=tuple(), rows_taken: int=1,
      columns_taken: int=1, nested=None, closing_tag=True, *,
      editable=False, **kwargs):
    
    if editable: pre_text = "{% block "+name_+"%}" + pre_text; post_text += "{% endblock %}"
    self.name = name_
    self.nested = nested or []
    self.type = type_
    self.pre_text = pre_text
    self.post_text = post_text
    
    if isinstance(classes, str): classes = tuple(classes.split(' '))
    self.classes = classes
    self.rows = rows_taken
    self.columns = columns_taken
    self.close_it = closing_tag
    self.kwargs = kwargs
    match self.type:
      case "button":
        self.kwargs["onclick"] = f"func_{kwargs.get("click", self.name)}()"
      case "img":
        self.close_it = False
        self.kwargs["src"] = f"{IMAGES_FOLDER_NAME}/{kwargs.get("img_source", self.name)}.png"


  @staticmethod
  def __dest(main, type_: str, separator='/', group='{}', *, start: int) -> tuple[Tree, int]:
    type_ = type_.replace(group[1] + separator, group[1])
    if not type_.endswith(separator): type_ += separator
    A = Tree(main, [])
    current = ''
    while True:
      try:f = type_[start]
      except: print(start, len(type_), '\n', A); return
      if f == separator:
        A.insert(Tree(current))
        current = ''
      elif f == group[0]:
        tree, start = Block.__dest(current, type_, separator, group, start=start+1)
        A.insert(tree)
        current = ''
      elif f == group[1]:
        return A, start
      else:current += f
      start += 1

  def add_property_to_type(self, property, value, type):
    if self.type == type: setattr(self, property, value)

  def img_django(self): 
    if "src" in self.kwargs: self.kwargs["src"] = "{% static '"+ self.kwargs["src"] +"'%}"

  @classmethod
  def from_tree(cls, A: Tree):
    nested = [cls.from_tree(a) for a in A.des]
    return cls('', type_=A.node, nested=nested)

  @classmethod
  def destructure(cls, type_: str, separator='/', group='{}'):
    main, type_ = type_.split(separator, 1)
    A, _ = cls.__dest(main, type_, separator, group, start=0)
    return cls.from_tree(A).nested
  
  def modify(self, *, name='', pre_text: str = '',post_text: str='',
      classes: tuple[str]=tuple(), rows_taken: int=1,
      columns_taken: int=1, nested=None, closing_tag=True, **kwargs):
    self.name = name or self.name
    self.nested = nested or self.nested
    self.pre_text = pre_text or self.pre_text
    self.post_text = post_text or self.post_text
    
    if isinstance(classes, str): classes = tuple(classes.split(' '))
    self.classes = classes or self.classes 
    self.rows = rows_taken or self.rows
    self.columns = columns_taken or self.columns
    self.close_it = closing_tag or self.close_it
    self.kwargs.update(kwargs)

  def allClasses(self):
    Lcls = []
    [Lcls.append(i) for i in self.classes if i not in Lcls]
    if self.name: _ = Lcls.append(f"css-{self.name}") if f"css-{self.name}" not in Lcls else None
    for child in self.nested:
      [Lcls.append(i) for i in child.allClasses() if i not in Lcls]
    for obj in ('', ' '):
      while obj in Lcls:
        Lcls.remove(obj)
    return Lcls





