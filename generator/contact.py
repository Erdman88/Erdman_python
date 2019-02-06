from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encorder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
