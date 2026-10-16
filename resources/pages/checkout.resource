*** Variables ***
${FIRST_NAME}    css:[data-test="firstName"]
${LAST_NAME}     css:[data-test="lastName"]
${POSTAL_CODE}   css:[data-test="postalCode"]

*** Keywords ***
Fill Checkout Identity
    [Arguments]    ${first}=Camille    ${last}=Test    ${postal}=75001
    Input Text    ${FIRST_NAME}    ${first}
    Input Text    ${LAST_NAME}    ${last}
    Input Text    ${POSTAL_CODE}    ${postal}

Continue Checkout
    Click Button    css:[data-test="continue"]

Checkout Error Should Be
    [Arguments]    ${expected}
    Wait Until Element Is Visible    css:[data-test="error"]
    Element Text Should Be    css:[data-test="error"]    ${expected}
    Element Should Be Visible    ${FIRST_NAME}

Overview Should Be Ready
    Wait Until Element Is Visible    css:[data-test="checkout-summary-container"]
    Element Text Should Be    css:[data-test="title"]    Checkout: Overview

Check Overview Totals
    ${prices}=    Get Texts From Elements    ${PRODUCT_PRICE}
    ${subtotal}=    Get Text    css:[data-test="subtotal-label"]
    ${tax}=    Get Text    css:[data-test="tax-label"]
    ${total}=    Get Text    css:[data-test="total-label"]
    Totals Should Be Consistent    ${prices}    ${subtotal}    ${tax}    ${total}

Finish Order
    Click Button    css:[data-test="finish"]
    Wait Until Element Is Visible    css:[data-test="complete-header"]
    Element Text Should Be    css:[data-test="complete-header"]    Thank you for your order!
    Capture Page Screenshot    order-complete.png
