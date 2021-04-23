import boto3


def update_meta(bucket_name, prefix):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    extensions = ['.webp', '.png']
    for bucket_object in bucket.objects.filter(Prefix=prefix):
        print(bucket_object.key)
        if bucket_object.key.endswith(tuple(extensions)):
            obj = bucket.Object(bucket_object.key)
            bucket_object.copy_from(CopySource={'Bucket': bucket_name, 'Key': bucket_object.key},
                                    CacheControl='max-age=31536000', ContentType=obj.content_type,
                                    MetadataDirective='REPLACE')


update_meta('BUCKET_NAME', 'PREFIX')
