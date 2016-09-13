ECR Cleanup
-----------

Simple command-line tool for cleaning up untagged images from AWS ECR. Features:

 * Boto3 suppoerted authentication methods
 * Image lists longer than AWS max result count (100)

Inspired by https://github.com/jdeskins/aws-python and https://github.com/fabfuel/ecs-deploy


Installation
------------

    $ pip install https://github.com/aeirola/ecr-cleanup/archive/master.zip


Usage
-----

    $ ecr-cleanup --repository-name my-repository
