# project_on_autotesting
My autotest project

Test site - http://selenium1py.pythonanywhere.com/

Tests are described according to the methodology of object-oriented programming

Described fixtures for running tests in chrome and firefox browsers on the command line which browser to use (--browser_name) and in which language (--language)

Automated checks:

Main page (test_main_page.py)
- the guest sees a link to the login page from the main page
- the guest goes to the login page, check the presence of login and registration forms on the page
- the guest goes to the cart from the main page, the cart is empty
- the guest sees the language switcher on the main page
- check the language switch on the main page

Product page (test_product_page.py)
- adding an item to the cart, check that the item has been added to the cart, compare the price of the item with the amount of the cart
- the product has been added to the cart, but the guest does not see a message about adding the product to the cart (negative check)
- check that the guest does not see a message about adding an item to the cart
- check that the success message is gone after adding the product to the cart (negative check)
- check that the guest sees the login link on the product page
- guest can go to the login page from the product page
- check that the guest. can switch language on product page
- search string, check that the output matches what you are looking for
- authorization, success message, the user can add the product to the cart
