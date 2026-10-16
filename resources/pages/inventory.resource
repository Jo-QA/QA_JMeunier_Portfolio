*** Variables ***
${INVENTORY_LIST}    css:[data-test="inventory-list"]
${PRODUCT_NAME}      css:[data-test="inventory-item-name"]
${PRODUCT_PRICE}     css:[data-test="inventory-item-price"]
${CART_LINK}         css:[data-test="shopping-cart-link"]
${CART_BADGE}        css:[data-test="shopping-cart-badge"]

*** Keywords ***
Inventory Should Be Ready
    Wait Until Element Is Visible    ${INVENTORY_LIST}
    Element Text Should Be    css:[data-test="title"]    Products

Add Product
    [Arguments]    ${slug}
    Click Button    css:[data-test="add-to-cart-${slug}"]
    Wait Until Element Is Visible    css:[data-test="remove-${slug}"]

Cart Badge Should Equal
    [Arguments]    ${quantity}
    Wait Until Element Is Visible    ${CART_BADGE}
    Element Text Should Be    ${CART_BADGE}    ${quantity}

Open Cart
    Click Element    ${CART_LINK}
    Wait Until Element Is Visible    css:[data-test="cart-list"]

Select Price Ascending
    Select From List By Value    css:[data-test="product-sort-container"]    lohi
    List Selection Should Be    css:[data-test="product-sort-container"]    lohi

Logout
    Click Button    id:react-burger-menu-btn
    Wait Until Element Is Visible    css:[data-test="logout-sidebar-link"]
    Click Element    css:[data-test="logout-sidebar-link"]
    Wait Until Element Is Visible    ${LOGIN_BUTTON}
