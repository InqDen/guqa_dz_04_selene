from selene.core.entity import Element
from selene.support.shared import browser
from enum import Enum


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_year(self, option: int):
        self.element.element(f'[value="{option}"]').click()
        return self

    def select_month(self, option: int):
        self.element.element(f'[value="{option.value}"]').click()
        return self

    def select_day(self, option: int):
        self.element.element(f'.react-datepicker__day--0{option}').click()

    def set_date(self, calendar: Element, option: str):
        browser.execute_script(
            '''
                document.querySelector("#dateOfBirthInput")
                .value = ''
            ''')
        browser.element(calendar).set_value(option).click()


class Month(Enum):
    January = 0
    February = 1
    March = 2
    April = 3
    May = 4
    June = 5
    July = 6
    August = 7
    September = 8
    October = 9
    November = 10
    December = 11

'''
calendar = '#dateOfBirthInput'
    browser.element(calendar).click()
    date_of_birth = DatePicker(browser.element('#dateOfBirth'))
    date_of_birth.select_year(2006).select_month(Month.September).select_day(16)
'''