@echo off
START /W curl -o python_installer.exe https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
START /W python_installer.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0 Include_pip=1
mkdir python_project
cd python_project
git clone https://github.com/MansorY23/auto-excel.git
cd auto-excel
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt

schtasks /create /sc daily /tn auto-excel /tr C:\Users\%username%\Desktop\python_project\auto-excel\start.bat /st 19:30