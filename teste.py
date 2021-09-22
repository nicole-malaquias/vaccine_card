
# import calendar
import datetime 

import time





# next_vaccine = datetime.date.today() + datetime.timedelta(days=90)
from datetime import datetime, timedelta

new_next = (datetime.now() + timedelta(hours=2160)).strftime("%a, %d %b, %Y %H:%M:%S %z")
print(new_next)


    # "Fri, 10 Sep 2021 00:00:00 GMT",

agora = time.strftime(f'%a, %d  %b %Y %H:%M:%S %z ')
print(agora)





# dWeek = datetime.datetime.today().strftime('%A')
# dyear = datetime.datetime.today().strftime('%Y')
# d = datetime.datetime.today().strftime('%d')
# moth =  datetime.datetime.today().strftime('%b')
# gmt =  gmtime()
# data_now = f'{dWeek}, {d} {moth} {dyear} {gmt}'
# print(data_now)



# NWeek = next_vaccine.strftime('%A')
# Nyear = next_vaccine.strftime('%Y')
# Nd = next_vaccine.strftime('%d')
# Nmoth = next_vaccine.strftime('%b')

# print(Nmoth)
