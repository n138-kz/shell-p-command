import os,sys

if len(sys.argv) == 0:
    sys.exit(0)

if __name__ != '__main__':
    sys.exit(0)

if False:
    pass
elif sys.argv[1] == 'ls':
    from p import ls
