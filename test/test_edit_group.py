from model.group import Group
from random import randrange


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edited_name")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="header"))
#     app.group.edit_first(Group(header="edited_header"))
#
# def test_edit_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(footer="footer"))
#     app.group.edit_first(Group(footer="edited_footer"))
