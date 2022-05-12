@echo off&color 0a&cd %~dp0
echo 本工具用于清理此脚本日常获取的弹幕文件和图片文件 按任意键开始清理 取消清理请关闭窗口
pause
rd /s /q douyinLiveFile
rd /s /q userImages
echo 清理完毕!
pause