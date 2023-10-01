import logging
from selenium.webdriver.common.by import By

from ..objects import Education

class EducationParser:
    def parse(self, driver):
        self.driver = driver
        education_section = self.get_educations_section()
        educations = []
        for education_div in education_section.find_elements(By.XPATH,'.//li[contains(@class, "artdeco-list__item")]'):
            education = self.parse_education(education_div)
            educations.append(education)
        return educations

    def parse_education(self, education_div):
        logging.debug(education_div.get_attribute('innerHTML'))

        institution_linkedin_url = education_div.find_element(By.XPATH, './/a').get_attribute("href")
        education_elements = education_div.find_elements(By.XPATH, './/*[contains(@aria-hidden, "true")]')


        institution_name = education_elements[0].text.strip()
        degree = education_elements[1].text.strip()
        from_to_date = education_elements[2].text.strip().split('-')
        from_date = from_to_date[0].strip()
        to_date = from_to_date[1].strip()

        description = None
        return Education(
            from_date=from_date,
            to_date=to_date,
            description=description,
            degree=degree,
            institution_name=institution_name,
            linkedin_url=institution_linkedin_url
        )


    def get_educations_section(self):
        education_id_div = self.driver.find_element(By.ID, "education")
        education_section  = education_id_div.find_element(By.XPATH, "..") 
        return education_section