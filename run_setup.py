import os
from pip_config import LIBS

# CREATES AN INSTALLATION FILE
class SetupRequirements():
    def __init__(self):
        with open('requirements.txt', 'w', encoding="utf-8") as f:
            f.writelines(LIBS)
            
# if __name__ == '__main__':
#     SetupRequirements()