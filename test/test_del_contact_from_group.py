import random
from model.group import Group
from model.contact import Contact


def test_del_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    if len(orm.get_all_contacts_in_groups()) == 0:
        groups = orm.get_group_list()
        group = random.choice(groups)
        contacts = orm.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact, group)
    else:
        contacts = orm.get_all_contacts_in_groups()
        contact = random.choice(contacts)
        groups = orm.get_groups_by_contact(contact)
        group = random.choice(groups)
    app.contact.delete_contact_from_group(contact, group)
    assert contact not in orm.get_contacts_in_group(group)
