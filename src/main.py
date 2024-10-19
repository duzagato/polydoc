from time import sleep
from polydoc.document_translation import DocumentTranslation
from command_line import CommandLine

try:
    cli = CommandLine()

    cli.init_program()
except Exception as e:
    print('Erro inesperado')
    print(str(e))
    print('O programa será finalizado em 5 segundos')
    sleep(5)
    exit()