from setuptools import setup

setup(
    name='interser',
    version='0.1.0',    
    description='Learn a computer',
    url='https://github.com/shuds13/pyexample',
    author='Pavel Sutormin',
    author_email='pavel.r.sutormin@gmail.com',
    license=None,
    packages=['interser'],
    install_requires=['pillow',
                      'numpy',
                      'pandas'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Machine Learning',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)