Python 3, Linux MakeDirTree
==============
![VFX Pipeline](https://img.shields.io/badge/VFX%20Pipeline-2018-lightgrey.svg?style=flat)
![python v3.6](https://img.shields.io/badge/Python-3.6-blue.svg?style=flat)
![pylint Score](https://mperlet.github.io/pybadge/badges/9.44.svg)

GitHub: https://github.com/tmdag/makedirtree

## Overview
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

PROJECTS_PARENT_DIR = "/home/Projects/"
STRUCTURE_TEMPLATE_FILE = "/config/folderTemplate.json"
NEW_PROJECT_NAME = "Project002"

dir_structure = SetupTree(PROJECTS_PARENT_DIR, template_file=STRUCTURE_TEMPLATE_FILE)
# dir_structure.test_structure(NEW_PROJECT_NAME)
dir_structure.create_new_project(NEW_PROJECT_NAME)

```

