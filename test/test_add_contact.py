# -*- coding: utf-8 -*-
from model.contact import Contact
import re


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=re.sub(" +", " ", contact.firstname.strip()), lastname=re.sub(" +", " ", contact.lastname.strip()))
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(map(clean, app.contact.get_contact_list()), key=Contact.id_or_max)

