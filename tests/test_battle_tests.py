from selene import have
from selene.support.shared import browser
from demoqa_tests.controls.date_picker import DatePicker, Month
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tags_input import TagsInput
from demoqa_tests.tools import resources
from demoqa_tests.controls import dropdown


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
    '''
    browser.element("#dateOfBirth-wrapper").click()
    browser.element(".react-datepicker__month-select").type(Student.birthMonthName)
    browser.element(".react-datepicker__year-select").type(Student.birthYear)
    browser.element("[aria-label= 'Choose Saturday, September 16th, 2006']").click()
    '''

    calendar = '#dateOfBirthInput'
    browser.element(calendar).click()
    date_of_birth = DatePicker(browser.element('#dateOfBirth'))
    date_of_birth.select_year(2006).select_month(Month.September).select_day(16)

    '''
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element(f'[value="{Student.birthYear}"]').click()
    browser.element(f'.react-datepicker__month-select [value="{Student.birthMonth}"]').click()
    browser.element(f'.react-datepicker__day--0{Student.birthDay}').click()
    '''
    browser.element("#uploadPicture").send_keys(resources('screen.png'))

    '''
    subjacts = browser.element('#subjectsInput')
    tags_input.add(subjacts, from_='History', to='Chemistry')
    tags_input.add(subjacts, from_='Maths')
    '''
    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('History')
    subjects.add('Chem', autocomplete='Chemistry')

    browser.element("#currentAddress").type(Student.currentAdress)

    class Hobbies:
        sports = 'Sports'
        reading = 'Reading'
        music = 'Music'

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
    '''
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
    '''
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


def test_web_table_form():
    browser.open("webtables")
    # browser.element('footer')._execute_script('element.style.display = "None"')
    # browser.all('[class^= select-wrap]')

    # added new record no.4
    browser.element("#addNewRecordButton").press_enter()
    browser.element("#firstName").type("Unknown")
    browser.element("#lastName").type("Last")
    browser.element("#userEmail").type("dsfgdfg@gmail.com")
    browser.element("#age").type("18")
    browser.element("#salary").type("40000").press_enter()
    browser.element("#department").type("Seven")
    browser.element("#submit").press_enter()

    # check adding record

    browser.all(".rt-tbody").should(have.text('Unknown'))
    browser.all(".rt-tbody").should(have.text('Last'))
    browser.all(".rt-tbody").should(have.text('dsfgdfg@gmail.com'))
    browser.all(".rt-tbody").should(have.text('18'))
    browser.all(".rt-tbody").should(have.text('40000'))
    browser.all(".rt-tbody").should(have.text('Seven'))

    # edit record no.2

    browser.element("#edit-record-2").click()
    browser.element("#firstName").clear().type("Mr")
    browser.element("#lastName").clear().type("Anderson")
    browser.element("#userEmail").set_value("matrix@hasyou.net")
    browser.element("#age").clear().type("81")
    browser.element("#salary").clear().type("00004")
    browser.element("#department").clear().type("seVen")
    browser.element("#submit").press_enter()

    # check edit record
    browser.all(".rt-tbody").should(have.text('Mr'))
    browser.all(".rt-tbody").should(have.text('Anderson'))
    browser.all(".rt-tbody").should(have.text('matrix@hasyou.net'))
    browser.all(".rt-tbody").should(have.text('81'))
    browser.all(".rt-tbody").should(have.text('00004'))
    browser.all(".rt-tbody").should(have.text('seVen'))

    # check record no.3 and rename

    browser.element("#edit-record-3").click()
    browser.element("#firstName").type('Target')
    browser.element("#submit").press_enter()

    browser.element('#searchBox').type('Target')
    browser.all(".rt-tbody").should(have.text('Target'))
    # browser.element('#searchBox').type('Kierra')
    # browser.all(".rt-tbody").should(have.text('Kierra'))

    # delete record no.3

    browser.element("#delete-record-3").click()

    # check delete record
    browser.all(".rt-tbody").should_not(have.text('Target'))

    # browser.all(".rt-tbody").should_not(have.text('Kierra'))
