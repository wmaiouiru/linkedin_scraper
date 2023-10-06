# Integration test
import __init__
import os
import json
from linkedin_scraper import Person
from linkedin_scraper import actions
from selenium import webdriver
use_profile_homepage = True
email = os.environ['LINKEDIN_EMAIL']
password = os.environ['LINKEDIN_PASSWORD']

try:
    if os.getenv("CHROMEDRIVER") == None:
        driver_path = os.path.join(
            os.path.dirname(__file__), "drivers/chromedriver"
        )
    else:
        driver_path = os.getenv("CHROMEDRIVER")

    driver = webdriver.Chrome(driver_path)
except:
    driver = webdriver.Chrome()


actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal

rick_fox = Person("https://www.linkedin.com/in/rifox?trk=pub-pbmap", driver=driver, close_on_complete=False,use_profile_homepage =use_profile_homepage)
print(json.dumps(rick_fox.to_dict(), indent=2, default=str))
iggy = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver, close_on_complete=False,use_profile_homepage=use_profile_homepage)
print(json.dumps(iggy.to_dict(), indent=2, default=str))
Anirudra = Person("https://in.linkedin.com/in/anirudra-choudhury-109635b1", driver=driver, close_on_complete=False,use_profile_homepage=use_profile_homepage)
print(json.dumps(Anirudra.to_dict(), indent=2, default=str))
