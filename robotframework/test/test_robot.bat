@echo off
:: ����Ƿ��ṩ�˲����׼�����
if "%~1"=="" (
    ::echo �÷�: %0 [�����׼��ļ�.robot]
    ::echo ʾ��: %0 test_suit.robot
	set robot_file="./test_suit.robot"
::    pause
::    exit /b 1
)

:: ִ�� Robot Framework ����
echo ����ִ�� Robot Framework ����: %robot_file%
robot %robot_file%

:: ��ѡ����ͣ�Բ鿴���
pause