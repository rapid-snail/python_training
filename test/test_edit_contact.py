from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="first name edited", middlename="middle name edited", lastname="last name edited", nickname="nickname edited", title="title edited",
                               company="company edited", address="address edited", homephone="9999999999", mobile="8888888888", workphone="5555555555", fax="333333", email="email@mail.ru",
                               email2="email2@mail.ru", email3="email3@mail.ru", homepage="http://homepage", address2="address2", phone2="2222222222", notes="notes edited"))
    app.session.logout()
