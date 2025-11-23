@echo off
setlocal

:: -----------------------------
:: Step 1: Get WSL2 IP
:: -----------------------------
for /f "tokens=*" %%i in ('wsl hostname -I') do set WSL_IP=%%i

:: Take first IP (if multiple)
for /f "tokens=1" %%i in ("%WSL_IP%") do set WSL_IP=%%i

echo Detected WSL IP: %WSL_IP%

:: -----------------------------
:: Step 2: Update frontend JSX
:: -----------------------------
set FRONTEND_FILE=web\src\GMPanel.jsx

:: Replace the line with socket.io init
powershell -Command "(gc %FRONTEND_FILE%) -replace 'const socket = io\\(.*\\);', 'const socket = io(\"http://%WSL_IP%:3001\");' | Set-Content %FRONTEND_FILE%"

echo Frontend socket address updated.

:: -----------------------------
:: Step 3: Start backend
:: -----------------------------
start "" wsl bash -c "cd game && python3 main.py"

:: -----------------------------
:: Step 4: Start frontend
:: -----------------------------
start "" cmd /k "cd web && npm install && npm run dev"

endlocal
