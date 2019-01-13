from sys import maxsize

class Contact:
      def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                   hometelephone=None, mobiletelephone=None, worktelephone=None, faxtelephone=None,
                   email=None, homepage=None, ayear=None, phone2=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.hometelephone = hometelephone
        self.mobiletelephone = mobiletelephone
        self.worktelephone = worktelephone
        self.faxtelephone = faxtelephone
        self.email = email
        self.homepage = homepage
        self.ayear = ayear
        self.phone2 = phone2
        self.id = id

      def __repr__(self):
        return "%s:%s" % (self.id, self.name)

      def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

      def id_or_max(self):
        if self.id:
          return int(self.id)
        else:
          return maxsize