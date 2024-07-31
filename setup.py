from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='code-merger',
    version='1.0.0',
    author="Raffaele Spataro",
    author_email="raffaele2692@gmail.com", 
    description="A tool for merging code files into a single markdown document.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/raphael2692/code-merger",  
    packages=find_packages(),
    install_requires=[
        'tkinter'
    ],
    entry_points={
        'console_scripts': [
            'merge = merge.merge:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)