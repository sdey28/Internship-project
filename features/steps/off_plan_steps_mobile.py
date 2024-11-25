from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open the main page mobile')
def open_target_main_page(context):
    context.app.reelly_app_mobile.open_main()


@when('Input user name mobile')
def user_name(context):
    context.app.main_page.input_username()



@when('Input user password mobile')
def user_password(context):
    context.app.main_page.input_password()




@when('Click continue button mobile')
def continue_button(context):
    context.app.main_page.verify_continue_btn()




@then('Click on “off plan” at the left side menu mobile')
def off_plan(context):
    context.app.reelly_app_mobile.off_plan_mobile()
    sleep(5)




@then('Verify the right page opens mobile')
def verify_right_page(context):
    context.app.reelly_app_mobile.verify_page_mobile()
    sleep(5)



@then('Click on filter mobile')
def filter_button(context):
    context.app.reelly_app_mobile.filter_btn_mobile()
    sleep(4)



@then('Input products price from 1200000 mobile')
def input_price_from(context):
    context.app.reelly_app_mobile.input_price_from()
    sleep(4)



@then('Input product price to 2000000 mobile')
def input_price_to(context):
    context.app.reelly_app_mobile.input_price_to()
    sleep(4)



@then('Click on apply filter mobile')
def apply_filter(context):
    context.app.reelly_app_mobile.click_apply_flr_mobile()
    sleep(4)



@then('Verify the price in all cards is inside the range 1200000 - 2000000 mobile')
def verify_price(context):
    context.app.reelly_app_mobile.verify_price_in_range_mobile()













