"""
Python 3, Linux script to re-create directory structure based on json file
Create directory tree template with
'tree -Jd . > folderTemplate.json'
"""
import pathlib
import os

class ExtractStructure:
    """ Class that creates list of directories from json file """
    def __init__(self, directory):
        """ initialize global variables """
        self.dir_structure = ""
        self.temp_directory = directory

    def crawler(self, directory, parent=""):
        """ crawl through json file and re-create directories """
        if directory['type'] == 'directory':
            parent += directory['name'] + "/"
            number_of_directories = len(directory['contents'])
            if number_of_directories > 0:
                for i in range(len(directory['contents'])):
                    self.crawler(directory['contents'][i], parent=parent)
            else:
                self.dir_structure += parent + ","

        elif directory['type'] == 'file':
            if parent not in self.dir_structure:
                self.dir_structure += parent + ","
            # self.dir_structure += parent+directory['name']+"," # Include Files

    def aslist(self):
        """ return structure as a sorted list """
        self.crawler(self.temp_directory)
        self.dir_structure = sorted(self.dir_structure[:-1].split(","))
        return self.dir_structure

class Structure:
    """ Main working class to re-create folder structure """
    def __init__(self, initial_dir, template_file="folderTemplate.json"):
        """ check if file exists, load json file and extract directories from it """
        self.init_dir = initial_dir
        if not os.path.isfile(template_file):
            raise Exception('file {0} not found\n'.format(template_file))
        self.template = JsonFile(template_file).load()
        self.structure = ExtractStructure(self.template[0]).aslist()

    def create(self, project_name):
        """ Create directory for every line in a list of directories """
        for single_path in self.structure:
            s_path = self.init_dir + project_name + single_path[1:]
            # https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
            pathlib.Path(s_path).mkdir(parents=True, exist_ok=True)
            print(s_path)

if __name__ == '__main__':
    from jsonParser.jsonParser import JsonFile
    Structure("/home/Projects/", template_file="folderTemplate.json").create("Project002")