
def decide_path_formula(path, django):
        if not django: return path
        return "{% static '"+path+"'%}"

def django_script(paths_family, before, after, folder_family, default_path= None, *, django_bool=False):
    if isinstance(paths_family, str): paths_family = tuple(paths_family.split(' '))
    res = before + decide_path_formula(folder_family+ '/' + default_path, django_bool) + after + '\n' if default_path else ''
    for path in paths_family:
        res += before + decide_path_formula(folder_family+ '/' + path, django_bool) + after + '\n'
    if res: res = res[:-1]
    return res 
