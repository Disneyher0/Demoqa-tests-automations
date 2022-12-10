import pytest
from selene import have
from selene.support.shared import browser
#browser.config.hold_browser_open = True
def test_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Sergey')
    browser.element('[id="lastName"]').type('Sobolev')
    browser.element('[id="userEmail"]').type('sobolev.s@mail.ru')
    browser.element('[class="custom-control-label"]').click()
    browser.element('[id="userNumber"]').type('7777777777')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1991"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="6"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--031"]').click()
    browser.element('[id="subjectsInput"]').type('hi').press_enter().type('E').press_enter().type('A').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()



    browser.element('[id="uploadPicture"]').send_keys(r"/Users/darkwing_duck/Desktop/1626c37fd018bafe840a548bd30c749e.jpeg")
    browser.element('[id="currentAddress"]').type('Russia, Moscow')
    browser.element('[id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').type('Noida').press_enter()
    browser.element('[id="submit"]').press_enter()

    browser.element(".table-responsive").should(have.text("Sergey"))
    browser.element(".table-responsive").should(have.text("Sobolev"))
    browser.element(".table-responsive").should(have.text("sobolev.s@mail.ru"))
    browser.element(".table-responsive").should(have.text("Male"))
    browser.element(".table-responsive").should(have.text("7777777777"))
    browser.element(".table-responsive").should(have.text("English"))
    browser.element(".table-responsive").should(have.text("Hindi"))
    browser.element(".table-responsive").should(have.text("Maths"))
    browser.element(".table-responsive").should(have.text("Russia, Moscow"))
    browser.element(".table-responsive").should(have.text("NCR"))
    browser.element(".table-responsive").should(have.text("Noida"))


