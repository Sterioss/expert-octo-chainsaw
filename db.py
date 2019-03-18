from tinydb import TinyDB, Query


class Db:

    def __init__(self):
        self.__db = TinyDB('./db.json').table('badger')


    def findfirst(self, firstname):
        query = Query()
        return self.__db.search(query.firstname == firstname)


    def all(self):
        return self.__db.all()

    def newuser(self, firstname, lastname, on, off):
        self.__db.insert({'firstname': firstname, 'lastname': lastname, 'on': on, 'off': off})

    def update(self, firstname, lastname, on, off):
        query = Query()
        user = self.__db.search((query.firstname == firstname) & (query.lastname == lastname))
        if on is not None:
            for usr in user:
                usr['on'] = on
            self.__db.write_back(user)
        if off is not None:
            for usr in user:
                usr['off'] = off
            self.__db.write_back(user)

    def remove(self, firstname, lastname):
        query = Query()
        user = self.__db.search((query.firstname == firstname) & (query.lastname == lastname))
        self.__db.remove(user)
