from selene import have
from selene.support.shared import browser
from demoqa_tests.controls.date_picker import DatePicker, Month
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tags_input import TagsInput
from demoqa_tests.tools import resources
from demoqa_tests.controls import dropdown
from demoqa_tests.pages.pages_form import StudentRegistrationForm


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

    form = StudentRegistrationForm

    form.set_first_name('Alala').set_first_name(Student.surname).set_mail(Student.email)
    form.set_mail().set_first_name().set_last_name()
    form.set_last_name()
    # fill out
    #browser.element("#firstName").type(Student.name)
    #browser.element("#lastName").type(Student.surname)
    #browser.element("#userEmail").type(Student.email)

    class Gender:
        male = 'Male'
        female = 'Female'
        other = 'Other'

    browser.all(".custom-radio").element_by(have.exact_text(Gender.other)).click()

    browser.element("#userNumber").type("1659865123")

    calendar = '#dateOfBirthInput'
    browser.element(calendar).click()
    date_of_birth = DatePicker(browser.element('#dateOfBirth'))
    date_of_birth.select_year(2006).select_month(Month.September).select_day(16)

    browser.element("#uploadPicture").send_keys(resources('screen.png'))

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('History')
    subjects.add('Chem', autocomplete='Chemistry')

    browser.element("#currentAddress").type(Student.currentAdress)

    class Hobbies:
        sports = 'Sports'
        reading = 'Reading'
        music = 'Music'

    browser.all(".custom-checkbox").element_by(have.exact_text(Hobbies.reading)).click()

    dropdown.select(browser.element('#state'), option='NCR')
    dropdown.select(browser.element('#city'), option='Gurgaon')

    browser.element('footer')._execute_script('element.style.display = "None"')
    browser.element("#submit").press_enter()

    # check

    modal_window = browser.element('.modal-content')
    result_table = Table(modal_window.element('.table'))
    result_table.path_to_cell(row=1, column=2).should(have.exact_text('Unknown Unknown'))
    result_table.path_to_cell(row=2, column=2).should(have.exact_text('dsfgdfg@gmail.com'))
    result_table.path_to_cell(row=3, column=2).should(have.exact_text('Other'))
    result_table.path_to_cell(row=4, column=2).should(have.exact_text('1659865123'))
    result_table.path_to_cell(row=5, column=2).should(have.exact_text('16 September,2006'))
    result_table.path_to_cell(row=6, column=2).should(have.exact_text('History, Chemistry'))
    result_table.path_to_cell(row=7, column=2).should(have.exact_text('Reading'))
    result_table.path_to_cell(row=8, column=2).should(have.exact_text('screen.png'))
    result_table.path_to_cell(row=9, column=2).should(have.exact_text('Russia Ekb. Lenina str. 1919 9191'))
    result_table.path_to_cell(row=10, column=2).should(have.exact_text('NCR Gurgaon'))

    browser.element("#closeLargeModal").click()
