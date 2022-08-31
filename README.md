
# Dadata.ru Console application

### Тестовое Задание
Консольное приложение для доступа к адресам API Dadata
https://dadata.ru/api/clean/address/

+ Python 3
+ SQLite

## Как запустить приложение:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/sfkan6/ConsoleAppDadata.git
```

```
cd ConsoleAppDadata
```

Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```

```
source venv/Scripts/activate
```

или

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Через терминал или консоль запустить приложение:
```
python app.py
```
<hr>

Поиск адресов

<hr>

Для работы с Dadata.ru Console application вам понадобится
API_KEY, SECRET_KEY которые вы можете получить на офицальном сайте
https://dadata.ru/

<hr>

Для начала Войдите или Зарегистрируйтесь

Введите адрес и выберите нужный вариант если их несколько,
Система вернёт широту и долготу.        

<hr>

В любом месте ввода доступна команда 
завершения **exit** и вывод информации **help**,
после входа доступны команды:
+ **swap** (смена API-ключа и Секретного ключа)
+ **...** (Для поиска вместо точек введите адрес)
+ **en** (Введите 'en' чтобы ответ возвращался на английском языке и 
'ru' чтобы на русском.)  

<hr>

На ОС Windows тестирование не проводилось

## License
[MIT](https://choosealicense.com/licenses/mit/)
