from tinydb import TinyDB, Query, where


class Db:

    def __init__(self):
        self.__db = TinyDB('./db.json')
        self.__query = Query()

    def findUser(self, lastname, firstname):
        query = Query()
        return self.__db.search((query.lastname == lastname) & (query.firstname == firstname))

    def all(self):
        return self.__db.all()

    def newuser(self, firstname, lastname, password, on, off):
        self.__db.insert({'firstname': firstname, 'lastname': lastname, 'password': password, 'on': on, 'off': off})

    def update(self, firstname, lastname, state, value):
        if state == 'on':
            self.__db.update({'on': value},
                             ((self.__query.lastname == lastname) & (self.__query.firstname == firstname)))
        elif state == 'off':
            self.__db.update({'off': value},
                             ((self.__query.lastname == lastname) & (self.__query.firstname == firstname)))
        elif state == 'password':
            self.__db.update({'password': value},
                             ((self.__query.lastname == lastname) & (self.__query.firstname == firstname)))
        else:
            return 1

    def remove(self, lastname, firstname):
        self.__db.remove((where('lastname') == lastname) & (where('firstname') == firstname))
