@echo off&cd %~dp0&color 0a
echo %cd%
echo ����ֱָ�ӻس�
set /p url=�����붶��ֱ�����ַ(���ղ���Ĭ�ϼ����ϴε�ֱ����): 
if "%url%"=="" (
	echo ��ʼ���� ����رմ˴��� �������ղ�����Ļ
	start cmd /k python webChat.py
	python webDriver.py
) else (
	(
		echo.def url^(^):
		echo.    return "%url%"
	)>live_url.py
	echo ��ʼ���� ����رմ˴��� �������ղ�����Ļ
	start cmd /k python webChat.py
	python webDriver.py
)
pause