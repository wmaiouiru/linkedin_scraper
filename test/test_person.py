"""
Test Person
"""
import test
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
    @classmethod
    def setUpClass(cls):
        # Configure logging settings
        logging.basicConfig(format='%(levelname)s:%(filename)s:%(lineno)d:%(message)s', level=logging.INFO)

    def test_person(self):
        """
        From HTML
        """

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
        person.get_open_to_work()
        person.get_about()
        person.get_experiences()
        person.get_educations()

        logging.info(json.dumps(person.to_dict(), indent=2)) 


        self.assertEqual(person.name, 'Rick Fox')
        self.assertEqual(person.location, 'The Bahamas')


        self.assertEqual(person.open_to_work, False)


        self.assertTrue('Rick Fox is a serial entrepreneur, philanthropist and three-time NBA champion.' in person.about)

        self.assertGreaterEqual(len(person.experiences), 1)
        print('person.experiences[0].description', person.experiences[0].description)
        self.assertTrue('Partanna is a Clean-Air Technology Company' in person.experiences[0].description)
        
        # Clean up and close the WebDriver

        self.assertGreaterEqual(len(person.educations), 1)

        driver.quit()

    def test_from_dict(self) -> None:
        """
        From Dict
        """
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'test/data/person_payload.json')
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            data_dict = json.load(file)        
            person = Person.from_dict(data_dict)

if __name__ == "__main__":
    unittest.main()