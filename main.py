from users import Users

inputs=[
    "SHOW",
    "SHOW u1",
    "EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL",
    "SHOW u4",
    "SHOW u1",
    "EXPENSE u1 1250 2 u2 u3 EXACT 370 880",
    "SHOW",
    "EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20",
    "SHOW u1",
    "SHOW"
        ]

u1=Users("RS", "rs@rs.com", 8660211111)
        #  {"id":"u2", "name":"RS2", "email":"rs2@rs.com", "phone_number": 8660211112},
        #  {"id":"u3", "name":"RS3", "email":"rs3@rs.com", "phone_number": 8660211113},
        #  {"id":"u4", "name":"RS4", "email":"rs4@rs.com", "phone_number": 8660211114}]

users=[u1]
for user in users:
    print(u1.name,u1.balances,u1.user_dict)