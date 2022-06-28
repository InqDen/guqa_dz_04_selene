from selene import have
from selene.core import command
from selene.support.shared import browser


def test_registration_form():
    browser.open("automation-practice-form")

#fill out
    browser.element("#firstName").type("Unknown")
    browser.element("#lastName").type("Unknown")

    browser.element("#userEmail").type("dsfgdfg@gmail.com")

    browser.all(".custom-radio").element_by(have.exact_text("Other")).click()

    browser.element("#userNumber").type("1659865123")

    browser.element("#dateOfBirth-wrapper").click()
    browser.element(".react-datepicker__month-select").type("September")
    browser.element(".react-datepicker__year-select").type("2006")
    browser.element("[aria-label= 'Choose Saturday, September 16th, 2006']").click()

    browser.element("#uploadPicture").type("D:\Prog\Python\Project\guqa_dz_04_selene\e7c772fd52841b814819c58037df730d.jpeg")

    browser.element("#subjectsInput").type("History").press_enter().type("English").press_enter()

    browser.element("#currentAddress").type("Russia Ekb. Lenina str. 1919 9191")

    browser.all(".custom-checkbox").element_by(have.exact_text("Reading")).click()

    browser.element("#state").perform(command.js.scroll_into_view).click()
    browser.element("#state input").type("NCR").press_tab()
    browser.element("#city input").type("Gurgaon").press_tab()

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
        'Picture e7c772fd52841b814819c58037df730d.jpeg',
        'Address Russia Ekb. Lenina str. 1919 9191',
        'State and City NCR Gurgaon'
    ))

    browser.element("#closeLargeModal").press_enter()

def test_web_table_form():
    browser.open("webtables")
# added new record no.4
    browser.element("#addNewRecordButton").press_enter()
    browser.element("#firstName").type("Unknown")
    browser.element("#lastName").type("Unknown")
    browser.element("#userEmail").type("dsfgdfg@gmail.com")
    browser.element("#age").type("18")
    browser.element("#salary").type("40000").press_enter()
    browser.element("#department").type("Seven")
    browser.element("#submit").press_enter()

# edit record no.2
    browser.element("#edit-record-2").click()
    browser.element("#firstName").clear().type("Mr")
    browser.element("#lastName").clear().type("Anderson")
    browser.element("#userEmail").set_value("matrix@hasyou.net")
    browser.element("#age").type("81")
    browser.element("#salary").clear().type("00004")
    browser.element("#department").clear().type("seVen")
    browser.element("#submit").press_enter()

# delete record no.3
    browser.element("#delete-record-3").click()