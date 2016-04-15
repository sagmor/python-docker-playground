import docker
from service.formatter import formatter

client = docker.from_env(assert_hostname=False)

class Container(object):
    def __init__(self,id):
        self.__id = id;

    def info(self):
        return formatter(client.inspect_container(self.__id))

    def start(self):
        client.start(self.__id)

    def stop(self):
        client.stop(self.__id)

def containers():
    containers = client.containers(all=True)
    return [formatter(container) for container in containers]

