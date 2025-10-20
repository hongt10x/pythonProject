@echo off
:: 检查是否提供了测试套件参数
if "%~1"=="" (
    ::echo 用法: %0 [测试套件文件.robot]
    ::echo 示例: %0 test_suit.robot
	set robot_file="./test_suit.robot"
::    pause
::    exit /b 1
)

:: 执行 Robot Framework 测试
echo 正在执行 Robot Framework 测试: %robot_file%
robot %robot_file%

:: 可选：暂停以查看结果
pause