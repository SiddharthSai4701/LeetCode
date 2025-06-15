@echo off
REM leetcode_push.bat - Batch script for Windows
REM Usage: leetcode_push.bat 567
REM Or: leetcode_push.bat (will prompt for problem number)

setlocal enabledelayedexpansion

REM Check if problem number is provided as argument
if "%1"=="" (
    set /p PROBLEM_NUM="Enter LeetCode problem number: "
) else (
    set PROBLEM_NUM=%1
)

REM Validate input
if "!PROBLEM_NUM!"=="" (
    echo Error: Problem number cannot be empty
    pause
    exit /b 1
)

REM Check if we're in a git repository
git status >nul 2>&1
if errorlevel 1 (
    echo Error: Not in a git repository
    pause
    exit /b 1
)

echo.
echo =====================================
echo  LeetCode Problem !PROBLEM_NUM! - Git Push
echo =====================================
echo.

REM Show current status
echo Current git status:
git status --short

echo.
echo Adding all files...
git add .

if errorlevel 1 (
    echo Error: Failed to add files
    pause
    exit /b 1
)

echo.
echo Committing with message "Solved !PROBLEM_NUM!"...
git commit -m "Solved !PROBLEM_NUM!"

@REM if errorlevel 1 (
@REM     echo Error: Failed to commit (maybe no changes to commit?)
@REM     pause
@REM     exit /b 1
@REM )

echo.
echo Pushing to remote repository...
git push

if errorlevel 1 (
    echo Error: Failed to push to remote repository
    pause
    exit /b 1
)

echo.
echo ✅ Successfully pushed LeetCode problem !PROBLEM_NUM!
echo.
pause