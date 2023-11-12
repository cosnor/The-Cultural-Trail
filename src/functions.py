def filter(word): 
    words = word.split()
    # Unir las palabras con un solo espacio entre ellas
    name = ' '.join(words)

    return name

def is_in_panel(name, panels): 
    for panel in panels:
        if panel.name == name:
            return True
    return False