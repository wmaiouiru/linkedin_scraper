import __init__
import os
import json
from selenium import webdriver
import unittest
from linkedin_scraper import Person
import logging



class TestPerson(unittest.TestCase):
    """
    Test Person
    """
    def test_person(self):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        driver = webdriver.Chrome()

        # Get the current working directory
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'test/data/person_page.html')

        # Navigate to the locally served HTML file
        driver.get(f'file://{file_path}')

        # Get and print the HTML content of the page
        # html_content = driver.page_source

        person = Person(
            driver=driver,
            get=False,
            scrape=False,
            use_profile_homepage=True
            )

        person.get_name_and_location()
        self.assertEqual(person.name, 'Rick Fox')
        self.assertEqual(person.location, 'The Bahamas')

        person.get_open_to_work()
        self.assertEqual(person.open_to_work, False)

        person.get_about()
        self.assertTrue('Rick Fox is a serial entrepreneur, philanthropist and three-time NBA champion.' in person.about)

        person.get_experiences()
        
        self.assertGreaterEqual(len(person.experiences), 1)

        # Clean up and close the WebDriver
        person.get_educations()
        self.assertGreaterEqual(len(person.educations), 1)
        print(json.dumps(person.to_dict(), indent=2))
        
        driver.quit()
if __name__ == "__main__":
    unittest.main()