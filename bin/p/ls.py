import os,sys

def list(path:str='.'):
    result = os.listdir(path)
    result = sorted(result)
    return result
