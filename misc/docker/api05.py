import docker
client = docker.from_env()
container = client.containers.get('f1064a8a4c82')
print(container.logs())