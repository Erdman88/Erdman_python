# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fname", middlename="mname", lastname="lname", nickname="nmane",
                               title="123", company="inet", hometelephone="84822343536",
                               mobiletelephone="89858883843", worktelephone="1234567", faxtelephone="12345678",
                               email="lllname@gmail.com", homepage="https://nname.com", ayear="1991", phone2="123")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)