from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.select import Select

from .base_page import BasePage


class CustomersPageLocators:
    CLEAR_BUTTON = (By.ID, "clear-button")
    SEARCH_INPUT = (By.ID, "search-input")
    DROP_DOWN = (By.ID, "search-column")
    MATCH_CASE = (By.ID, "match-case")
    SUMMARY = (By.ID, "table-resume")
    SEARCH_TERM = (By.ID, "search-slogan")
    TABLE = (By.XPATH, "//table")


class CustomersPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.wait = ui.WebDriverWait(self.context.driver, 10)

    def clear_button_click(self):
        """
        Click on Clear Filters Button.

        :return: the Button element
        """
        clear_button = self.wait.until(
            lambda d: d.find_element(*CustomersPageLocators.CLEAR_BUTTON)
        )
        clear_button.click()
        return clear_button

    def set_search_input(self, search_input):
        """
        Set value to searchInput field.

        :param search_input: input which should be typed into the field
        """
        self.find_element(CustomersPageLocators.SEARCH_INPUT).send_keys(search_input)

    def set_search_column_drop_down_list_field(self, value):
        """
        Set value to Search Column Drop Down List field.

        :param value: String which should match with one of values visible on the dropdown
        """
        Select(self.find_element(CustomersPageLocators.DROP_DOWN)).select_by_visible_text(value)

    def set_match_case_checkbox_field(self, value):
        """
        Set Match Case Checkbox field to required value.

        :param value: boolean value of the checkbox status true - checked, false - unchecked
        """
        case_checkbox = self.find_element(CustomersPageLocators.MATCH_CASE)
        checkbox_is_selected = case_checkbox.is_selected()
        if str(checkbox_is_selected) != value:
            case_checkbox.click()

    def get_summary_text(self):
        return self.find_element(CustomersPageLocators.SUMMARY).get_attribute("innerText")

    def get_search_term_text(self):
        return self.find_element(CustomersPageLocators.SEARCH_TERM).get_attribute("innerText")

    def get_search_input_text(self):
        return self.find_element(CustomersPageLocators.SEARCH_INPUT).get_attribute("value")

    def get_search_results_table_text(self):
        return self.find_element(CustomersPageLocators.TABLE).text

    def open(self):
        application_url \
            = self.context.config.userdata.get("applicationUrl",
                                               'http://localhost:8080/root/sample-page/pages/index.html')

        return self.context.driver.get(application_url)
