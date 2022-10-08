import yaml

__config = None

def config():
    global __config
        
    if not config:
        with open("config.yaml") as f:
            __config = yaml.load(f)
    else: 
        pass

    return __config