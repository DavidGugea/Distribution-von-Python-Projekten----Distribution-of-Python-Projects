import gettext
import random 

trans = gettext.translation("script", "locale", ["de"])
trans.install()

values = list()

while True:
    w = input(_("Please enter a value: "))
    if not w:
        break

    values.append(w)

print(_("The random choice is {0}").format(random.choice(values)))
