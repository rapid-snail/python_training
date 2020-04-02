from random import randrange
from model.contact import Contact
import re


def test_edit_firstname(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="firstname"))
    old_contacts = db.get_contact_list()
    random_idx = randrange(len(old_contacts))
    contact_to_edit = old_contacts[random_idx]
    contact = Contact(firstname="first name edited")
    contact.id = contact_to_edit.id
    contact.lastname = contact_to_edit.lastname
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[random_idx] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=re.sub(" +", " ", contact.firstname.strip()), lastname=re.sub(" +", " ", contact.lastname.strip()))
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(map(clean, app.contact.get_contact_list()), key=Contact.id_or_max)


# def test_edit_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(lastname="lasttname"))
#     app.contact.edit_first(Contact(lastname="last name edited"))
