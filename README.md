# Python 3, Linux MakeDirTree
Recreates directory structure from given json file. 

## Requiremenets:
[Json Parser ](https://github.com/tmdag/jsonParser)
This module is using 'jsonParser' module (wrapper on top of native python 'json'module )

## Usage:

- Create directory structure from current directory (and its children) and save structure to json file using built in linux command:
```
$ 'tree -Jd . > folderTemplate.json'
```
Or from Python subprocess:
```
import subprocess
data = subprocess.run(["tree", "-Jd", "/path/to/dir"], stdout=subprocess.PIPE)
print(data.stdout)
```
- Recreate directory structure from saved json file, starting from provided directory and your project name
```
from jsonParser import JsonFile
Structures("/home/Projects/", template_file="folderTemplate.json").create("Project002")
```

# Example:
```
Each of your projects has same directory structure:

$ /home/Projects/Project001 >  tree -d .
.
├── out
│   ├── folder01
│   └── folder02
├── sceneFiles
│   ├── folder01
│   │   └── backup
│   └── folder02
├── render
│   └── folder01
│       └── folder01
└── source

and you want to create a new, Project002 with same directory structure.

You can save current directory structure to file:
$ /home/Projects/Project001 >  'tree -Jd . > folderTemplate.json'

and using python, recreate this structure:
from jsonParser import JsonFile
from createDirectories import Structures
Structures("/home/Projects/", template_file="folderTemplate.json").create("Project002")
```