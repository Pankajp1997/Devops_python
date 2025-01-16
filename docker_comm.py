import docker

def list_containers():
    client = docker.from_env()
    containers = client.containers.list()
    for container in containers:
        print(container.name)

list_containers()
