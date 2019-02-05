import random
import string

constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1", title="title1",
            company="company1", address="address1", hometelephone="hometelephone1", mobiletelephone="mobiletelephone1",
            worktelephone="worktelephone1", faxtelephone="faxtelephone1", email="email1", email2="email21",
            email3="email31", homepage="homepage1", ayear="ayear1", phone2="phone21"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2", title="title2",
            company="company2", address="address2", hometelephone="hometelephone2", mobiletelephone="mobiletelephone2",
            worktelephone="worktelephone2", faxtelephone="faxtelephone2", email="email2",
                email2="email22", email3="email32", homepage="homepage2", ayear="ayear2", phone2="phone22")
]

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