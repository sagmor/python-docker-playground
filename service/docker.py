import docker

client = docker.from_env(assert_hostname=False)

INFO_KEYS = ( 'Id', 'State' )

class Container(object):
    def __init__(self,name):
        self.__name = name;

    def info(self):
        payload = client.inspect_container(self.__name)
        return { key: payload[key] for key in INFO_KEYS }

    def start(self):
        client.start(self.__name)

    def stop(self):
        client.stop(self.__name)


LIST_KEYS = ( 'Id', 'Image', 'Names', 'Status' )

def containers():
    containers = client.containers(all=True)

    return [{key: c[key] for key in LIST_KEYS } for c in containers]

