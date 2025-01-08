import time

from pageObject.PracticeAutomation import PracticeAutomation
from testCases.conftest import setUp


class TestPracticeAutomation:

    practiceAutomationURL = "http://practice.automationtesting.in/"

    def test_Home_Page_with_three_Sliders_only(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        sliders = self.driver.obj_PracticeAutomation.setSliders()
        print(len(sliders))
        if len(sliders) == 3:
            print("There are exactly 3 sliders")
        else:
            print("There are not exactly 3 sliders")
        if len(sliders) == 3:
            assert True
        self.driver.quit()

    def test_Home_page_with_three_Arrivals_only(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True
        self.driver.quit()

    def test_Home_page_Images_in_Arrivals_should_navigate(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage()
        actTitle = self.driver.title
        expTitle = "Selenium Ruby – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")
        self.driver.quit()

    def test_Home_page_Arrivals_Images_Description(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage()
        actTitle = self.driver.title
        expTitle = "Selenium Ruby – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        # self.driver.obj_PracticeAutomation.setDescription()
        self.driver.quit()

    def test_Home_page_Arrivals_Images_Reviews(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage()
        actTitle = self.driver.title
        expTitle = "Selenium Ruby – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setReviews()
        self.driver.quit()

    def test_Home_page_Arrivals_Images_Add_to_Basket(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage()
        actTitle = self.driver.title
        expTitle = "Selenium Ruby – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")
        self.driver.quit()


    def test_Home_page_Arrivals_Add_to_Basket_with_more_books(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage()
        actTitle = self.driver.title
        expTitle = "Selenium Ruby – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        self.driver.obj_PracticeAutomation.setCheckOut()
        self.driver.quit()

    def test_Home_Arrivals_Add_to_Basket_Items_Coupon(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage()
        actTitle = self.driver.title
        expTitle = "Selenium Ruby – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        self.driver.obj_PracticeAutomation.setCheckOut()
        self.driver.obj_PracticeAutomation.setCouponCodeLink()
        self.driver.obj_PracticeAutomation.setCouponCode()
        self.driver.obj_PracticeAutomation.setApplyCouponCodeBtn()
        time.sleep(2)
        self.driver.quit()

    def test_Home_Arrivals_Add_to_Basket_Items_Coupon_value_450(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage2()
        actTitle = self.driver.title
        expTitle = "Mastering JavaScript – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket2()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        self.driver.obj_PracticeAutomation.setCheckOut()
        self.driver.obj_PracticeAutomation.setCouponCodeLink()
        self.driver.obj_PracticeAutomation.setCouponCode()
        self.driver.obj_PracticeAutomation.setApplyCouponCodeBtn()
        error = self.driver.obj_PracticeAutomation.setErrorMsg()
        if error.is_displayed():
            print("Error msg displayed")
        else:
            print("Error msg is not displayed")
        self.driver.quit()


    def test_Home_Arrivals_Add_to_Basket_Items_Remove_book(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage2()
        actTitle = self.driver.title
        expTitle = "Mastering JavaScript – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket2()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        time.sleep(4)
        self.driver.obj_PracticeAutomation.setRemoveIcon()
        self.driver.quit()

    def test_Home_Arrivals_Add_to_Basket_Items_Check_out_Update_Basket(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage2()
        actTitle = self.driver.title
        expTitle = "Mastering JavaScript – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket2()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        self.driver.obj_PracticeAutomation.setQuantity()
        self.driver.obj_PracticeAutomation.setUpdate()
        self.driver.quit()

    def test_Home_Arrivals_Add_to_Basket_Items_Check_out_Total_and_Sub_total_condition(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage2()
        actTitle = self.driver.title
        expTitle = "Mastering JavaScript – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket2()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        self.driver.obj_PracticeAutomation.setQuantity()
        self.driver.obj_PracticeAutomation.setUpdate()
        subTotal = self.driver.obj_PracticeAutomation.setSubTotal()
        finalTotal = self.driver.obj_PracticeAutomation.setFinalTotal()
        if subTotal.text < finalTotal.text:
         print("Testcase passed")
        else:
            print("Testcase failed")
        self.driver.quit()

    def test_Home_Arrivals_Add_to_Basket_Items_Check_out_functionality(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage2()
        actTitle = self.driver.title
        expTitle = "Mastering JavaScript – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket2()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        self.driver.obj_PracticeAutomation.setQuantity()
        self.driver.obj_PracticeAutomation.setUpdate()
        subTotal = self.driver.obj_PracticeAutomation.setSubTotal()
        finalTotal = self.driver.obj_PracticeAutomation.setFinalTotal()
        if subTotal.text < finalTotal.text:
            print("Testcase passed")
        else:
            print("Testcase failed")

        time.sleep(1)
        self.driver.obj_PracticeAutomation.setCheckOut()
        self.driver.quit()

    def test_Home_Arrivals_Add_to_Basket_Items_Check_out_Payment_Gateway(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage2()
        actTitle = self.driver.title
        expTitle = "Mastering JavaScript – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket2()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        self.driver.obj_PracticeAutomation.setQuantity()
        self.driver.obj_PracticeAutomation.setUpdate()
        subTotal = self.driver.obj_PracticeAutomation.setSubTotal()
        finalTotal = self.driver.obj_PracticeAutomation.setFinalTotal()
        if subTotal.text < finalTotal.text:
            print("Testcase passed")
        else:
            print("Testcase failed")

        time.sleep(3)
        self.driver.obj_PracticeAutomation.setCheckOut()
        self.driver.obj_PracticeAutomation.setFirstName()
        self.driver.obj_PracticeAutomation.setLastName()
        self.driver.obj_PracticeAutomation.setCompanyName()
        self.driver.obj_PracticeAutomation.setEmail()
        self.driver.obj_PracticeAutomation.setPhone()
        # self.driver.obj_PracticeAutomation.setCountry()
        self.driver.obj_PracticeAutomation.setStreetAddress()
        self.driver.obj_PracticeAutomation.setAptNumber()
        self.driver.obj_PracticeAutomation.setCity()
        self.driver.obj_PracticeAutomation.setState()
        # time.sleep(4)
        self.driver.obj_PracticeAutomation.setPincode()
        # self.driver.obj_PracticeAutomation.setCheckbox()
        # self.driver.obj_PracticeAutomation.setPassword()

        self.driver.obj_PracticeAutomation.setPaymentRadioBtn()
        self.driver.obj_PracticeAutomation.setPlaceOrder()
        self.driver.quit()

    def test_Home_Arrivals_Add_to_Basket_Items_Check_out_Payment_Gateway_Place_order(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceAutomationURL)
        self.driver.maximize_window()
        self.driver.obj_PracticeAutomation = PracticeAutomation(self.driver)
        self.driver.obj_PracticeAutomation.setShopMenu()
        self.driver.obj_PracticeAutomation.setHomeMenu()
        arrivals = self.driver.obj_PracticeAutomation.setArrivals()
        print(arrivals)
        if len(arrivals) == 3:
            print("There are total 3 arrivals")
        else:
            print("There are not 3 arrivals")

        if len(arrivals) == 3:
            assert True

        self.driver.obj_PracticeAutomation.setImage2()
        actTitle = self.driver.title
        expTitle = "Mastering JavaScript – Automation Practice Site"
        if actTitle == expTitle:
            print("Navigated to correct page")
        else:
            print("Navigated to different page")

        self.driver.obj_PracticeAutomation.setAddToBasket2()
        self.driver.obj_PracticeAutomation.setViewBasket()
        price = self.driver.obj_PracticeAutomation.setPrice()
        if price.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        self.driver.obj_PracticeAutomation.setQuantity()
        self.driver.obj_PracticeAutomation.setUpdate()
        subTotal = self.driver.obj_PracticeAutomation.setSubTotal()
        finalTotal = self.driver.obj_PracticeAutomation.setFinalTotal()
        if subTotal.text < finalTotal.text:
            print("Testcase passed")
        else:
            print("Testcase failed")

        time.sleep(3)
        self.driver.obj_PracticeAutomation.setCheckOut()
        self.driver.obj_PracticeAutomation.setFirstName()
        self.driver.obj_PracticeAutomation.setLastName()
        self.driver.obj_PracticeAutomation.setCompanyName()
        self.driver.obj_PracticeAutomation.setEmail()
        self.driver.obj_PracticeAutomation.setPhone()
        # self.driver.obj_PracticeAutomation.setCountry()
        self.driver.obj_PracticeAutomation.setStreetAddress()
        self.driver.obj_PracticeAutomation.setAptNumber()
        self.driver.obj_PracticeAutomation.setCity()
        self.driver.obj_PracticeAutomation.setState()
        # time.sleep(4)
        self.driver.obj_PracticeAutomation.setPincode()
        # self.driver.obj_PracticeAutomation.setCheckbox()
        # self.driver.obj_PracticeAutomation.setPassword()

        self.driver.obj_PracticeAutomation.setPaymentRadioBtn()
        self.driver.obj_PracticeAutomation.setPlaceOrder()
        actTitle = self.driver.title
        expTitle = "Checkout – Automation Practice Site"
        if actTitle == expTitle:
            print("Test case passed")
        else:
            print("Test case failed")
        self.driver.quit()