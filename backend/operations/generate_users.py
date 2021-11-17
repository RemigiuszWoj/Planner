import json
import random

MAX = 20

records = []
with open("fixture.json", "w", encoding="utf-8") as fp:
    id = 0
    for _ in range(MAX):
        id += 1
        name = random.choice(open(r"backend/operations/data/names", "r", encoding="utf-8").read().splitlines())
        surname = random.choice(open(r"backend/operations/data/surnames", "r", encoding="utf-8").read().splitlines())
        email = "{}.{}.{}".format(name.lower(), surname.lower(), random.choice(["gmail.com", "wp.pl", "onet.pl"]))
        phone = "".join([str(random.randint(0, 9)) for i in range(9)])
        position = (random.randint(-20, 20), random.randint(-20, 20))
        visit_time = random.randrange(10, 60, 5)
        adress = (
            random.choice(open(r"backend/operations/data/adresses", "r", encoding="utf-8").read().splitlines())
            + " "
            + str(random.randint(1, 20))
            + "/"
            + str(random.randint(1, 20))
        )
        fields = {
            "first_name": name,
            "last_name": surname,
            "email": email,
            "phone_number": phone,
            "x": position[0],
            "y": position[1],
            "visit_time": visit_time,
            "adress": adress,
        }
        records.append({"model": "user.User", "pk": id, "fields": fields})
    fp.write(json.dumps(records, indent=4, sort_keys=True))
