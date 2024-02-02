from json_importer import JsonImporter
from xml_importer import XmlImporter

class ImporterFactory:

    def get_importer(self, file_name):
        importer = self.create_importer(file_name)
        return importer


class XmlImporterFactory(ImporterFactory):

    def create_importer(self, file_name):
        xml_importer = XmlImporter(file_name)
        return xml_importer


class JsonImporterFactory(ImporterFactory):

    def create_importer(self, file_name):
        json_importer = JsonImporter(file_name)
        return json_importer


class Document:
    
    def __init__(self, impoter_factory):
        self.importer_factory = impoter_factory

    def import_file(self,file_name):
        importer = self.importer_factory.get_importer(file_name)
        data = importer.execute()

xml_import_factory = XmlImporterFactory()
document1 = Document(xml_import_factory)
document1.import_file("text.xml")