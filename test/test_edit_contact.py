from model.contact import Contact


def test_edit_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    app.contact.edit_first(Contact(firstname="first name edited"))

def test_edit_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="lasttname"))
    app.contact.edit_first(Contact(lastname="last name edited"))
