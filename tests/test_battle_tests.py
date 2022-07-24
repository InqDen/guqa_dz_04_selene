from typing import Optional

from selene import have
from selene.core.entity import Element
from selene.support.shared import browser

# from demoqa_tests.controls import tags_input
from demoqa_tests.tools import resources
from demoqa_tests.controls import dropdown
from demoqa_tests.controls import modal_content


def test_registration_form():
    browser.open("automation-practice-form")

    class Student:
        name = 'Unknown'
        surname = 'Unknown'
        email = 'dsfgdfg@gmail.com'
        mobileNumber = '1659865123'
        birthDay = '16'
        birthMonth = '09'
        birthMonthName = 'September'
        birthYear = '2006'
        currentAdress = 'Russia Ekb. Lenina str. 1919 9191'
        state = 'NCR'
        city = 'Gurgaon'

    # fill out
    browser.element("#firstName").type(Student.name)
    browser.element("#lastName").type(Student.surname)

    browser.element("#userEmail").type(Student.email)

    class Gender:
        male = 'Male'
        female = 'Female'
        other = 'Other'

    browser.all(".custom-radio").element_by(have.exact_text(Gender.other)).click()

    browser.element("#userNumber").type("1659865123")

    browser.element("#dateOfBirth-wrapper").click()
    browser.element(".react-datepicker__month-select").type(Student.birthMonthName)
    browser.element(".react-datepicker__year-select").type(Student.birthYear)
    browser.element("[aria-label= 'Choose Saturday, September 16th, 2006']").click()
    '''
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element(f'[value="{Student.birthYear}"]').click()
    browser.element(f'.react-datepicker__month-select [value="{Student.birthMonth}"]').click()
    browser.element(f'.react-datepicker__day--0{Student.birthDay}').click()
    '''
    browser.element("#uploadPicture").send_keys(resources('screen.png'))

    class TagsInput:
        def __init__(self):
            self.element: Element = ...

        def add(self, from_: str, /, *, autocomlete: Optional[str] = None):
            self.type(from_)
            browser.all(
                '.subjects-auto-complete__control'
            ).element_by(have.text(autocomlete or from_)).click()



    # autocomlite("#subjectsInput", from= )
    tags_input = TagsInput
    tags_input.element = browser.element('#subjectsInput')
    tags_input.add('His', autocomlete='History')
    tags_input.add('Maths')

    # browser.element("#subjectsInput").type("History").press_enter().type("English").press_enter()
    # browser.element("#currentAddress").type(Student.currentAdress)

    class Hobbies:
        sports = 'Sports'
        reading = 'Reading'
        music = 'Music'

    tags_input2 = TagsInput()
    tags_input2.element = browser.element('#hobbiesInput')
    browser.all(".custom-checkbox").element_by(have.exact_text(Hobbies.reading)).click()

    '''
    browser.element("#state").perform(command.js.scroll_into_view).click()
    browser.element("#state input").type("NCR").press_tab()
    browser.element("#city input").type("Gurgaon").press_tab()
    '''
    dropdown.select(browser.element('#state'), option='NCR')
    dropdown.select(browser.element('#city'), option='Gurgaon')

    browser.element('footer')._execute_script('element.style.display = "None"')
    browser.element("#submit").press_enter()

    # check
    browser.all("tbody tr").should(have.texts(
        'Student Name Unknown Unknown',
        'Student Email dsfgdfg@gmail.com',
        'Gender Other',
        'Mobile 1659865123',
        'Date of Birth 16 September,2006',
        'Subjects History, English',
        'Hobbies Reading',
        'Picture screen.png',
        'Address Russia Ekb. Lenina str. 1919 9191',
        'State and City NCR Gurgaon'
    ))

    browser.element("#closeLargeModal").click()
