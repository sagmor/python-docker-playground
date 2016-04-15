import docker

client = docker.from_env(assert_hostname=False)

INFO_KEYS = ( 'Id', 'State' )

class Container(object):
    def __init__(self,id):
        self.__id = id;

    def info(self):
        payload = client.inspect_container(self.__id)
        return { key: payload[key] for key in INFO_KEYS }

    def start(self):
        client.start(self.__id)

    def stop(self):
        client.stop(self.__id)


LIST_KEYS = ( 'Id', 'Image', 'Status' )

def containers():
    containers = client.containers(all=True)

    return [{key: c[key] for key in LIST_KEYS } for c in containers]

