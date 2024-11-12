from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open the main page')
def open_target_main_page(context):
    context.app.main_page.open_main()


@when('Input user name')
def user_name(context):
    context.app.main_page.input_username()



@when('Input user password')
def user_password(context):
    context.app.main_page.input_password()




@when('Click continue button')
def continue_button(context):
    context.app.main_page.verify_continue_btn()




@then('Click on “off plan” at the left side menu')
def off_plan(context):
    context.app.main_page.side_nav()
    sleep(5)




@then('Verify the right page opens')
def verify_right_page(context):
    context.app.main_page.verify_page()
    sleep(5)



@then('Click on filter')
def filter_button(context):
    context.app.main_page.filter_btn()
    sleep(4)



@then('Input products price from 1200000')
def input_price_from(context):
    context.app.main_page.input_price_from()
    sleep(4)



@then('Input product price to 2000000')
def input_price_to(context):
    context.app.main_page.input_price_to()
    sleep(4)



@then('Click on apply filter')
def apply_filter(context):
    context.app.main_page.click_apply_flr()
    sleep(4)



@then('Verify the price in all cards is inside the range 1200000 - 2000000')
def verify_price(context):
    context.app.main_page.verify_price_in_range()













