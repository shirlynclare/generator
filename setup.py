from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Sunny Savita',
    author_email='sunny.savita@ineuron.ai',
    description='A package for generating multiple-choice questions',
    install_requires=[
        "openai>=0.12.0",
        "langchain>=0.2.0",
        "streamlit>=1.7.0",
        "python-dotenv>=0.18.0",
        "PyPDF2>=1.26.0"
    ],
    packages=find_packages(),
    license='MIT',
    url='https://github.com/shirlynclare/mcqgenerator',
)
