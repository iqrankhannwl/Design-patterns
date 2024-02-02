class XmlImporter:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def execute(self):
        print(f"XML import from {self.file_name}")