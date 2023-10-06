import logging
from selenium.webdriver.common.by import By

from ..objects import Experience

class ExperienceParser:
    def parse(self, driver):
        self.driver = driver
        experiences = []
        experience_section = self.get_experiences_section()
        for position in experience_section.find_elements(By.XPATH,'.//li[contains(@class, "artdeco-list__item")]'):
            experience = self.parse_position(position)
            experiences.append(experience)
        return experiences

    def get_experiences_section(self):
        experience_id_div = self.driver.find_element(By.ID, "experience")
        experience_section  = experience_id_div.find_element(By.XPATH, "..") 
        return experience_section
    
    def parse_position(self, position):
        logging.debug(position.get_attribute('innerHTML'))
        # company_linkedin_url = position.find_element(By.XPATH,"*").get_attribute("href")
        company_linkedin_url = position.find_element(By.CSS_SELECTOR, 'a[data-field="experience_company_logo"]').get_attribute("href")
        position_info = position.find_element(By.XPATH, """.//*[contains(@class, 'display-flex') and contains(@class, 'flex-row') and contains(@class, 'justify-space-between')]""")
        position_elements = position_info.find_elements(By.XPATH, './/*[contains(@aria-hidden, "true")]')

        logging_position_info = logging.debug
        logging_position_info(f'---------')
        for position_element in position_elements:
            logging_position_info(position_element.get_attribute('innerHTML'))
        position_duration = position_elements[2].text
        position_duration_split = position_duration.split('·')
        start_end_split = position_duration_split[0].split('-')
        from_date = start_end_split[0].strip()
        to_date = start_end_split[1].strip()
        duration = position_duration_split[1].strip()

        company_name, position_type = self.get_company_and_position_type(position_elements)

        return Experience(
            position_title=self.get_position_title(position_elements),
            from_date=from_date,
            to_date=to_date,
            duration=duration,
            location=self.get_company_location(position_elements),
            description=self.get_description(position),
            position_type=position_type,
            institution_name=company_name,
            linkedin_url=company_linkedin_url
        )

    def get_company_and_position_type(self, position_elements):
        company_and_type = position_elements[1].text
        company_and_type_split = company_and_type.split('·')

        position_type = None
        company_name = company_and_type_split[0].strip()
        if len(company_and_type_split) > 1:
            position_type = company_and_type_split[1].strip()
        return company_name, position_type

    def get_position_title(self, position_elements):
        return position_elements[0].text

    def get_company_location(self, position_elements):
        if len(position_elements) >= 4:
            return position_elements[3].text

    def get_description(self, position):
        try:
            position_description_div = position\
                .find_element(By.XPATH, """.//*[contains(@class, 'inline-show-more-text')]""")\
                .find_element(By.XPATH, './/*[contains(@aria-hidden, "true")]')
            return position_description_div.text
        except:
            return None