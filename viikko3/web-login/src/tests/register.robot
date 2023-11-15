*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    kalle
    Set Password    kalle1234
    Set Password Confirmation    kalle1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    a
    Set Password    kalle1234
    Set Password Confirmation    kalle1234
    Submit Credentials
    Register Should Fail With Message    Minimum length of username is 3

Register With Valid Username And Invalid Password
    Set Username    kalle
    Set Password    abcdabcd
    Set Password Confirmation    abcdabcd
    Submit Credentials
    Register Should Fail With Message    Password should not contain only letters


Register With Nonmatching Password And Password Confirmation
    Set Username    asdasdas
    Set Password    abcd1234
    Set Password Confirmation    aaa
    Submit Credentials
    Register Should Fail With Message    Password and confirmation don't match

*** Keywords ***
Reset And Go To Register Page
    Reset Application
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Submit Credentials
    Click Button    Register

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Confirmation
    [Arguments]    ${password}
    Input Password    password_confirmation    ${password}
