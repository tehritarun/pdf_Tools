$CurrentPath=$PWD.Path
Copy-Item .\*.pdf D:\Programming\Python\pdf_Actions\
Set-Location D:\Programming\Python\pdf_Actions
pipenv run python .\merge_pdf.py
Copy-Item .\merged_pdf.pdf $CurrentPath
Remove-Item .\*.pdf
Set-Location $CurrentPath
