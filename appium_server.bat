@ECHO OFF&PUSHD %~DP0 &TITLE appium服务一键启动
mode con cols=100 lines=60
color 9f
:starthome
cls
set a=^set /p=■%b%^<nul^&ping/n 0 127.1^>nul^&
echo.
echo.
echo.
echo 服务正在初始化. . .
echo.
echo ┌────────────────────────────────────┐
set/p=<nul&%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%%a%
echo 100%%
echo └────────────────────────────────────┘



set a=%cd%
set b=%DATE:~0,4%-%DATE:~5,2%-%DATE:~8,2%
set c=%time:~,2%
echo ---------------------------------------
echo .	leiyong711@163.com
echo ---------------------------------------
echo ---------------------------------------
echo .
echo .	      为了炫酷
echo .
echo .          
echo .         ╭══╮　 ┌═══════┐
echo .      ╭╯ 让路 ║═║   BUG专用车  ║
echo .     └══⊙═⊙═~----╰⊙═══⊙╯
echo .
echo .
echo .
echo ---------------------------------------
echo .
IF EXIST  %a%\Report\%b%\%c%\log (
	echo .	%a%\Report\%b%\%c%\log 文件夹已存在，等待开启服务...
) ELSE (
    echo .	%a%\Report\%b%\%c%\log 文件夹不存在，正在创建中...
	MD %a%\Report\%b%\%c%\log
	IF EXIST  %a%\Report\%b%\%c%\log (
		echo .	文件夹创建成功。
	) ELSE (
		echo .	文件夹创建失败！！！
		pause
	)
)
echo .
echo .	直到出现五条info日志输出，则服务开启成功...
echo .
echo .
appium -a 127.0.0.1 -p 4723 --log %a%\report\%b%\%c%\log\appium.log


pause