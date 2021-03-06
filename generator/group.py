from model.group import Group
import string
import random
import os.path
import jsonpickle
import getopt
import sys


# считывание параметров запуска скрипта
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# количество генерируемых групп по умолчанию (если не заданы параметры запуска скрипта)
n = 5
# файл для генерации тестовых данных по умолчанию (если не заданы параметры запуска скрипта)
f = "data/groups.json"

# переприсваивание переменных по умолчанию, если заданы параметры запуска скрипта
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(max_len))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # генерация файла при помощи пакета jsonpickle
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
