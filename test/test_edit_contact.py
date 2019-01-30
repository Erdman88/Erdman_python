from model.contact import Contact
from random import randrange

def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="fname", middlename="mname", lastname="lname", nickname="nmane",
                               title="123", company="inet", hometelephone="84822343536",
                               mobiletelephone="89858883843", worktelephone="1234567", faxtelephone="12345678",
                               email="lllname@gmail.com", homepage="https://nname.com", ayear="1991", phone2="123")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)