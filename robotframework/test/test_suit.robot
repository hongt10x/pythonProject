*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://www.baidu.com
${BROWSER}        chrome

*** Test Cases ***
Test Baidu Search
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text      id=kw    Robot Framework
    Click Button    id=su
    Wait Until Page Contains    结果
    Close Browser