from selene.support.shared import browser


class StudentRegistrationForm:

    def set_first_name(self, param: str):
        browser.element("#firstName").type(param)
        return self

    def set_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def set_mail(self, value):
        browser.element("#userEmail").type(value)
        return self
