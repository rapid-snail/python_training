# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="first name", middlename="middle name", lastname="last name", nickname="nickname", title="title",
                                    company="company", address="address", homephone="9999999999", mobile="8888888888", workphone="5555555555", fax="333333", email="email@mail.ru",
                                    email2="email2@mail.ru", email3="email3@mail.ru", homepage="http://homepage", address2="address2", phone2="2222222222", notes="notes"))
    app.logout()

