from selene import have
from selene.support.shared import browser
from demoqa_tests.controls.date_picker import DatePicker, Month
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tags_input import TagsInput
from demoqa_tests.data import Student, Hobbies, Gender, Subjects
from demoqa_tests.tools import resources
from demoqa_tests.controls import dropdown
from demoqa_tests.pages.pages_form import StudentRegistrationForm


def test_registration_form():
    browser.open("automation-practice-form")

    (StudentRegistrationForm()
     .set_first_name(Student.name)
     .set_last_name(Student.surname)
     .set_email(Student.email)
     .set_mobile_nubmer(Student.mobile_number)
     .ser_gender(Gender.other)
     .set_birth_data(Student.birth_year, Student.birth_month, Student.birth_day)
     .select_subjact(Subjects.history,
                     Subjects.chemistry)
     .select_hobbies(Hobbies.reading)
     .upload('screen.png')
     .set_adress(Student.current_adress)
     .set_state_city(Student.state, Student.city)
     )
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
