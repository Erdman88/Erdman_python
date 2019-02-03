# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

#гинератор случайных строк
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*3
    #многократно случайно выбираем символ из заданной строки
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                address="", hometelephone="", mobiletelephone="", worktelephone="", faxtelephone="", email="",
                email2="", email3="", homepage="", ayear="", phone2="")] + [
        Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 4),
                lastname=random_string("lastname", 6), nickname=random_string("nickname", 5),
                title=random_string("title", 3), company=random_string("company", 5),
                address=random_string("address", 7), hometelephone=random_string("hometelephone", 9),
                mobiletelephone=random_string("mobiletelephone", 9), worktelephone=random_string("worktelephone", 9),
                faxtelephone=random_string("faxtelephone", 6), email=random_string("email", 8),
                email2=random_string("email2", 8), email3=random_string("email3", 8),
                homepage=random_string("homepage", 8), ayear=random_string("ayear", 4), phone2=random_string("phone2", 9))
    for i in range(3)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

