import os
import re

class treatingTheFile:

    def __init__(self, path, module):
        self.path = path
        self.module = module
    
    def creatingRouteFile(self):
        currentPath = os.getcwd() + '/'
        os.chdir(self.path)
        os.system('adonis route:list > {}'.format(currentPath + self.module + '.txt'))

        return os.chdir(currentPath)

    def getRoutes(self):
        pass
