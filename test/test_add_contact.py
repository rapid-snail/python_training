# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random


def gen_str(symbols, max_len):
    return "".join([random.choice(symbols) for _ in range(random.randrange(max_len))])


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + gen_str(symbols, max_len)


def rand_email(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return "%s%s@%s.%s" % (prefix, gen_str(symbols, max_len), gen_str(symbols, max_len), gen_str(symbols, max_len))


def rand_phone(prefix, max_len):
    symbols = string.digits + " " + "+" + "-" + "(" + ")"
    return prefix + gen_str(symbols, max_len)


test_data = [
    Contact(firstname="", middlename="", lastname="", nickname="", title="",
                               company="", address="", homephone="", mobile="", workphone="", fax="", email="",
                               email2="", email3="", homepage="", address2="", phone2="", notes="")
] + [
    Contact(firstname=random_string("fn", 20), middlename=random_string("mn", 20), lastname=random_string("ln", 20),
            nickname=random_string("nick", 20), title=random_string("title", 50), company=random_string("comp", 50),
            address=random_string("addr", 100), homephone=rand_phone("", 20), mobile=rand_phone("+", 20),
            workphone=rand_phone("", 20), fax=random_string("", 20), email=rand_email("e1", 15),
            email2=rand_email("e2", 15), email3=rand_email("e3", 15), homepage=random_string("http", 30),
            address2=random_string("addr2", 100), phone2=rand_phone("", 20), notes=random_string("note", 100))
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
