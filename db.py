from tinydb import TinyDB, Query, where


class Db:

    def __init__(self):
        self.__db = TinyDB('./db.json')
        self.__query = Query()

    def findUser(self, lastname, firstname):
        query = Query()
        const = self.__db.table("const")
        return const.search((query.lastname == lastname) & (query.firstname == firstname))

    def all(self):
        const = self.__db.table("const")
        return const.all()

    def all_random(self):
        random = self.__db.table("random")
        return random.all()

    def newuser(self, firstname, lastname, password, on, off):
        const = self.__db.table("const")
        const.insert({'firstname': firstname, 'lastname': lastname, 'password': password, 'on': on, 'off': off})

    def randomuser(self, firstname, lastname, password, on, off):
        random = self.__db.table("random")
        random.insert({'firstname': firstname, 'lastname': lastname, 'password': password, 'on': on, 'off': off})

    def droprandom(self):
        self.__db.purge_table("random")

    def update(self, firstname, lastname, state, value):
        const = self.__db.table("const")
        if state == 'on':
            const.update({'on': value},
                             ((self.__query.lastname == lastname) & (self.__query.firstname == firstname)))
        elif state == 'off':
            const.update({'off': value},
                             ((self.__query.lastname == lastname) & (self.__query.firstname == firstname)))
        elif state == 'password':
            const.update({'password': value},
                             ((self.__query.lastname == lastname) & (self.__query.firstname == firstname)))
        else:
            return 1

    def remove(self, lastname, firstname):
        const = self.__db.table("const")
        const.remove((where('lastname') == lastname) & (where('firstname') == firstname))
