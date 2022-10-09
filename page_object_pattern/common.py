import yaml
from yaml.loader import SafeLoader

__config = None

def config():
    """Carga una sola vez a memoria la configuración del yaml. En caso de que ya haya sido
    cargarda, simplemente regresa el objeto desde memoria."""
    global __config

    if not __config:
        with open("config.yaml", "r") as f:
            __config = yaml.load(f, Loader=SafeLoader)

    return __config