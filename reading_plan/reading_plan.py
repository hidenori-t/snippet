# 読書計画用スニペット
from datetime import date


def reading_plan(title, total_number_of_pages, period):
    current_page = int(input("Current page?: "))
    deadline = (date(int(period[0]), int(period[1]),
                     int(period[2])) - date.today()).days
    print(title, period, "まで残り", deadline, "days",
          (total_number_of_pages - current_page) // deadline, "p/day")
