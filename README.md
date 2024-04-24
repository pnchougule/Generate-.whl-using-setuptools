Firstly, create a new virtual environment & activate newly created virtual environment(.venv/Scripts/activate).</br>
Then add project folder & add python package (create your package).</br>

ProjectName</br>
|__ __init__.py</br>
|__ ModuleName.py</br>

Now, add setup.py file & add respective metadata.</br>

ProjectName</br>
|__ __init__.py</br>
|__ ModuleName.py</br>
setup.py</br>

Run below commands:</br>
pip install setuptools wheel</br>
python setup.py bdist_wheel</br>
