from enum import Enum

class DocumentTypes(Enum):
    INVALID = 0
    PDF = 1

    def get_enumerate_by_key(key_name):
        try:
            index = DocumentTypes[key_name.upper()]
            return index
        except:
            return DocumentTypes.INVALID