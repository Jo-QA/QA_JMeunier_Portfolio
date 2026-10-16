*** Variables ***
${LOGIN_USERNAME}    css:[data-test="username"]
${LOGIN_PASSWORD}    css:[data-test="password"]
${LOGIN_BUTTON}      css:[data-test="login-button"]
${LOGIN_ERROR}       css:[data-test="error"]

*** Keywords ***
Submit Credentials
    [Arguments]    ${username}    ${password}
    Input Text    ${LOGIN_USERNAME}    ${username}
    Input Password    ${LOGIN_PASSWORD}    ${password}
    Click Button    ${LOGIN_BUTTON}

Login Error Should Contain
    [Arguments]    ${message}
    Wait Until Element Is Visible    ${LOGIN_ERROR}
    Element Should Contain    ${LOGIN_ERROR}    ${message}
    Element Should Be Visible    ${LOGIN_BUTTON}
