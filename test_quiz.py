from actions import  driver_init,check_home, enter_info, filling_form


def test_quiz():
    driver_init()
    check_home()
    enter_info('tamar', 'abraaaa@gmail.com')
    filling_form(        "SecurePassword123",        "John",     "Doe",        "Doe Inc.","123 Elm Street", "Apt 4", "New York",     "New York",       "10001",        "1234567890"   )
