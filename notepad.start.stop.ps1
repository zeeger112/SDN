notepad
notepad
notepad
sleep 3
Get-Process |where ProcessName -like notepad | select id
Get-Process |where ProcessName -like notepad | Stop-Process