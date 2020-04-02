from model.contact import Contact
from random import randrange
import re


def test_delete_some_contact(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="firstname"))
    old_contacts = db.get_contact_list()
    random_idx = randrange(len(old_contacts))
    contact_id = old_contacts[random_idx].id
    app.contact.delete_contact_by_id(contact_id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[random_idx:random_idx+1] = []
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=re.sub(" +", " ", contact.firstname.strip()), lastname=re.sub(" +", " ", contact.lastname.strip()))
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(map(clean, app.contact.get_contact_list()), key=Contact.id_or_max)
