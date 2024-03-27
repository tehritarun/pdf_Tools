New-Item -Path 'Registry::HKEY_CLASSES_ROOT\Directory\Background\shell\PDF Tools'
New-ItemProperty -Path  'Registry::HKEY_CLASSES_ROOT\Directory\Background\shell\PDF Tools' -Name 'Icon' -Value 'D:\Programming\Python\pdf_Actions\assets\icon_pdf_tool.ico'

New-Item -Path 'Registry::HKEY_CLASSES_ROOT\Directory\Background\shell\PDF Tools\command'
set-ItemProperty -Path 'Registry::HKEY_CLASSES_ROOT\Directory\Background\shell\PDF Tools\command' -Name '(Default)' -Value 'powershell.exe -File "D:\Programming\Python\pdf_Actions\pdf_tools.ps1" -ExecutionPolicy Bypass -windowstyle hidden'
