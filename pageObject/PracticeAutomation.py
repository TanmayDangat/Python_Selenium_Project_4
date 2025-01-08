import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PracticeAutomation:

    shopMenu_linkText = "Shop"
    homeMenu_linkText = "Home"
    sliders_id = "n2-ss-6-align"
    arrivals_XPATH = "//div[@class='themify_builder_sub_row clearfix gutter-default   sub_row_1-0-2']"
    image_XPATH = "(//img[@class='attachment-shop_catalog size-shop_catalog wp-post-image'])[1]"
    description_linkText = "Description"
    reviews_className = "reviews_tab"
    addToBasket_XPATH = "//button[@class='single_add_to_cart_button button alt']"
    viewBasket_className = "button.wc-forward"
    cart_className = "cart_item"
    price_XPATH = "(//span[@class='woocommerce-Price-amount amount'])[1]"
    checkOutBtn_XPATH = "//a[@class='checkout-button button alt wc-forward']"
    couponCodeLink_XPATH = "//a[@class='showcoupon']"
    couponCode_XPATH = "//input[@name='coupon_code']"
    applyCouponCodeBtn = "//input[@value='Apply Coupon']"
    image2_XPATH = "(//img[@class='attachment-shop_catalog size-shop_catalog wp-post-image'])[2]"
    addToBasket2_XPATH = "//button[@class='single_add_to_cart_button button alt']"
    errorMsg_XPATH = "//*[@id='page-35']/div/div[1]/ul/li"
    removeIcon_XPATH = "//a[@class='remove']"
    quantity_XPATH = "//input[@value='1']"
    updateBtn_XPATH = "//input[@name='update_cart']"
    subTotal_XPATH = "//td[@data-title='Subtotal']"
    finalTotal_XPATH = "(//span[@class='woocommerce-Price-amount amount'])[5]"
    firstName_XPATH = "//input[@id='billing_first_name']"
    lastName_XPATH = "//input[@id='billing_last_name']"
    companyName_XPATH = "//input[@id='billing_company']"
    email_XPATH = "//input[@id='billing_email']"
    phone_XPATH = "//input[@id='billing_phone']"
    selectCountry_XPATH = "//div[@class='select2-container country_to_state country_select']"
    selectCountryNameInput_XPATH = "//div[@id='select2-drop']/div/input[@class='select2-input']"
    selectCountryName_XPATH = "(//div[@class='select2-result-label'])[2]"
    streetAddress_XPATH = "//input[@id='billing_address_1']"
    aptNumber_XPATH = "//input[@id='billing_address_2']"
    city_XPATH = "//input[@id='billing_city']"
    state_XPATH = "//div[@class='select2-container state_select']"
    stateName_XPATH = "//input[@id='s2id_autogen2_search']"
    pincode_XPATH = "//input[@id='billing_postcode']"
    checkbox_XPATH = "//input[@id='createaccount']"
    password_XPATH = "//input[@id='account_password']"
    paymentRadioBtn_XPATH = "//input[@id='payment_method_cheque']"
    placeOrder_XPATH = "//input[@id='place_order']"


    def __init__(self,driver):
        self.driver = driver

    def setShopMenu(self):
        self.driver.find_element(By.LINK_TEXT,self.shopMenu_linkText).click()

    def setHomeMenu(self):
        self.driver.find_element(By.LINK_TEXT,self.homeMenu_linkText).click()

    def setSliders(self):
        sliders = self.driver.find_elements(By.ID,self.sliders_id)
        return sliders

    def setArrivals(self):
        arrivals = self.driver.find_elements(By.XPATH,self.arrivals_XPATH)
        return arrivals

    def setImage(self):
        self.driver.find_element(By.XPATH,self.image_XPATH).click()

    def setDescription(self):
        self.driver.find_element(By.LINK_TEXT,self.description_linkText).click()

    def setReviews(self):
        self.driver.find_element(By.CLASS_NAME,self.reviews_className).click()

    def setAddToBasket(self):
        self.driver.find_element(By.XPATH,self.addToBasket_XPATH).click()

    def setViewBasket(self):
        self.driver.find_element(By.CLASS_NAME,self.viewBasket_className).click()

    def setPrice(self):
        price = self.driver.find_element(By.XPATH,self.price_XPATH)
        return price

    def setCheckOut(self):
        self.driver.find_element(By.XPATH,self.checkOutBtn_XPATH).click()

    def setCouponCodeLink(self):
        self.driver.find_element(By.XPATH,self.couponCodeLink_XPATH).click()

    def setCouponCode(self):
        self.driver.find_element(By.XPATH,self.couponCode_XPATH).send_keys("krishnasakinala")

    def setApplyCouponCodeBtn(self):
        self.driver.find_element(By.XPATH,self.applyCouponCodeBtn).click()

    def setImage2(self):
        self.driver.find_element(By.XPATH,self.image2_XPATH).click()

    def setAddToBasket2(self):
        self.driver.find_element(By.XPATH, self.addToBasket2_XPATH).click()

    def setErrorMsg(self):
        error = self.driver.find_element(By.XPATH,self.errorMsg_XPATH)
        return error

    def setRemoveIcon(self):
        self.driver.find_element(By.XPATH,self.removeIcon_XPATH).click()

    def setQuantity(self):
        self.driver.find_element(By.XPATH, self.quantity_XPATH).clear()
        self.driver.find_element(By.XPATH,self.quantity_XPATH).send_keys(3)

    def setUpdate(self):
        self.driver.find_element(By.XPATH,self.updateBtn_XPATH).click()

    def setSubTotal(self):
        subtotal = self.driver.find_element(By.XPATH,self.subTotal_XPATH)
        return subtotal

    def setFinalTotal(self):
        finalTotal = self.driver.find_element(By.XPATH,self.finalTotal_XPATH)
        return finalTotal

    def setFirstName(self):
        self.driver.find_element(By.XPATH,self.firstName_XPATH).clear()
        self.driver.find_element(By.XPATH,self.firstName_XPATH).send_keys("Rahul")

    def setLastName(self):
        self.driver.find_element(By.XPATH,self.lastName_XPATH).clear()
        self.driver.find_element(By.XPATH,self.lastName_XPATH).send_keys("Patil")

    def setCompanyName(self):
        self.driver.find_element(By.XPATH,self.companyName_XPATH).clear()
        self.driver.find_element(By.XPATH,self.companyName_XPATH).send_keys("TCS")

    def setEmail(self):
        self.driver.find_element(By.XPATH,self.email_XPATH).clear()
        self.driver.find_element(By.XPATH,self.email_XPATH).send_keys("rahul@test.com")

    def setPhone(self):
        self.driver.find_element(By.XPATH,self.phone_XPATH).clear()
        self.driver.find_element(By.XPATH,self.phone_XPATH).send_keys("1234567890")

    def setCountry(self):
        self.driver.find_element(By.XPATH, self.selectCountry_XPATH).click()
        inputCountry = self.driver.find_element(By.XPATH,self.selectCountryNameInput_XPATH)
        inputCountry.send_keys("India")
        inputCountry.send_keys(Keys.ENTER)
        # self.driver.find_element(By.XPATH, self.selectCountryName_XPATH).click()

    def setStreetAddress(self):
        self.driver.find_element(By.XPATH, self.streetAddress_XPATH).clear()
        self.driver.find_element(By.XPATH, self.streetAddress_XPATH).send_keys("Wonder street")

    def setAptNumber(self):
        self.driver.find_element(By.XPATH, self.aptNumber_XPATH).clear()
        self.driver.find_element(By.XPATH, self.aptNumber_XPATH).send_keys("3")

    def setCity(self):
        self.driver.find_element(By.XPATH,self.city_XPATH).clear()
        self.driver.find_element(By.XPATH,self.city_XPATH).send_keys("Pune")

    def setState(self):
        self.driver.find_element(By.XPATH,self.state_XPATH).click()
        drpState = self.driver.find_element(By.XPATH,self.stateName_XPATH)
        drpState.send_keys("Maharashtra")
        drpState.send_keys(Keys.ENTER)
        return drpState

    def setPincode(self):
        self.driver.find_element(By.XPATH,self.pincode_XPATH).clear()
        self.driver.find_element(By.XPATH,self.pincode_XPATH).send_keys("123456")

    def setCheckbox(self):
        self.driver.find_elements(By.XPATH,self.checkbox_XPATH).click()

    def setPassword(self):
        self.driver.find_element(By.XPATH,self.password_XPATH).send_keys("RahulPatil!1")

    def setPaymentRadioBtn(self):
        self.driver.find_element(By.XPATH,self.paymentRadioBtn_XPATH).click()

    def setPlaceOrder(self):
        self.driver.find_element(By.XPATH,self.placeOrder_XPATH).click()
