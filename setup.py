from setuptools import setup, find_packages

setup(
    name='pyproxy',
    version='0.0.1',
    description='A python proxy protocol library',
    url='https://github.com/efossier/py-proxy-protocol',
    author='Evan Fossier',
    author_email='evan.fossier@gmail.com',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='proxy protocol haproxy proxy_protocol',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
)

