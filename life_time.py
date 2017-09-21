import datetime

today = datetime.date.today()
birthday = datetime.date(1985,1,28)
life = today - birthday
print(life.days)