from .exceptions import ServiceNotFoundError
import subprocess

SERVICES = {
    "nextcloud": {
        "container_name": "nextcloud",
        "image": "nextcloud",
        "description": "Self-hosted cloud storage and collaboration platform.",
        "memory_limit": "1024m",  # 1GB
        "volumes": ["/opt/nextcloud/data:/var/www/html/data"],
        # "volumes": ["/home/jasforum/Developer/hackathons/Hackaburg25/dashboard/backend/data/nextcloud:/var/www/html/data"],
        "ports": ["8010:80"],
        "help": {
            "description": "Nextcloud is a self-hosted productivity platform that keeps you in control.",
            "link": {
                "apple": "https://apps.apple.com/us/app/nextcloud/id1125420102",
                "google": "https://play.google.com/store/apps/details?id=com.nextcloud.client&pcampaignid=web_share",
            },
            "instructions": [
                "Download the Nextcloud app from the App Store or Google Play.",
                "Open the app and enter your server URL (e.g., http://your-server-ip:8010).",
                "Log in with your Nextcloud credentials.",
                "Start using Nextcloud to store and share files securely."
            ]
        },
        "config": {
            "port": {
                "type": "port",
                "from": 1024,
                "to": 65535,
                "value": 8010,
            },
            "memory limit (MiB)": {
                "type": "slider",
                "from": 512,
                "to": 4096,
                "value": 1024
            },
        }
    },
    "immich": {
        "container_name": "immich_server",
        "image": "altran1502/immich-server:v1.89.0",
        "description": "Self-hosted Google Photos alternative with AI features.",
        "memory_limit": "2048m",  # 2GB
        "volumes": ["/opt/immich/data:/app/data"],
        # "volumes": ["/home/jasforum/Developer/hackathons/Hackaburg25/dashboard/backend/data/immich:/app/data"],
        "ports": ["8020:2283"],
        "help": {
            "description": "Immich is a self-hosted photo and video backup solution with AI features.",
            "link": {
                "apple": "https://apps.apple.com/us/app/immich/id1613945652",
                "google": "https://play.google.com/store/apps/details?id=app.alextran.immich&pcampaignid=web_share",
            },
            "instructions": [
                "Download the Immich app from the App Store or Google Play.",
                "Open the app and enter your server URL (e.g., http://your-server-ip:8020).",
                "Log in with your Immich credentials.",
                "Start backing up your photos and videos securely."
            ]
        },
        "config": {
            "port": {
                "type": "port",
                "from": 1024,
                "to": 65535,
                "value": 8020,
            },
            "memory limit (MiB)": {
                "type": "slider",
                "from": 512,
                "to": 4096,
                "value": 2048
            },
        }
    },
}

def list_services():
    results = {}
    for key, meta in SERVICES.items():
        container = meta["container_name"]
        try:
            output = subprocess.check_output(["docker", "inspect", "-f", "{{.State.Status}}", container], stderr=subprocess.DEVNULL)
            status = output.decode().strip()
        except subprocess.CalledProcessError:
            status = "not found"
        results[key] = {"status": status, "description": meta["description"], "port": meta["ports"][0].split(":")[0], "help": meta["help"]}
    return results

def check_service_name(func):
    def wrapper(service_name: str, *args, **kwargs):
        if service_name not in SERVICES:
            raise ServiceNotFoundError(f"Service '{service_name}' not found.")
        return func(service_name, *args, **kwargs)
    return wrapper

@check_service_name
def service_status(service_name: str):
    container = SERVICES[service_name]["container_name"]
    try:
        output = subprocess.check_output(["docker", "inspect", "-f", "{{.State.Status}}", container], stderr=subprocess.DEVNULL)
        return {"status": output.decode().strip()}
    except subprocess.CalledProcessError:
        return {"status": "not found"}

@check_service_name
def restart_service(service_name: str):
    container = SERVICES[service_name]["container_name"]
    subprocess.run(["docker", "restart", container], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return {"status": "restarted"}

@check_service_name
def stop_service(service_name: str):
    container = SERVICES[service_name]["container_name"]
    subprocess.run(["docker", "stop", container], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return {"status": "stopped"}

@check_service_name
def start_service(service_name: str):
    container = SERVICES[service_name]["container_name"]
    image = SERVICES[service_name]["image"]
    memory_limit = SERVICES[service_name].get("memory_limit")
    volumes = SERVICES[service_name].get("volumes", [])
    ports = SERVICES[service_name].get("ports", [])

    try:
        subprocess.run(["docker", "start", container], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        cmd = [
            "docker", "run", "-d",
            "--memory", memory_limit,
            "--name", container,
        ]
        for v in volumes:
            cmd += ["-v", v]
        for p in ports:
            cmd += ["-p", p]
        cmd.append(image)
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return {"status": "started"}

@check_service_name
def service_help(service_name: str):
    return {"help": SERVICES[service_name]["help"]}
