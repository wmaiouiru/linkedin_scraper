import test
import os
import json
from selenium import webdriver
import unittest
from linkedin_scraper.objects import Experience
import logging



class TestObjects(unittest.TestCase):
    """
    Test Objects
    """
    @classmethod
    def setUpClass(cls):
        # Configure logging settings
        logging.basicConfig(format='%(levelname)s:%(filename)s:%(lineno)d:%(message)s', level=logging.INFO)

    def test_experience(self):
        payload = {
            "institution_name": "test name",
            "linkedin_url": "https://www.linkedin.com/company/test/",
            "website": None,
            "industry": None,
            "type": None,
            "headquarters": None,
            "company_size": None,
            "founded": None,
            "from_date": "Jun 2023",
            "to_date": "Present",
            "description": "test description",
            "position_title": "test position title",
            "duration": "5 mos",
            "location": "",
            "position_type": "Part-time"
        }
        experience = Experience.from_payload(payload)
        self.assertEqual(experience.institution_name,  "test name")
        self.assertEqual(experience.linkedin_url, "https://www.linkedin.com/company/test/")
        self.assertEqual(experience.headquarters, None)
        self.assertEqual(experience.from_date, "Jun 2023")

if __name__ == "__main__":
    unittest.main()