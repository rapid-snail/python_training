from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name"))
    old_groups = db.get_group_list()
    random_idx = random.randrange(len(old_groups))
    group_to_edit = old_groups[random_idx]
    group = Group(name="edited_name")
    group.id = group_to_edit.id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[random_idx] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="header"))
#     app.group.edit_first(Group(header="edited_header"))
#
# def test_edit_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(footer="footer"))
#     app.group.edit_first(Group(footer="edited_footer"))
