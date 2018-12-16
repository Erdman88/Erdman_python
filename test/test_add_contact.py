# -*- coding: utf-8 -*-

from Model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="fname", middlename="mname", lastname="lname", nickname="nmane",
                               title="123", company="inet", address="moscow, 23", hometelephone="84822343536",
                               mobiletelephone="89858883843", worktelephone="1234567", faxtelephone="12345678",
                               email="lllname@gmail.com", homepage="https://nname.com", bday="3",
                               bmonth="March", byear="1991", aday="4", amonth="May", ayear="1991",
                               address2="NY, 45", phone2="123", notes="qwerty"))
    app.session.logout()

