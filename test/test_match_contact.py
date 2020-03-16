from random import randrange
from model.contact import Contact
import re


def test_home_page_contact_info_matches_edit_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="first name", middlename="middle name", lastname="last name", nickname="nickname", title="title",
                               company="company", address="address", homephone="9999999999", mobile="8888888888", workphone="5555555555", fax="333333", email="email@mail.ru",
                               email2="email2@mail.ru", email3="email3@mail.ru", homepage="http://homepage", address2="address2", phone2="2222222222", notes="notes"))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None and x != "",
                                   [contact.email, contact.email2, contact.email3]))
