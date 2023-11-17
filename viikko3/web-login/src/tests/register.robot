*** Settings ***
Resource            resource.robot
Resource            login_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    kalle
    Set Password    kalle1234
    Set Password Confirmation    kalle1234
    Submit Register Form
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    a
    Set Password    kalle1234
    Set Password Confirmation    kalle1234
    Submit Register Form
    Register Should Fail With Message    Minimum length of username is 3

Register With Valid Username And Invalid Password
    Set Username    kalle
    Set Password    abcdabcd
    Set Password Confirmation    abcdabcd
    Submit Register Form
    Register Should Fail With Message    Password should not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username    asdasdas
    Set Password    abcd1234
    Set Password Confirmation    aaa
    Submit Register Form
    Register Should Fail With Message    Password and confirmation don't match

Login After Successful Registration
    Set Username    kalle
    Set Password    kalle1234
    Set Password Confirmation    kalle1234
    Submit Register Form

    Go To Login Page
    Set Username    kalle
    Set Password    kalle1234
    Click Button    Login
