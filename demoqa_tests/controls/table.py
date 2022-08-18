from selene import have


class Table:

    def __init__(self, element):
        self.element = element

    def check_data(self, row_index: int, column_index: int, *values: str):
        for value in values:
            self.element.all('tr')[row_index].all('td')[column_index].should(have.text(value))
        return self
