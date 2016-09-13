from setuptools import setup

setup(
    name='ecr-cleanup',
    version='0.1.0',
    packages=['ecr_cleanup'],
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'ecr-cleanup = ecr_cleanup.ecr_cleanup:main'
        ]
    }
)
