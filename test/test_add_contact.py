# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first name", middlename="middle name", lastname="last name", nickname="nickname", title="title",
                               company="company", address="address", homephone="9999999999", mobile="8888888888", workphone="5555555555", fax="333333", email="email@mail.ru",
                               email2="email2@mail.ru", email3="email3@mail.ru", homepage="http://homepage", address2="address2", phone2="2222222222", notes="notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
