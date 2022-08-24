import allure
from selene.support.conditions import have
from selene.support.shared import browser
from demoqa_tests.controls.table import Table
from demoqa_tests.data import Student, Hobbies, Gender, Subjects
from demoqa_tests.pages.pages_form import StudentRegistrationForm
from utils import attach


@allure.step('Open registration form')
def test_registration_form():


    browser.open('https://demoqa.com/automation-practice-form')


    # browser = setup_chrome
    '''
    with allure.step('Open Registration Form'):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element('.practce-form-wrapper').should(have.text('Student Regidtration Form'))
        browser.driver.execute_script("$('.footer').remove()")
        browser.driver.execute_script("$('#fixban').remove()")
    '''

    with allure.step('Fill form'):
        (StudentRegistrationForm()
         .set_first_name(Student.name)
         .set_last_name(Student.surname)
         .set_email(Student.email)
         .set_mobile_nubmer(Student.mobile_number)
         .ser_gender(Gender.other)
         .set_birth_data(Student.birth_year,
                         Student.birth_month,
                         Student.birth_day)
         .select_subjact(Subjects.history,
                         Subjects.chemistry)
         .select_hobbies(Hobbies.reading)
         .upload('screen.png')
         .set_adress(Student.current_adress)
         .set_state_city(Student.state,
                         Student.city)
         .submit()
         )
    with allure.step('check form results'):
        modal_window = browser.element('.modal-content')
        result_table = Table(modal_window.element('.table'))
        (result_table
         .check_data(1, 1, Student.name, Student.surname)
         .check_data(2, 1, Student.email)
         .check_data(3, 1, Gender.other)
         .check_data(4, 1, Student.mobile_number)
         .check_data(5, 1, Student.birthday_day)
         .check_data(6, 1, Subjects.history, Subjects.chemistry)
         .check_data(7, 1, Hobbies.reading)
         .check_data(8, 1, Student.picture)
         .check_data(9, 1, Student.current_adress)
         .check_data(10, 1, Student.state, Student.state)
         )

    browser.element("#closeLargeModal").click()

    attach.add_log(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
