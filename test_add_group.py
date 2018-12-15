# -*- coding: utf-8 -*-
import pytest

from group import Group
from application import Application

@pytest.fixture
def app(request):
    #иницилизация фикстуры
    fixture = Application()
    #для разрушения фикстуры
    request.addfinalizer(fixture.destroy)
    return fixture

#тестовый метод принимающий в качестве параметра фикстуру
def test_add_group(app):
    #вызывающие в фикстуре вспомогательные методы
    app.login(username="admin", password="secret")
    app.create_group(Group(name="qwerty1", header="qwerty1", footer="qwerty1"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()