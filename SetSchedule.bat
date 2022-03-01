@echo off
for /f "tokens=1*" %%A in ('
  powershell -NoP -C "(Get-Date).AddMinutes(5).ToString('yyyy/MM/dd HH:mm:ss')"
') do (
  Set "MyDate=%%A"
  set "MyTime=%%B"
)
set "currdir=%~dp0"
SCHTASKS /Create /RU "%USERNAME%" /SC Hourly /MO 4 /TN TG-Report  /SD %MyDate% /ST %MyTime% /TR """"%currdir%\temp.bat""""  
pause
exit

