from sys import maxsize

class Contact:
      def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                   hometelephone=None, mobiletelephone=None, worktelephone=None, faxtelephone=None,
                   email=None, email2=None, email3=None, homepage=None, ayear=None, phone2=None, id=None,
                   all_phones_from_home_page=None, address=None, all_emails_from_home_page=None):
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
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.ayear = ayear
        self.phone2 = phone2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.address = address

      def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

      def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

      def id_or_max(self):
          if self.id:
            return int(self.id)
          else:
            return maxsize