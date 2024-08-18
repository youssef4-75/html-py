from .block import Block


def read_block(block: Block, order=2):
    tab = order*'\t'
    classes = ''.join([cls + ' ' for cls in block.classes])
    if classes: classes = " " + classes.removesuffix(" ")
    if block.name: classes = f"js-{block.name} css-{block.name}{classes}"
    if classes: classes = f" class=\"{classes}\""
    additional_attributes = ''
    for name, value in block.kwargs.items():
        additional_attributes += f' {name}="{value}"'
    opening = \
f"""{tab}<{block.type}{classes}{additional_attributes}>
{tab}\t{block.pre_text}
"""
    if not block.close_it: return opening 
    ending = f"""
{tab}\t{block.post_text}
{tab}</{block.type}>"""
    body = '\n'
    for child in block.nested:
        body += read_block(child, order+1)+'\n'
    return opening + body +  ending
