from setuptools import setup, find_packages

setup(
    name='beets-redmissing',
    version='0.1',
    description='A beets plugin to compare local library with Redacted',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/beets-redmissing',
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
)
