import os
import subprocess
from run_setup import SetupRequirements

class RunFlask():
    def __init__(self):
        print('\n\tUpgrading pip:')
        # subprocess.call("python -m pip install --upgrade pipl", shell=True)

        
        print('\n\tSeting up requirements:')
        # SetupRequirements()
        
        print('\n\tCreating virtual environment:')
        # subprocess.call("python -m venv venv", shell=True)

        subprocess.Popen(['python -m pip install -r .\requirements.txt'],env='/venv/Scripts/activate.bat', shell=True)
        # subprocess.Popen(["venv\\Scripts\\activate.bat", 'python -m pip install -r .\requirements.txt'])
        # subprocess.Popen(["venv\\Scripts\\activate.bat", 'python -m pip install --upgrade pip; python -m pip install -r .\requirements.txt; set FLASK_APP=development; $env:FLASK_ENV="development"; set FLASK_APP=__init__.py; $env:FLASK_APP = "__init__.py"; python -m flask run'])
        print('\n\tpip installs:')
        # # os.system('cmd /k "python -m pip install --upgrade pip & python -m pip install -r .\requirements.txt"')
        # subprocess.call("python -m pip install --upgrade pip", shell=True)
        # subprocess.call("python -m pip install -r .\requirements.txt", shell=True)

        
        # print('flask config:')
        # # os.system('cmd /k "set FLASK_APP=development & $env:FLASK_ENV="development" & set FLASK_APP=__init__.py & $env:FLASK_APP = "__init__.py"')
        # subprocess.call('set FLASK_APP=development', shell=True)
        # subprocess.call('$env:FLASK_ENV="development"', shell=True)
        # subprocess.call('set FLASK_APP=__init__.py', shell=True)
        # subprocess.call('$env:FLASK_APP = "__init__.py"', shell=True)

        
        # print('run flask:')
        # # os.system('cmd /k "python -m flask run"')
        # subprocess.call('python -m flask run"', shell=True)

        
if __name__ == '__main__':
    RunFlask()