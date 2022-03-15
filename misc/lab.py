directory_structure = {
    'root' : ['bin','usr','boot', 'etc'],
    'bin' : ['firefox', 'git', 'chrome'],
    'usr' : ['share', 'local'],
    'boot' : ['efi', 'grub'],
    'etc' : ['flatpack', 'dconf'],
}

def BFS(directory_structure, directory):
    visited = []
    queue = []
    queue.append(directory)
    visited.append(directory)

    while queue:
        dr = queue.pop(0) 
        print ("-",dr)
        if dr in directory_structure:
            for sub_dir in directory_structure[dr]:
                if sub_dir not in visited:
                    visited.append(sub_dir)
                    queue.append(sub_dir)

print("All Directories")
BFS(directory_structure, 'root')
