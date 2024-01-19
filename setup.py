from setuptools import setup, find_packages

setup(
    name='realmeye',
    version='0.1.0',
    packages=find_packages(),
    author="thedrdu",
    author_email="thedrdu@gmail.com",
    description="An API wrapper for RealmEye.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords="realmeye rotmg".split(),
    url="https://github.com/thedrdu/realmeye.py",
    python_requires=">=3.8",
    install_requires=[
        'aiohttp',
        'beautifulsoup4',
        'pydantic',
        'pydantic-settings'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    license='MIT'
)
