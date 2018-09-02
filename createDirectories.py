import pathlib

# Create directory tree template with
# 'tree -Jd . > folderTemplate.json'

class ExtractStructure:
	def __init__(self, directory):
		self.dir_structure = ""
		self.temp_directory = directory;

	def crawler(self, directory, parent=""):
		if directory['type']=='directory':
			parent += directory['name'] + "/"
			if len(directory['contents'])>0:
				for i in range(len(directory['contents'])):
					self.crawler(directory['contents'][i], parent=parent)
			else:
				self.dir_structure += parent + ","

		elif directory['type']=='file':
			if(parent not in self.dir_structure):
				self.dir_structure += parent + ","
			# self.dir_structure += parent+directory['name']+"," # Include Files

	def aslist(self):
		self.crawler(self.temp_directory)
		self.dir_structure = sorted(self.dir_structure[:-1].split(","))
		return self.dir_structure

class Structures:
	def __init__(self, initial_dir, template_file="folderTemplate.json"):
		self.init_dir = initial_dir
		self.template = JsonFile(template_file).load()
		self.structure = ExtractStructure(self.template[0]).aslist()

	def create(self, project_name):
		for p in self.structure:
			s_path = self.init_dir + project_name + p[1:]
			# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
			pathlib.Path(s_path).mkdir(parents=True, exist_ok=True) 
			print(s_path)

if __name__ == '__main__':
	from jsonParser import JsonFile
	Structures("/jobs/LIBRARY/HDR/", template_file="folderTemplate.json").create("HDR004")