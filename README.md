# VehiclesMarket
FullStackApp_ServerSide


# Start project:
1) run set_up.py
2) copy the lines below to powershell in this order!

python -m pip install --upgrade pip

python .\run_setup.py 
python -m venv venv
.\venv\Scripts\activate

python -m pip install --upgrade pip
python -m pip install -r .\requirements.txt

set FLASK_APP=development
$env:FLASK_ENV="development"
set FLASK_APP=__init__.py
<br />
$env:FLASK_APP = "__init__.py"

python -m flask run
