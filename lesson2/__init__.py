import datetime

def lesson():
    dict = [
        {"название": "176128","категория":"Music", "Главная категория":"Music","Валюта":"USD", "таргет2":625.0,"Цель в долларах":1000.0,"Дедлайн":"2013-01-10","Дата публикации": "2012-12-09","таргет1":0.0,"rent":34.0, "income":20.0},
        {"название": "241929","категория":"Accessories", "Главная категория":"Fashion","Валюта":"USD", "таргет2":22.0,"Цель в долларах":80000.0,"Дедлайн":"2016-11-18", "Дата публикации": "2016-10-19", "таргет1":0.0,"rent":34.0, "income":14.0},
        {"название": "244460","категория":"Food","Главная категория":"Food","Валюта":"KZT", "таргет2":35.0,"Цель в долларах":20.0,"Дедлайн":"2015-05-17", "Дата публикации": "2015-04-17", "таргет1":1.0,"rent":34.0, "income":24.0},
        {"название": "80845","категория":"Theater","Главная категория":"Theater","Валюта":"USD", "таргет2":145.0,"Цель в долларах":99.0,"Дедлайн":"2013-06-17", "Дата публикации": "2013-05-03", "таргет1":1.0,"rent":34.0, "income":34.0},
        {"название": "181197","категория":"Shorts","Главная категория":"Film & Video","Валюта":"EUR", "таргет2":387.0,"Цель в долларах":1900.0,"Дедлайн":"2012-08-11", "Дата публикации": "2012-07-12", "таргет1":0.0,"rent":34.0, "income":44.0}
        ]
  # income*срок -((rent/30)*срок+таргет2)
  #   dict.append({"название": "7777777","категория":"Shorts","Главная категория":"Film & Video","Валюта":"EUR", "таргет2":387.0,"Цель в долларах":1900.0,"Дедлайн":"2012-08-11", "Дата публикации": "2012-07-12","rent":4.0, "income":104.0})
  #   for i in dict:
  #       i["Срок"]=(datetime.date.fromisoformat(i["Дедлайн"]) - datetime.date.fromisoformat(i["Дата публикации"])).days
  #       i["Год публикации"] = datetime.date.fromisoformat(i["Дата публикации"]).year
  #
  #   isSuccess = dict[-1]["income"] * dict[-1]["Срок"] - ((dict[-1]["rent"] / 30) * dict[-1]["Срок"] + dict[-1]["таргет2"])
  #   if isSuccess >= dict[-1]["Цель в долларах"]:
  #       dict[-1]["таргет1"] = 1.0
  #   else:
  #       dict[-1]["таргет1"] = 0.0

user_A = {"python", "java", "docker", "linux"}
user_B = {"python", "aws", "linux", "kubernetes"}

common = user_A & user_B
only_A = user_A - user_B
recommend_to_A = user_B - user_A

print(common, only_A, recommend_to_A)

records = [
  {"id": 1, "email": "a@test.com", "tags": ["vip", "new"]},
  {"id": 2, "email": "b@test.com", "tags": ["vip"]},
  {"id": 3, "email": "a@test.com", "tags": ["fraud"]},
]

emails = {}
tags = {}

for r in records:
    email = r["email"]
    emails.setdefault(email, []).append(r["id"])
    tags.setdefault(email, set()).update(r["tags"])

duplicates = {e: ids for e, ids in emails.items() if len(ids) > 1}
conflicts = {e: t for e, t in tags.items() if e in duplicates}

report = {
    "duplicates": duplicates,
    "conflicts": conflicts
}

print(report)


lesson()