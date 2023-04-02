#Ejercicio 3

import string

jupyter_info = """  JupyterLab is a web-based interactive development
                    environment for Jupyter notebooks,
                    code, and data. JupyterLab is flexible: configure and arrange the user
                    interface to support a wide range
                    of workflows in data science, scientific computing, and machine learning.
                    JupyterLab is extensible and
                    modular: write plugins that add new components and integrate with existing
                    ones.  """
                    
letter = input("Ingresar una letra: ").lower()   
                
if letter in string.ascii_letters:
    for word in jupyter_info.lower().split():
        if word.startswith(letter):
            print(word)
else:
    print("No se ingreso una letra.")