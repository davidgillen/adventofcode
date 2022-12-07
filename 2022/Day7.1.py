#import sys
#sys.setrecursionlimit(5000)
folders = {}

class File:
    name = ''
    size = ''

class Folder:
    path = ''
    parentPath = '' 
    subs = []
    files = {}
    name = ''
    size = 0

    def __init__(self, parentPath, name):
        self.path = parentPath + name
        self.parentPath = parentPath
        self.name = name
    
    def addsub(self, subname):
        global folders
        print('New folder ' + subname)
        folders[self.path + subname] = Folder(self.path, subname)
        print(folders.keys())
        self.subs.append( subname )

    def addFile(self, name, size):
        self.files[name] = size
        self.addSize(size)

    def addSize(self, size):
        self.size += size
        if self.name != '/':
            folders[self.parentPath].addSize(size)


#fp = open('test7.txt')
fp = open('input7.txt')
lines = fp.readlines()
root = Folder('', '/')
folders['/'] = root
currentFolder = '/'
for line in lines:
    if line[0:3] == 'dir':
        xxx, foldername = line.strip().split(' ')
        folders[currentFolder].addsub(foldername)
    elif line[0].isdigit():
        size, filename = line.strip().split(' ')
        folders[currentFolder].addFile(filename, int(size))
    else: # Process command
        print(line[2:4])
        if line[2:4] == 'ls':
            print('LS so skipping')
            next
        elif line[2:4] == 'cd':
            prompt, cmd, arg = line.strip().split(' ')
            print('Changing to ' + arg )
            if arg == '/':
                currentFolder = '/'
            elif arg == '..':
                currentFolder = folders[currentFolder].path[0:-len(folders[currentFolder].name)]
            else:
                currentFolder = folders[currentFolder].path + arg

print(folders.keys())

totalSize = 0
for key in folders.keys():
    if folders[key].size <= 100000:
        totalSize += folders[key].size

print(totalSize)