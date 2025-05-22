from .exceptions import ServiceNotFoundError
import docker

SERVICES = {
    # "email": {
    #     "name": "Email Service",
    #     "description": "Handles email notifications and communications.",
    #     "status": "running",
    #     "restartable": True,
    #     "stoppable": True,
    #     "startable": True,
    # },
    # "vpn": {
    #     "name": "VPN Service",
    #     "description": "Provides secure VPN connections.",
    #     "status": "stopped",
    #     "restartable": True,
    #     "stoppable": True,
    #     "startable": True,
    # },
    # "llm": {
    #     "name": "LLM Service",
    #     "description": "Handles large language model processing.",
    #     "status": "running",
    #     "restartable": True,
    #     "stoppable": True,
    #     "startable": True,
    # },
}

def list_services():
    return SERVICES

def check_service_name(func):
    def wrapper(service_name: str, *args, **kwargs):
        if service_name not in SERVICES:
            raise ServiceNotFoundError(f"Service '{service_name}' not found.")
        return func(service_name, *args, **kwargs)
    return wrapper

@check_service_name
def service_status(service_name: str):
    service = SERVICES[service_name]
    return service["status"]

@check_service_name
def restart_service(service_name: str):
    pass

@check_service_name
def stop_service(service_name: str):
    pass

@check_service_name
def start_service(service_name: str):
    pass

@check_service_name
def service_help(service_name: str):
    pass
