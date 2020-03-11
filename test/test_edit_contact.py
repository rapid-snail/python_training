from random import randrange
from model.contact import Contact


def test_edit_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="first name edited")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(lastname="lasttname"))
#     app.contact.edit_first(Contact(lastname="last name edited"))
