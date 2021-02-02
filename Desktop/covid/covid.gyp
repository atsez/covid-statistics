# importing 
from covid import Covid
import time
# initializing
covid = Covid()
# global datas
print()
print('total confirmed cases in world: ' , covid.get_total_confirmed_cases)
time.sleep(0.5)
print()
print('total active cases in world: ' , covid.get_total_active_cases())
time.sleep(0.5)
print('total recovered cases in world: ' , covid.get_total_recovered())
time.sleep(0.5)
print('total deaths in world:' , covid.get_total_deaths())
total_confirmed_cases = covid.get_total_confirmed_cases
time.sleep(0.5)
population = 7710000000
# country datas
while True :
    print()
    country_name_X = input('country data: ')
    cases = covid.get_status_by_country_name(country_name=country_name_X)
    print(cases)
    print('hello')
    print()