import os,sys

def list(path:str='.'):
    result = os.listdir(path)
    result = sorted(result)
    for i in range(len(result)):
        result[i] = {
            'name': result[i],
        }
    return result
