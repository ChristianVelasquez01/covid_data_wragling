from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'covid_data_wragling=main.__main__:main',
        ],
    },
)