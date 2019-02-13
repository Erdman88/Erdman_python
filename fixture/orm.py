from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, hast, name, user, password):
        #в conv передается набор конвертеров-преобразователей для отдельных типов данных
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        #сопоставление свойств, описанных в классах с таблицами и полями этих таблиц
        self.db.ganerate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=group.id, name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        #Извлекаем объект из БД с помощью select
        #преобразуем в список
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        #Извлекаем объект из БД с помощью select
        #преобразуем в список
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))
