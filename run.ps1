# Smart Key Launcher - v2.0
# Automatski postavlja Tcl/Tk environment i pokreće aplikaciju

# Aktiviraj virtual environment
& ".\venv\Scripts\Activate.ps1"

# Postavi Tcl/Tk environment varijable
$env:TCL_LIBRARY = "$PWD\venv\tcl\tcl8.6"
$env:TK_LIBRARY = "$PWD\venv\tcl\tk8.6"

# Pokreni aplikaciju
Write-Host "`n🚀 Pokrećem Smart Key - PyZ3R Security v2.0...`n" -ForegroundColor Green

python main.py

# Deaktiviraj virtual environment nakon zatvaranja
deactivate
