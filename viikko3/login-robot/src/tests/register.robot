*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  alle  abcd1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  abcd1234
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  aa  abcd1234
    Output Should Contain  Minimum length of username is 3

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ab1  abcd1234
    Output Should Contain  Username should only contain lowercase letters

Register With Valid Username And Too Short Password
    Input Credentials  abc  abcd123
    Output Should Contain  Minimum length of password is 8

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  abc  abcdabcd
    Output Should Contain  Password should not contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command