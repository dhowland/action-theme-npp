@ECHO OFF

pushd %~dp0

if "%1" == "" goto help
if "%1" == "help" goto help
if "%1" == "colors" goto colors
if "%1" == "themes" goto themes
if "%1" == "install" goto install

:help
echo usage: make.bat {colors, themes, install}
goto end

:colors
@ECHO -- .\themes\palette.html
python .\tools\palette.py .\themes
goto end

:themes
@ECHO -- .\themes\Npp.xml
@ECHO -- .\themes\Npp_colors.html
python .\tools\stylers.py .\templates\stylers.template.xml .\themes\Npp.json .\themes\Npp.xml
@ECHO -- .\themes\Action.xml
@ECHO -- .\themes\Action_colors.html
python .\tools\stylers.py .\templates\stylers.template.xml .\themes\Action.json .\themes\Action.xml
goto end

:install
@ECHO -- %APPDATA%\Notepad++\themes\Action.xml
copy ".\themes\Action.xml" "%APPDATA%\Notepad++\themes\"
goto end

:end
popd
