import os

def print_tree(startpath, exclude=None, prefix=""):
    if exclude is None:
        exclude = []

    items = sorted(os.listdir(startpath))
    items = [item for item in items if item not in exclude]  # excluye carpetas/archivos
    
    for index, item in enumerate(items):
        path = os.path.join(startpath, item)
        connector = "├── " if index < len(items) - 1 else "└── "
        print(prefix + connector + item)
        
        if os.path.isdir(path) and item not in exclude:
            new_prefix = prefix + ("│   " if index < len(items) - 1 else "    ")
            print_tree(path, exclude, new_prefix)


if __name__ == "__main__":
    # Carpeta raíz desde donde empezar
    root_dir = "."
    
    # Directorios a ignorar
    exclude_dirs = ["venv", "__pycache__", ".git"]
    
    print(root_dir)
    print_tree(root_dir, exclude_dirs)
