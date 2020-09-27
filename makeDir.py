import os


def makeDir(name):
    currentPath = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists('.'+name):
        os.makedirs('.'+name)
    return (currentPath+name)
