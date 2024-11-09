# Understand orchestration and the basics of Kestra

* **What is Kestra**: an orchestration platform.
* **What is orchestration**: the configuration of multiple tasks (some may be automated) into one complete end-to-end process or job.
* **Why Kestra**:
  * Lots and lots of integrations with other technologies and third-party services by [pluggings](https://kestra.io/plugins).
  * Allows versioning using your favourite control version system ([Github](https://www.youtube.com/watch?v=YbIuqYWLrpA&t=41s) for example, for managing your flows and files). Mention that even integrate with this plattforms for orchestrate processes using your CI/CDs pipelines already defined ([Github example](https://kestra.io/docs/version-control-cicd/cicd/github-action)).
  * Great [community](https://kestra.io/community).
  * Great [video tutorials](https://kestra.io/tutorial-videos/all).



## How to use it locally

We can execute it from a Docker image, we only have to run this command (or use the file I've already included: ```bash start_kestra.sh```) to download the latest image and start it locally (available on port 8080):

```bash
docker run --pull=always \
    --rm -it -p 8080:8080 --user=root \
    -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp kestra/kestra:latest server local
```

## Plan

1. Be able to run Kestra locally.
2. Understand the basic elements of a flow.
3. See a few examples.
4. Start writting the flow for solving our problem.

## What about Python?

We have basically two **types of tasks** to execute Python code:
1. To execute scripts directly written in the flow: ```io.kestra.core.tasks.scripts.Python```
2. To execute a script already loaded: ```io.kestra.core.tasks.scripts.Python```

***

# References

* [Kestra quickstart guide](https://kestra.io/docs/getting-started/quickstart).
* In case you want to try something different: [6 Best Kestra Alternatives and Competitors for 2024](https://www.shipyardapp.com/blog/kestra-alternatives/).
* To see how far can you go with this tool: [My NEW HomeLab automation platform // Kestra](https://www.youtube.com/watch?v=D4cixQ_Ek4Y&t=1895s).