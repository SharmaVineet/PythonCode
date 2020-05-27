import random

import boto3

prefix = 'fcn-cfn-apollo-'
client = boto3.client('s3')
s3 = boto3.resource('s3')


def s3_create_bucket():
    random_number = random.randint(100, 999)
    bucket_name = prefix + str(random_number)
    bucket = s3.Bucket(bucket_name)

    response = bucket.create(
        ACL='private'
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Successfully Created bucket {}".format(bucket_name))


def s3_delete_bucket(bucket_name):
    bucket = s3.Bucket(bucket_name)
    # object_versions_iterator = bucket.object_versions.all()
    # print(object_versions_iterator)
    bucket.object_versions.delete()
    bucket.delete()
    print("Successfully Deleted bucket {}".format(buckets))


def s3_list_buckets():
    response = client.list_buckets()
    all_buckets = []
    for bucket in response['Buckets']:
        if prefix in bucket['Name']:
            all_buckets.append(bucket['Name'])
    return all_buckets


def s3_put_objects(bucket_name):
    random_number = random.randint(100, 999)
    response = client.put_object(
        ACL='private',
        Bucket=bucket_name,
        Key="random_bucket_inside_bucket_" + str(random_number)
    )
    return response


if __name__ == '__main__':
    user_input = input("Would you like to create/delete bucket\nSelect 1 for create bucket \nSelect 2 for delete "
                       "bucket\nSelect 3 for put object\n")

    if user_input == '1':
        for _ in range(1):
            s3_create_bucket()
    elif user_input == '2':
        s3_bucket_name = s3_list_buckets()
        for buckets in s3_bucket_name:
            s3_delete_bucket(buckets)
    elif user_input == '3':
        print(s3_put_objects('fcn-cfn-apollo-495'))
