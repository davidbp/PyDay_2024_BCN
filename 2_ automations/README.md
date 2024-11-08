# Understand orchestration and the basics of Kestra

## How to use it locally

We can execute it from a Docker image, we only have to run this command (or use the file I've already included: ```bash start_kestra.sh```) to download the latest image and start it locally (available on port 8080):

```bash
docker run --pull=always \
    --rm -it -p 8080:8080 --user=root \
    -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp kestra/kestra:latest server local
```


***

# References

