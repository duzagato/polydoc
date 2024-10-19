from polydoc.document_translation import DocumentTranslation
from polydoc.features.document import Document
from polydoc.utils.path_manager import PathManager
from polydoc.constants.translation_methods import TranslationMethods

class CommandLine:
    translation_methods__menu = {
        'Google Tradutor': TranslationMethods.GOOGLE,
        'Google Gemini': TranslationMethods.GEMINI
    }

    def init_program(self) -> None:
        print('Bem-Vindo ao Polydoc')

        while(True):
            try:
                document_translation = DocumentTranslation()

                print('Cole o caminho do arquivo que você deseja traduzir: ')
                doc_path = input('')
                
                doc = Document(doc_path)
                document_translation.document = doc
                document_translation.type = doc.get_document_type()

                translation_method = self.choose_translation_method()
                document_translation.method = translation_method

                print(document_translation.document)
                print(document_translation.type)
                print(document_translation.method)
                exit()
            except ValueError as e:
                print(str(e))
                continue

            

    def choose_translation_method(self) -> str:
        menu = Menu()
        methods = list(self.translation_methods__menu.keys())

        while(True):
            user_input = menu.create_cli_menu(self.translation_methods__menu, 'Escolha o método de tradução.')

            if user_input.isdigit():
                index = int(user_input)

                if index <= len(methods):
                    method = methods[index - 1]
                    return self.translation_methods__menu[method]
                    break
                else:
                    print('Opção inválida.')
                    continue
            else:
                if user_input in methods:
                    return self.translation_methods__menu[user_input]
                    break
                else:
                    print('Opção inválida')
                    continue

    

class Menu(CommandLine):
    def create_cli_menu(self, options: dict, message: str = None) -> None:
        self.__show_menu(options)
        user_input = input('Escolha a opção: ')
        
        return user_input
    
    def __show_message(self, message: str = None) -> None:
        if message is not None:
            print(message)
    
    def __show_menu(self, options: dict, message: str = None) -> None: 
        index = 1

        for option in options.keys():
            print(f'{index}. {option}')
            index += 1

        print('')

    def __get_options(self, user_input: str, options: dict) -> str:
        if user_input.is_numeric():
            index = int(user_input)
            options_values = list(options.values())

            if index < len(options_values):
                return options_values[index - 1]
            else:
                print('Opção inválida, tente novamente')
                return False
        else:
            if user_input in options:
                return options[user_input]
            else:
                print('Opção inválida, tente novamente')
                return False
