import random
from model.group import Group
from model.contact import Contact


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Иван", lastname="Иванов"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Имя группы", header="Заголовок группы", footer="footer группы"))
    (is_found, contact, group) = orm.get_any_contact_group_pair_not_linked()
    if not is_found:
        app.contact.create(Contact(firstname="Иван", lastname="Иванов"))
        group = orm.get_group_list()[0]
        contact = orm.get_contacts_not_in_group(group)[0]
    app.contact.add_contact_to_group(contact, group)
    assert contact in orm.get_contacts_in_group(group)
