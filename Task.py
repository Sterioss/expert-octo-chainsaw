from badger import Badger
import time

class Task:
    def __init__(self, on, off, firstname, lastname):
        self.on = on
        self.off = off
        self.firstname = firstname
        self.lastname = lastname

    def __seton(self, firstname, lastname):
        onbadger = Badger(firstname, lastname)
        return onbadger.setpresence(1)

    def __setoff(self, firstname, lastname):
        offbadger = Badger(firstname, lastname)
        return offbadger.setpresence(0)

    def start(self):
        if time.strftime("%H:%M") == self.on:
            self.__seton(self.firstname, self.lastname)
