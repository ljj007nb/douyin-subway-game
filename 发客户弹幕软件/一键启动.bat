@echo off&cd %~dp0&color 0a
echo %cd%
echo 留空指直接回车
set /p url=请输入抖音直播间地址(留空不填默认监听上次的直播间): 
if "%url%"=="" (
	echo 开始运行 请勿关闭此窗口 否则会接收不到弹幕
	start cmd /k python webChat.py
	python webDriver.py
) else (
	(
		echo.def url^(^):
		echo.    return "%url%"
	)>live_url.py
	echo 开始运行 请勿关闭此窗口 否则会接收不到弹幕
	start cmd /k python webChat.py
	python webDriver.py
)
pause