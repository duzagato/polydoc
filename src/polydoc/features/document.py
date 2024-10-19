from polydoc.utils.path_manager import PathManager
from polydoc.constants.document_types import DocumentTypes

class Document:
    def __init__(self, path: str) -> None:
        extension = PathManager.get_extension(path)
        document_type = DocumentTypes.get_enumerate_by_key(extension)

        if document_type != DocumentTypes.INVALID:
            self.__document_type = document_type
        else:
            raise ValueError('Não possuimos suporte a extensão do arquivo enviado.')

    def get_document_type(self) -> DocumentTypes:
        return self.__document_type