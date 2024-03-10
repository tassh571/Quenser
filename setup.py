from setuptools import setup, find_packages

setup(
    name="Quenser",
    version="0.0.2",
    author="Tassana Khrueawan",
    author_email="tassana.khr@gmail.com",
    description="A custom library for Robot Framework that allows you to say hello",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tassh571/Quenser.git",
    packages=find_packages(),
    install_requires=[
        'robotframework>=3.0', 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
