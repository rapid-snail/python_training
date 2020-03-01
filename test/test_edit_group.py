from model.group import Group


def test_edit_group_name(app):
    app.group.edit_first(Group(name="edited_name"))

def test_edit_group_header(app):
    app.group.edit_first(Group(header="edited_header"))

def test_edit_group_footer(app):
    app.group.edit_first(Group(footer="edited_footer"))
