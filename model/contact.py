from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobile=None, workphone=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None, address2=None, phone2=None, notes=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.firstname == other.firstname and self.lastname == other.lastname

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
