# service-toy

start the service: `$ baseplate-serve --debug example.ini`

make some requests:

```
python3 -m reddit_service_toy.toy_thrift.remote -h localhost:9090 is_healthy
python3 -m reddit_service_toy.toy_thrift.remote -h localhost:9090 get_random
python3 -m reddit_service_toy.toy_thrift.remote -h localhost:9090 multiply 6 23
```
