from selene.support.shared import browser
from selene import have, by
from selene import command
from demoqa_tests.tools import resources


class StudentRegistrationForm:

    def set_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def set_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def set_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def set_mobile_nubmer(self, value):
        browser.element('#userNumber').type(value)
        return self

    def ser_gender(self, value):
        # browser.element('#genderWrapper').all('.custom-radio').element_by(have.exact_text(value)).click()
        browser.all(".custom-radio").element_by(have.exact_text(value)).click()
        return self

    def set_birth_data(self, year: str, month: int, day: 'str'):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').element(f'[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

        return self

    def select_subjact(self, *values):
        for value in values:
            browser.element('#subjectsInput').set_value(value).press_enter()
        return self

    def select_hobbies(self, *values):
        for value in values:
            browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload(self, file: str):
        browser.element('#uploadPicture').send_keys(resources('screen.png'))
        return self

    def set_adress(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def set_state_city(self, state: str, city: str):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.element(by.text(state)).click()
        browser.element('#city').click()
        browser.element(by.text(city)).click()
        return self

    def submit(self):
        browser.element('footer')._execute_script('element.style.display = "None"')
        browser.element("#submit").press_enter()

        '''
            def submit(self):
        browser.element('#submit').perform(command.js.click)
        '''
