# makedirtree
Recreates directory structure from json file.

## Requiremenets:
[Json Parser ](https://github.com/tmdag/jsonParser)
This module is using 'jsonParser' module (wrapper on top of native python 'json'module )

## Usage:

- Create directory structure from current directory (and its children) and save structure to json file
```
$ 'tree -Jd . > folderTemplate.json'
```
- Recreate directory structure from json, starting from provided directory and project name
```
from jsonParser import JsonFile
Structures("/home/Projects/", template_file="folderTemplate.json").create("Project002")
```

# Example:
```
Each of yout projects has same directory structure:

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

And you want to create new, Project002 with same directory structure.

You can save current directory structure to file:
$ /home/Projects/Project001 >  'tree -Jd . > folderTemplate.json'

and using python, recreate this structure:
from jsonParser import JsonFile
from createDirectories import Structures
Structures("/home/Projects/", template_file="folderTemplate.json").create("Project002")
```