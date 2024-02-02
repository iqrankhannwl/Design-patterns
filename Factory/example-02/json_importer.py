class JsonImporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        print(f"Json import from {self.file_name}")