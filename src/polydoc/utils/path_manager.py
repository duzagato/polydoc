import os

class PathManager:
    @staticmethod
    def get_extension(path: str):
        if os.path.exists(path):
            if os.path.isfile(path):
                extension = path.split('.')[-1]

                return extension
            elif os.path.isfolder(path):
                raise ValueError('Você enviou o caminho de uma pasta. Tente enviar o caminho de um PDF.')
            else:
                raise ValueError('Ocorreu um erro ao receber o caminho enviado.')
        else:
            raise ValueError('O caminho enviado não foi encontrado.')
