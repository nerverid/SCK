# Проверяет текущую дату, создаёт списки на повторение
from datetime import datetime

def wich_day():
    return datetime.today().strftime("%Y-%m-%d")

print(wich_day())
