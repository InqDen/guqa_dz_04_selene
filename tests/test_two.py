from selene import have
from selene.support.shared import browser
import allure


def test_web_table_form():
    browser.open("https://demoqa.com/webtables")

    with allure.step('Added new record no.4'):
        browser.element("#addNewRecordButton").press_enter()
        browser.element("#firstName").type("Unknown")
        browser.element("#lastName").type("Last")
        browser.element("#userEmail").type("dsfgdfg@gmail.com")
        browser.element("#age").type("18")
        browser.element("#salary").type("40000").press_enter()
        browser.element("#department").type("Seven")
        browser.element("#submit").press_enter()

    with allure.step('Check adding record'):
        browser.all(".rt-tbody").should(have.text('Unknown'))
        browser.all(".rt-tbody").should(have.text('Last'))
        browser.all(".rt-tbody").should(have.text('dsfgdfg@gmail.com'))
        browser.all(".rt-tbody").should(have.text('18'))
        browser.all(".rt-tbody").should(have.text('40000'))
        browser.all(".rt-tbody").should(have.text('Seven'))

    with allure.step('Edit record no.2'):
        browser.element("#edit-record-2").click()
        browser.element("#firstName").clear().type("Mr")
        browser.element("#lastName").clear().type("Anderson")
        browser.element("#userEmail").set_value("matrix@hasyou.net")
        browser.element("#age").clear().type("81")
        browser.element("#salary").clear().type("00004")
        browser.element("#department").clear().type("seVen")
        browser.element("#submit").press_enter()

    with allure.step('Check edit record'):
        browser.all(".rt-tbody").should(have.text('Mr'))
        browser.all(".rt-tbody").should(have.text('Anderson'))
        browser.all(".rt-tbody").should(have.text('matrix@hasyou.net'))
        browser.all(".rt-tbody").should(have.text('81'))
        browser.all(".rt-tbody").should(have.text('00004'))
        browser.all(".rt-tbody").should(have.text('seVen'))

    with allure.step('Check record no.3 and rename'):
        browser.element("#edit-record-3").click()
        browser.element("#firstName").type('Target')
        browser.element("#submit").press_enter()
        browser.element('#searchBox').type('Target')
        browser.all(".rt-tbody").should(have.text('Target'))

    with allure.step('Delete record no.3'):
        browser.element("#delete-record-3").click()

    with allure.step('Check delete record'):
        browser.all(".rt-tbody").should_not(have.text('Target'))
