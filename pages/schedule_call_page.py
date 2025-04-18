import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class ScheduleCallPage:
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        self.driver.get("https://www.previseit.com/")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-2146']"))
        )

    def click_schedule_call(self):
        # Wait for the contact menu item and click it
        contact = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@id='menu-item-2146']"))
        )
        contact.click()
        schedule = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(schedule).click().perform()


    def handle_privacy_popup(self):
        print("1")
        try:
            # Switch to the privacy popup iframe
            iframe = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/iframe"))
            )
            self.driver.switch_to.frame(iframe)
            print("2")
            # Click the "Close" (X) button
            time.sleep(5)
            close_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']"))
            )
            close_btn.click()
            print("3")

            # Switch back to the main content
            #self.driver.switch_to.default_content()
            print("popup handled successfully")

        except (TimeoutException, NoSuchElementException):
            print("4")
            #self.driver.switch_to.default_content() # Ensure we're not stuck in iframe
            pass

      
        

    def select_random_day(self,user):
        print("6")
        self.driver.find_element(By.XPATH,"//div[@class='DKTIFpsb_BvUKsL5bGP2 Ycu0Thh4F4paU6_41lGw']").click()
        # Wait for the days to be visible and select a random one
        print("5")
        
        #self.driver.switch_to.default_content()
        time.sleep(5)
        #ScheduleCallPage(self.driver).handle_privacy_popup()
        days = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td[aria-selected='false']"))
        )
        print("9")
        if days:
            random.choice(days).click()

        slot = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='H2wiGo__wRvJJKM0eaOr S4EQ84F_9sWOFYZ9_sX7']"))
        )
        print("10")
        if slot:
            random.choice(slot).click()
        
        self.driver.find_element(By.XPATH,"//button[@class='uvkj3lh y9_mQD7Hd4ZLZ4SUzgyw jyr1fbkKIhuAcffh_VRx VfCFnsGvnnkn_bFdwv5V _jYiR9T_piWilfmGslIg _hOCj_sBOEZ7LFd5ZO9h']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//input[@class='i167bxqy i1uya22c' and contains(@name,'full_name')]").send_keys(user['name'])
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@class='i167bxqy i1uya22c' and contains(@name,'email')]").send_keys(user['email'])
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//textarea[@class='i167bxqy ikzg8f9 i1uya22c']").send_keys(user['status'])
        time.sleep(3)
        
        self.driver.switch_to.default_content()

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def close_popup(self):
        # Wait for the close button to be visible and click it
        close_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='calendly-popup-close']"))
        )
        close_btn.click()
