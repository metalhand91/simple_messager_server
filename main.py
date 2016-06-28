#curl -v -d "username=world&password=pass&email=email@email.com" http://127.0.0.1:8888/register/

import tornado.web
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import User, Message


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("It's work!")
        

class RegisterHandler(tornado.web.RequestHandler):
    """
    Обработчик регистрации пользователя.
    При успешной регистрации возвращает http код 201 Created.
    Если пользователь с данным именем уже существует возвращает http 
    код 205 Reset Content.
    """
    def post(self):
        print(self.request)
        
        # Получение имени пользователя и пароля из post запроса.
        username = self.get_argument('username')
        password = self.get_argument('password')
        email = self.get_argument('email')
        print(username, password, email)
        
        # Проверка на существовние пользователя.
        if not session.query(User).filter_by(username = username)\
                .one_or_none():
            # Создание пользователя и сохранение.
            user = User(username, password, email)
            session.add(user)
            session.commit()
            print('user', username, 'with password', password, 'created')
            self.set_status(201, 'user created')
        else:
            print('user already exist')
            self.set_status(205, 'user already exist')


class LogInHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        user = session.query(User).filter_by(username = username)\
                .one_or_none()
        if user and user.password == password:
            user.set_access_token()
            print(user.access_token)
            session.commit()
            self.write(user.access_token)
        else:
            self.set_status(205, 'wrong username or password')


class LogOutHandler(tornado.web.RequestHandler):
    def get(self): #post(self):
        self.write("LogOutHandler work!")
        

class EchoHandler(tornado.web.RequestHandler):
    def post(self):
        print(self.request)
        self.write(self.request.body)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/register/", RegisterHandler),
        (r"/login/", LogInHandler),
        (r"/logout/", LogOutHandler),
        (r"/echo/", EchoHandler),
    ])


if __name__ == "__main__":
    engine = create_engine('sqlite:///simple_messeger.db')
    session = Session(bind=engine)
    print("Hello World!\nIt's alive!")
    app = make_app()
    app.listen(8888)
    print("Server started on 127.0.0.1:8888")
    tornado.ioloop.IOLoop.current().start()


