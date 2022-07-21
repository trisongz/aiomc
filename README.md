
# aiomc

Forked from [`bmc`](https://github.com/ikodotai/bmc)


aiomc is an Async Python 3 wrapper library for MinIO's command line interface [mc](https://github.com/minio/mc) and `minio`. 
[MinIO](https://min.io), an Amazon Simple Storage Service (S3) compatible object storage. It has a useful [Python client library](https://github.com/minio/minio-py) which unfortunately lacks administrative capabilities that the `mc` and `minio` command line interfaces provide, such as adding users and hosts, which we need to do for the [iko](https://iko.ai) machine learning platform. This library solves that [problem](https://github.com/minio/minio-py/issues/829).


## Installation

```bash
pip install aiomc
```




