import os,sys

def get_type(path:str='.'):
    if False:
        pass
    elif os.path.isfile(path):
        return 'file'
    elif os.path.isdir(path):
        return 'dir'
    elif os.path.islink(path):
        return 'link'
    elif os.path.isjunction(path):
        return 'junction'
    elif os.path.ismount(path):
        return 'mountpoint'
    elif os.path.isdevdrive(path):
        return 'drive'
    else:
        return 'unknown'

def get_size(path:str='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_size(entry.path)
    return total

def list(path:str='.'):
    result = os.listdir(path)
    result = sorted(result)
    for i in range(len(result)):
        stat = os.stat(result[i])
        result[i] = {
            'name': result[i],
            'type': get_type(result[i]),
            'size': get_size(result[i]),
            'inode': stat['st_ino'],
            'atime': stat['st_atime'],
            'mtime': stat['st_mtime'],
            'ctime': stat['st_ctime'],
            'uid': stat['st_uid'],
            'gid': stat['st_gid'],
            'stat': stat,
        }
    return result
