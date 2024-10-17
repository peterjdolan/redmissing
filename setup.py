from setuptools import setup, find_packages

setup(
    name='redmissing',
    version='0.1',
    description='A simple utility to identify missing items on Redacted',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Peter Dolan',
    author_email='peter@petedolan.com',
    url='https://github.com/peterjdolan/redmissing',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'tqdm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'redmissing=redmissing:main',
        ],
    },
)
