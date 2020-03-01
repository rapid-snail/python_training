from model.contact import Contact


def test_edit_firstname(app):
    app.contact.edit_first(Contact(firstname="first name edited"))

def test_edit_lastname(app):
    app.contact.edit_first(Contact(lastname="last name edited"))
