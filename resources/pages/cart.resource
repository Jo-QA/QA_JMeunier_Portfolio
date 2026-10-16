*** Variables ***
${CART_ITEMS}    css:[data-test="inventory-item"]

*** Keywords ***
Cart Should Contain Names
    [Arguments]    @{expected}
    ${actual}=    Get Texts From Elements    ${PRODUCT_NAME}
    Lists Should Be Equal    ${actual}    ${expected}    ignore_order=True
    ${count}=    Get Length    ${expected}
    ${expected_quantity}=    Convert To String    1
    ${quantities}=    Get Texts From Elements    css:[data-test="item-quantity"]
    Length Should Be    ${quantities}    ${count}
    FOR    ${quantity}    IN    @{quantities}
        Should Be Equal    ${quantity}    ${expected_quantity}
    END

Remove Product From Cart
    [Arguments]    ${slug}
    Click Button    css:[data-test="remove-${slug}"]
    Wait Until Element Is Not Visible    css:[data-test="remove-${slug}"]

Start Checkout
    Click Button    css:[data-test="checkout"]
    Wait Until Element Is Visible    css:[data-test="firstName"]
