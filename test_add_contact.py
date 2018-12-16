# -*- coding: utf-8 -*-
import pytest

from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="fname", middlename="mname", lastname="lname", nickname="nmane",
                            title="123", company="inet", address="moscow, 23", hometelephone="84822343536",
                            mobiletelephone="89858883843", worktelephone="1234567", faxtelephone="12345678",
                            email="lllname@gmail.com", homepage="https://nname.com", bday="3",
                            bmonth="March", byear="1991", aday="4", amonth="May", ayear="1991",
                            address2="NY, 45", phone2="123", notes="qwerty"))
    app.logout()

