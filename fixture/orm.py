from pony.orm import *
from model.group import Group
from model.contact import Contact
#from pymysql.converters import decoders
#from datetime import datetime


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        #deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        #self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        #return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if orm_group not in c.groups))

    @db_session
    def get_groups_by_contact(self, contact):
        orm_contact = list(select(c for c in ORMFixture.ORMContact if c.id == contact.id))[0]
        return self.convert_groups_to_model(orm_contact.groups)

    @db_session
    def get_all_contacts_in_groups(self):
        groups = self.get_group_list()
        all_contacts = []
        for group in groups:
            contacts = self.get_contacts_in_group(group)
            if len(contacts) > 0:
                for contact in contacts:
                    all_contacts.append(contact)
        return all_contacts

    @db_session
    def get_any_contact_group_pair_not_linked(self):
        groups = self.get_group_list()
        for g in groups:
            contacts = self.get_contacts_not_in_group(g)
            if len(contacts) > 0:
                contact = contacts[0]
                group = g
                return (True, contact, group)
        return (False, None, None)
