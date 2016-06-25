Simple messager server on tornado with SQLAlchemy and sqlite3.
Yet another helloworld project.


Уствновка и запуск:

Для запуска сервера должен быть установлен python 3.5 и sqlite3.

Для установки зависимых пакетов войдите в директорию с проектом и выполните:
pip3 install -r requirements.txt

или установите пакеты из файла requirements.txt вручную.

Для инциализации тестовыой базы данных выполните в директории с проектом:
python3 models.py

Для запуска сервера выполните в директории с проектом:
python3 main.py

Для проверки работы сервера вы можете отправить post запрос на http://root:8888/echo/
где root - ip машины на которой запущен сервер.
Например с помощью cURL:
curl -v -d "someparametr1=somevalue1&someparametr2=somevalue2" http://127.0.0.1:8888/echo/

сервер вернет тело запроса someparametr1=somevalue1&someparametr2=somevalue2.


