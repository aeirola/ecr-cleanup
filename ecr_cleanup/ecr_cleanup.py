#!/usr/bin/env python

import boto3
import sys
import argparse
import pprint

def main(args):
    # Read arguments
    parser = argparse.ArgumentParser(description='Clean ECR repositories.')
    parser.add_argument('--repository-name', required=True, help='The repository whose image IDs are to be listed.')
    args = parser.parse_args(args)

    print('Cleaning up untagged images in repository: %s' % args.repository_name)

    # Fetch images to remove
    client = boto3.client('ecr')
    list_image_paginator = client.get_paginator('list_images')
    image_filter = {'tagStatus': 'UNTAGGED'}
    list_response_iterator = list_image_paginator.paginate(repositoryName=args.repository_name, filter=image_filter)

    # Iterate over responses and remove untagged images
    for list_response in list_response_iterator:
        images = list_response.get('imageIds')
        if images:
            print('Deleting untagged images: \n%s' % '\n'.join(image.get('imageDigest') for image in images))
            delete_response = client.batch_delete_image(repositoryName=args.repository_name, imageIds=images)
            if delete_response.get('failures'):
                print('Failed:')
                pprint.pprint(delete_response.get('failures'))
            else:
                print('Done')
        else:
            print('No images to delete')


if __name__ == "__main__":
    main(sys.argv)
