

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


def driver_init():
    driver.get('https://www.automationexercise.com/')
    driver.maximize_window()


def check_home():
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.home))
    driver.find_element(*Locators.signUp).click()
    #WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.signUpText))


def enter_info(name, email):
    driver.find_element(*Locators.nameInput).send_keys(name)
    driver.find_element(*Locators.emailInput).send_keys(email)
    driver.find_element(*Locators.signUpButton).click()
    #WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.accountInfo))


def filling_form(password, firstname, lastname, company, address1, address2, state, city, zipcode, mobile):
    driver.find_element(*Locators.gender).click()
    driver.find_element(*Locators.newsletter).click()
    driver.find_element(*Locators.offers).click()
    driver.find_element(*Locators.password).send_keys(password)
    Select(driver.find_element(*Locators.day)).select_by_index(3)
    Select(driver.find_element(*Locators.year)).select_by_visible_text('1998')
    Select(driver.find_element(*Locators.month)).select_by_index(3)

    driver.find_element(*Locators.firstName).send_keys(firstname)
    driver.find_element(*Locators.lastName).send_keys(lastname)
    driver.find_element(*Locators.company).send_keys(company)

    driver.find_element(*Locators.address1).send_keys(address1)
    driver.find_element(*Locators.address2).send_keys(address2)

    Select(driver.find_element(*Locators.country)).select_by_visible_text('Canada')

    driver.find_element(*Locators.state).send_keys(state)
    driver.find_element(*Locators.city).send_keys(city)
    driver.find_element(*Locators.zipCode).send_keys(zipcode)
    driver.find_element(*Locators.mobileNumber).send_keys(mobile)

    driver.find_element(*Locators.createAcc).click()
    #WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.accountCreatedText))
    driver.find_element(*Locators.continueButton).click()
    #WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.text))
    driver.find_element(*Locators.delete).click()
    #WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.deleteText))


