from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="edited_name", header="edited_header", footer="edited_footer"))
    app.session.logout()
