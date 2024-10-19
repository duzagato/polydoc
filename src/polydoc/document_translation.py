from polydoc.constants.translation_methods import TranslationMethods
from polydoc.constants.document_types import DocumentTypes
from polydoc.features.document import Document

class DocumentTranslation:
    def __init__(self) -> None:
        self.document: Document
        self.type: DocumentTypes
        self.method: TranslationMethods