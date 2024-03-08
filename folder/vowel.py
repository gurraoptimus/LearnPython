# a simple file writer object

class MsgWriter(object):
	def __init__(self, file_name):
		self.file_name = file_name
	
	def __enter__(self):
		self.file = open(self.file_name, 'w')
		return self.file

	def __exit__(self, *args):
		self.file.close()

# using with statement with MessageWriter

with MsgWriter('my_file.md') as xfile:
	xfile.write('# hello world')
