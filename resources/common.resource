*** Settings ***
Variables   ../variables/settings.py
Library     SeleniumLibrary    timeout=${UI_TIMEOUT}    run_on_failure=NOTHING
Library     Collections
Library     ../libraries/QualityLibrary.py
Resource    pages/login.resource
Resource    pages/inventory.resource
Resource    pages/cart.resource
Resource    pages/checkout.resource

*** Keywords ***
Open Fresh Login
    Open Isolated Chrome
    Go To    ${BASE_URL}
    Wait Until Element Is Visible    ${LOGIN_BUTTON}

Finish Test
    TRY
        Capture Test Evidence
    FINALLY
        Close All Browsers
    END

Login As Standard User
    Submit Credentials    ${DEMO_USERNAME}    ${DEMO_PASSWORD}
    Inventory Should Be Ready

Get Texts From Elements
    [Arguments]    ${locator}
    ${elements}=    Get WebElements    ${locator}
    ${texts}=    Create List
    FOR    ${element}    IN    @{elements}
        ${text}=    Get Text    ${element}
        Append To List    ${texts}    ${text}
    END
    RETURN    ${texts}
