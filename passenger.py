class Passenger:

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, name):
        self._first = name

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        self._last = last

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def yell_name(self):
        return self._first.upper() +" " + self._last.upper()
