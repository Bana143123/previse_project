import pytest
import os
from pages.schedule_call_page import ScheduleCallPage
from utils.excel_reader import read_excel_data
import time

@pytest.mark.parametrize("user", read_excel_data("data/data_file.xlsx"))
def test_schedule_call(driver, user):
    page = ScheduleCallPage(driver)
    page.open_homepage()
    page.click_schedule_call()
    page.handle_privacy_popup()
    time.sleep(10)
    page.select_random_day(user)
    screenshot_path = os.path.join("screenshots", f"{user['name']}_details.png")
    page.take_screenshot(screenshot_path)
    page.close_popup()
