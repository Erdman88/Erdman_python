import re
from random import randrange

def test_lastname_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()
    #index = randrange(len(contact_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)

def test_lastname_on_view_page(app):
    contact_from_home_page = app.contact.get_contact_list()
    #index = randrange(len(contact_from_home_page))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname

def test_firstname_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()
    #index = randrange(len(contact_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)

def test_firstname_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.firstname == contact_from_edit_page.firstname

def test_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()
    #index = randrange(len(contact_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)

def test_address_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.address == contact_from_edit_page.address

def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()
    #index = randrange(len(contact_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_emails_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()
    #index = randrange(len(contact_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page()
    #index = randrange(len(contact_from_view_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.hometelephone == contact_from_edit_page.hometelephone
    assert contact_from_view_page.mobiletelephone == contact_from_edit_page.mobiletelephone
    assert contact_from_view_page.worktelephone == contact_from_edit_page.worktelephone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.hometelephone, contact.mobiletelephone, contact.worktelephone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))