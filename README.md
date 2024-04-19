# README: User Registration Test Case

## Overview
This README document details the automated test case designed for user registration, login, and account deletion on [Automation Exercise](http://automationexercise.com). It outlines the steps involved in ensuring that the user registration process functions as expected.

## Tools and Technologies
- **Selenium WebDriver**: For automating web browser interaction.
- **Python**: Scripting language used to write the test.
- **Pytest**: Python testing framework used for running the test.

### Test Steps
1. **Launch Browser**: Start a Chrome or Firefox browser session.
2. **Navigate to URL**: Open 'http://automationexercise.com'.
3. **Verify Home Page**: Check that the home page is loaded and visible.
4. **Click Signup/Login**: Navigate to the 'Signup / Login' button and click it.
5. **Check Signup Section**: Ensure the 'New User Signup!' section is visible.
6. **Enter Name and Email**: Fill the name and email address fields.
7. **Click Signup**: Submit the signup form.
8. **Account Information Page**: Confirm visibility of 'ENTER ACCOUNT INFORMATION'.
9. **Fill Account Details**: Enter required details like title, name, email, password, and date of birth.
10. **Select Checkboxes**: Opt-in for newsletters and special offers.
11. **Complete Personal Info**: Provide details such as first name, last name, company, address, country, state, city, zipcode, and mobile number.
12. **Create Account**: Submit all information by clicking the 'Create Account' button.
13. **Confirm Account Creation**: Verify the message 'ACCOUNT CREATED!' is displayed.
14. **Continue**: Click the 'Continue' button after account creation.
15. **Verify Login**: Ensure the 'Logged in as username' message is visible.
16. **Delete Account**: Click the 'Delete Account' button.
17. **Verify Account Deletion**: Check that the 'ACCOUNT DELETED!' message appears and click 'Continue'.

