class msgWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "w")
        return self.file

    def __exit__(self, *args):
        self.file.close()

    #using with statement with MessageWriter
with msgWriter("my_file.txt") as xfile:
        xfile.Write("this is a txt file")