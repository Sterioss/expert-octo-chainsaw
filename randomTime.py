from db import Db
import random
from datetime import datetime, timedelta


class RandomTime:
    db = Db()

    def getdbvalues(self):
        return self.db.all()

    def randomizer(self):
        self.db.droprandom()
        for user in self.getdbvalues():
            on = datetime.strptime(user['on'], "%H:%M")
            on += timedelta(minutes=random.randint(0, 10))
            off = datetime.strptime(user['off'], "%H:%M")
            off -= timedelta(minutes=random.randint(0, 10))
            self.db.randomuser(user['firstname'], user['lastname'], user['password'], on.strftime("%H:%M"),
                               off.strftime("%H:%M"))
