import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='verify-quickstart',
    version='1.0.0',
    url='https://www.twilio.com/docs/verify',
    maintainer='Twilio',
    description='Tutorial for phone verification with Twilio.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
