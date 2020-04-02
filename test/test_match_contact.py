#from random import randrange
from model.contact import Contact
import re


# def test_home_page_contact_info_matches_edit_page(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="first name", middlename="middle name", lastname="last name", nickname="nickname", title="title",
#                                company="company", address="address", homephone="9999999999", mobile="8888888888", workphone="5555555555", fax="333333", email="email@mail.ru",
#                                email2="email2@mail.ru", email3="email3@mail.ru", homepage="http://homepage", address2="address2", phone2="2222222222", notes="notes"))
#     index = randrange(app.contact.count())
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[-() ./]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None and x != "",
                                   [contact.email, contact.email2, contact.email3]))


def clear_extra_blanks(s):
    return re.sub(" +", " ", s.strip())


def test_home_page_contacts_matches_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="first name", middlename="middle name", lastname="last name", nickname="nickname", title="title",
                               company="company", address="address", homephone="9999999999", mobile="8888888888", workphone="5555555555", fax="333333", email="email@mail.ru",
                               email2="email2@mail.ru", email3="email3@mail.ru", homepage="http://homepage", address2="address2", phone2="2222222222", notes="notes"))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[i].id == contacts_from_db[i].id
        assert clear_extra_blanks(contacts_from_home_page[i].firstname) == clear_extra_blanks(contacts_from_db[i].firstname)
        assert clear_extra_blanks(contacts_from_home_page[i].lastname) == clear_extra_blanks(
            contacts_from_db[i].lastname)
        assert clear_extra_blanks(contacts_from_home_page[i].address) == clear_extra_blanks(
            contacts_from_db[i].address)
        assert contacts_from_home_page[i].all_phones_from_homepage == merge_phones_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_emails_from_homepage == merge_emails_like_on_home_page(contacts_from_db[i])
