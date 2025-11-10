# Manage GCP Buckets

[https://docs.cloud.google.com/sdk/docs/install-sdk](https://docs.cloud.google.com/sdk/docs/install-sdk)

## Create bucket
```
gcloud storage buckets create gs://$BUCKET_NAME
```

## Transfer files to bucket
```
gcloud storage rsync -r ./local_dir gs://$BUCKET_NAME
```

## List buckets
```
gcloud storage ls
```
