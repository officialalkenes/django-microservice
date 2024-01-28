import os


ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")

if ENVIRONMENT == "dev":
    from .dev import *
elif ENVIRONMENT == "prod":
    from .prod import *
elif ENVIRONMENT == "stage":
    from .stage import *
else:
    raise ValueError("Invalid environment specified.")
