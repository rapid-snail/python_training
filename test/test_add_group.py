# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step("When a group %s is added to the list" % group):
        app.group.create(group)
    with allure.step("Then a new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            def clean(group):
                return Group(id=group.id, name=group.name.strip())
            assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

