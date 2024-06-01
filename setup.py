from setuptools import setup, find_packages

setup(
    name='cartoonizer',
    version='0.1.0',
    description='A library for converting normal pictures to cartoon-like images',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='sachin harshitha',
    author_email='sachinharshitha971@gmail.com',
    url='https://github.com/yourusername/cartoonizer',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'numpy',
        'opencv-python',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
