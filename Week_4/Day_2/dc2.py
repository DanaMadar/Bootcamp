from datetime import datetime, date
  

birthday = input("What is your B'day? (in DD/MM/YYYY)\n")
#Identify given date as date month and year
birthday = datetime.strptime(birthday, "%d/%m/%Y").date()
#Get today's date
today = date.today()
  
age = today.year - birthday.year - ((today.month,today.day) < (birthday.month,birthday.day))

candles = age % 10

i = "i" * candles

num = "_" * ((12 - candles) // 2)
top = (f"    {num}{i}{num}\n")
bottem = ("  |:H:a:p:p:y:|\n __|___________|__\n|^^^^^^^^^^^^^^^^^|\n|:B:i:r:t:h:d:a:y:|\n|                 |\n~~~~~~~~~~~~~~~~~~~")
print(top, bottem)