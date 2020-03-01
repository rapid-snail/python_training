from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name"))
    app.group.edit_first(Group(name="edited_name"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="header"))
    app.group.edit_first(Group(header="edited_header"))

def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="footer"))
    app.group.edit_first(Group(footer="edited_footer"))
