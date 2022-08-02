import argparse
import sys
import textwrap

from ConsoleApp import Input, Output, ToApiDadata


class App:
    def __init__(self):
        self.entry = Input()
        self.output = Output()
        self.dadata = ToApiDadata(self.entry, self.output)

    def help(self):
        print(info)

    def console_command(self, query):
        if query.lower() == 'exit':
            sys.exit(0)
        elif query.lower() == 'help':
            self.help()
            return 'continue'
        elif query.lower() == 'swap':
            self.dadata.change_profile()
            return 'continue'
        elif self.dadata.change_language(query):
            return 'continue'

    def run(self):
        self.output.hello()
        while True:
            query = self.entry.entry()
            if self.console_command(query) == 'continue':
                continue
            self.dadata.search_address(query)


if __name__ == '__main__':
    name = 'Dadata.ru Console application'
    info = '''

    Поиск адресов
    _________________________________________________________
    Для работы с Dadata.ru Console application вам понадобится
    API_KEY, SECRET_KEY которые вы можете получить на офицальном сайте
    https://dadata.ru/
    _________________________________________________________
    Для начала Войдите или Зарегистрируйтесь

    Введите адрес и выберите нужный вариант если их несколько,
    Система вернёт широту и долготу.        
    _________________________________________________________
    В любом месте ввода доступна команда 
    завершения exit и вывод информации help,
    после входа доступны команды:
        swap (смена API-ключа и Секретного ключа)
        ... (Для поиска вместо точек введите адрес)
    _________________________________________________________
    Введите 'en' чтобы ответ возвращался на английском языке и 
    'ru' чтобы на русском.
    _________________________________________________________
    '''

    parser = argparse.ArgumentParser(
        description=name,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(info))
    parser = parser.parse_args()

    app = App()
    app.run()
