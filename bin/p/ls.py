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

def list(path:str='.'):
    result = os.listdir(path)
    result = sorted(result)
    for i in range(len(result)):
        result[i] = {
            'name': result[i],
            'type': get_type(result[i]),
        }
    return result
