*** Settings ***
Documentation    Public demo only. Business oracles are inferred hypotheses H-01 to H-14.
Resource         ../../resources/common.resource
Test Setup       Open Fresh Login
Test Teardown    Finish Test
Test Timeout     90 seconds

*** Test Cases ***
TC01 Valid Login Opens Inventory
    [Tags]    smoke    regression    TC01    H-01    R-01
    Login As Standard User
    Element Should Not Be Visible    ${LOGIN_BUTTON}

TC02 Locked User Is Refused
    [Tags]    regression    negative    TC02    H-02    R-01
    Submit Credentials    ${LOCKED_USERNAME}    ${DEMO_PASSWORD}
    Login Error Should Contain    Sorry, this user has been locked out.
    Element Should Not Be Visible    ${INVENTORY_LIST}

TC03 Wrong Password Is Refused
    [Tags]    regression    negative    TC03    H-02    R-01
    Submit Credentials    ${DEMO_USERNAME}    invalid-demo-password
    Login Error Should Contain    Username and password do not match any user in this service
    Element Should Not Be Visible    ${INVENTORY_LIST}

TC06 Logout Returns To Login
    [Tags]    smoke    regression    TC06    H-04    R-01
    Login As Standard User
    Logout
    Element Should Not Be Visible    ${INVENTORY_LIST}
    Go To    ${BASE_URL}inventory.html
    Wait Until Element Is Visible    ${LOGIN_BUTTON}
    Element Should Not Be Visible    ${INVENTORY_LIST}

TC09 Prices Sort Ascending
    [Tags]    regression    TC09    H-06    R-05
    Login As Standard User
    ${before}=    Get Texts From Elements    ${PRODUCT_PRICE}
    Select Price Ascending
    ${after}=    Get Texts From Elements    ${PRODUCT_PRICE}
    Lists Should Be Equal    ${before}    ${after}    ignore_order=True
    Prices Should Be Ascending    ${after}

TC13 Add One Product
    [Tags]    smoke    regression    TC13    H-07    R-02
    Login As Standard User
    Add Product    sauce-labs-backpack
    Cart Badge Should Equal    1
    Open Cart
    Cart Should Contain Names    Sauce Labs Backpack
    Element Text Should Be    ${PRODUCT_PRICE}    $29.99

TC14 Add Two Distinct Products
    [Tags]    smoke    regression    TC14    H-07    R-02
    Login As Standard User
    Add Product    sauce-labs-backpack
    Add Product    sauce-labs-bike-light
    Cart Badge Should Equal    2
    Open Cart
    Cart Should Contain Names    Sauce Labs Backpack    Sauce Labs Bike Light

TC15 Remove One Product From Cart
    [Tags]    regression    TC15    H-07    R-02
    Login As Standard User
    Add Product    sauce-labs-backpack
    Add Product    sauce-labs-bike-light
    Open Cart
    Remove Product From Cart    sauce-labs-backpack
    Cart Badge Should Equal    1
    Cart Should Contain Names    Sauce Labs Bike Light

TC17 Cart Persists After Reload
    [Tags]    regression    TC17    H-08    R-03
    Login As Standard User
    Add Product    sauce-labs-backpack
    Open Cart
    Reload Page
    Wait Until Element Is Visible    css:[data-test="cart-list"]
    Cart Badge Should Equal    1
    Cart Should Contain Names    Sauce Labs Backpack

TC19 Checkout Requires All Identity Fields
    [Tags]    regression    negative    TC19    H-09    R-04
    Login As Standard User
    Add Product    sauce-labs-backpack
    Open Cart
    Start Checkout
    Continue Checkout
    Checkout Error Should Be    Error: First Name is required
    Fill Checkout Identity    first=Camille    last=${EMPTY}    postal=${EMPTY}
    Continue Checkout
    Checkout Error Should Be    Error: Last Name is required
    Fill Checkout Identity    first=Camille    last=Test    postal=${EMPTY}
    Continue Checkout
    Checkout Error Should Be    Error: Postal Code is required

TC21 Checkout Amounts Are Consistent
    [Tags]    smoke    regression    TC21    H-11    R-02
    Login As Standard User
    Add Product    sauce-labs-backpack
    Add Product    sauce-labs-bike-light
    Open Cart
    Start Checkout
    Fill Checkout Identity
    Continue Checkout
    Overview Should Be Ready
    Cart Should Contain Names    Sauce Labs Backpack    Sauce Labs Bike Light
    Check Overview Totals

TC22 Complete Order Clears Cart
    [Tags]    smoke    regression    TC22    H-12    R-07
    Login As Standard User
    Add Product    sauce-labs-backpack
    Open Cart
    Start Checkout
    Fill Checkout Identity
    Continue Checkout
    Overview Should Be Ready
    Finish Order
    Element Should Not Be Visible    ${CART_BADGE}
    Click Button    css:[data-test="back-to-products"]
    Inventory Should Be Ready
    Open Cart
    ${items}=    Get Element Count    ${CART_ITEMS}
    Should Be Equal As Integers    ${items}    0
