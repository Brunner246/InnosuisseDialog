@echo off
set SOURCE_PATH=D:\Python\PycharmProjects\InnosuisseDialog
set DESTINATION_PATH=D:\cadwork\userprofil_30\3d\API.x64\PluginEntry

echo Copying folders and .py files...
xcopy /s /i /y "%SOURCE_PATH%\Controller" "%DESTINATION_PATH%\Controller"
xcopy /s /i /y "%SOURCE_PATH%\Model" "%DESTINATION_PATH%\Model"
xcopy /s /i /y "%SOURCE_PATH%\View" "%DESTINATION_PATH%\View"

xcopy /s /i /y "%SOURCE_PATH%\*.py" "%DESTINATION_PATH%\"

echo Copy complete.