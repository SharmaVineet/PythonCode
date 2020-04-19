import boto3

client = boto3.client('s3')
bucket = 'test-credential-compromised'
prefix = 'testdata'


def list_buckets():
    response = client.list_buckets()
    return response


def list_object_versions(bucket_name, prefix_name):
    try:
        response = client.list_object_versions(
            Bucket=bucket_name,
            MaxKeys=123,
            Prefix=prefix_name
        )
        return response['Versions']
    except Exception as error:
        print("Error {}".format(error))


def delete_object(bucket_name, key_name, version_id):
    response = client.delete_object(
        Bucket=bucket_name,
        Key=key_name,
        VersionId=version_id
    )
    return response


def list_object(bucket_name):
    try:
        response = client.list_objects(
            Bucket=bucket_name,
            MaxKeys=100,
        )
        return response
    except Exception as error:
        print("Error {}".format(error))


if __name__ == '__main__':
    buckets = list_buckets()
    for bucket in buckets['Buckets']:
        print("Bucket Name is {}".format(bucket['Name']))
        # print("Listing Object {} from Bucket {}".format(list_object(bucket['Name']),bucket['Name']))
        versions = list_object_versions(bucket, prefix)
        if versions:
            for version in versions:
                if version['Key'] == prefix:
                    print("deleting the version {} for key {}".format(version['VersionId'], version['Key']))
                    delete_object(bucket, prefix, version['VersionId'])
        else:
            print("Empty Response")
