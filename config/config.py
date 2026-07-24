#this two lines connects Environments and Current Environment and then provides it's url for testing

from config.environments import ENVIRONMENTS     #Explicit importing environments dictationary into config to fetch url to test
from config.current_environment import CURRENT_ENV 

if CURRENT_ENV in ENVIRONMENTS:   
    BASE_URL = ENVIRONMENTS[CURRENT_ENV]
    REQUEST_TIMEOUT = 30 
else:
    raise ValueError(
        f"Invalid environment '{CURRENT_ENV}' selected."
        f"Supported Environments include: {', '.join(ENVIRONMENTS.keys())}"
    )