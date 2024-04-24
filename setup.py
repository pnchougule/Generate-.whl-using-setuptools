from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    package_data={
        '': ['data/*.xlsx', 'data/*.pdf'],
    },
    install_requires=[
        'et-xmlfile==1.1.0',
        'numpy==1.26.4',
        'openpyxl==3.1.2',
        'pandas==2.2.2',
        'PyMuPDF==1.24.2',
        'PyMuPDFb==1.24.1',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.1',
        'setuptools==69.5.1',
        'six==1.16.0',
        'tzdata==2024.1',
        'wheel==0.43.0',
    ],
)
