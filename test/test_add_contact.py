# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="fname", middlename="mname", lastname="lname", nickname="nmane",
                               title="123", company="inet", hometelephone="84822343536",
                               mobiletelephone="89858883843", worktelephone="1234567", faxtelephone="12345678",
                               email="lllname@gmail.com", homepage="https://nname.com", ayear="1991", phone2="123"))

