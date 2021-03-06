from setuptools import setup

setup(
    name='pyticketswitch',
    version='1.6.4',
    author='Ingresso',
    author_email='systems@ingresso.co.uk',
    packages=[
        'pyticketswitch',
        'pyticketswitch.interface_objects'
    ],
    license='MIT',
    description='A Python interface for the Ingresso XML Core API',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
)
