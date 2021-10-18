import json
import os
import random

# from backend.settings import MAX

if not os.path.isfile("fixture.json"):
    with open("fixture.json", "w", encoding="utf-8") as fp:
        fp.write("[\n")
        id = 0
        for _ in range(1):
            id += 1
            name = random.choice(open(r"backend/operations/data/names", "r", encoding="utf-8").read().splitlines())
            surname = random.choice(
                open(r"backend/operations/data/surnames", "r", encoding="utf-8").read().splitlines()
            )
            email = "{}.{}.{}".format(name.lower(), surname.lower(), random.choice(["gmail.com", "wp.pl", "onet.pl"]))
            phone = "".join([str(random.randint(0, 9)) for i in range(9)])
            position = (random.randint(-20, 20), random.randint(-20, 20))
            fields = {
                "first_name": name,
                "last_name": surname,
                "email": email,
                "phone_number": phone,
                "position": position,
            }
            # command = f"""{
            #     "model": user.User,
            #     "pk": {id},
            #     "fields": {
            #         "first_name": {id},
            #         "last_name": {},
            #         "email": {},
            #         "phone_number": {},
            #         "position": {},
            #     }
            # },
            # """

            # json_file = json.dumps(command)
            # fp.write(json_file)
            # print(json.dumps(fields, ensure_ascii=False).encode("utf8"))
            # fp.write(
            #     ' {\n  "model": "user.User",\n  "pk": {},\n  "fields": {\n   "first_name": {},\n   "last_name": {}},\n   "email": {},\n   "phone_number": {},\n   "position": {}\n  }\n '.format(
            #         id, name, surname, email, phone, position
            #     )
            # )
