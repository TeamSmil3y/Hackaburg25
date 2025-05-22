| Method | Endpoint                           | Description                                  |
| ------ | ---------------------------------- | -------------------------------------------- |
| GET    | `/services/list`                   | List all available services.                 |
| GET    | `/services/{service_name}/status`  | Get the status of a specific service.        |
| GET    | `/services/{service_name}/help`    | Get help information for a specific service. |
| GET    | `/services/{service_name}/restart` | Restart a specific service.                  |
| GET    | `/services/{service_name}/stop`    | Stop a specific service.                     |
| GET    | `/services/{service_name}/start`   | Start a specific service.                    |


## Examples
- curl http://localhost:8080/services/list
- curl http://localhost:8080/services/nextcloud/status
- curl http://localhost:8080/services/nextcloud/restart
- curl http://localhost:8080/services/nextcloud/start
- curl http://localhost:8080/services/nextcloud/help
- 

- curl http://localhost:8080/services/immich/status
- curl http://localhost:8080/services/immich/stop

## Raw docker commands
- docker run -d --memory 1024m --name nextcloud \
  -v /home/jasforum/Developer/hackathons/Hackaburg25/dashboard/backend/data/nextcloud:/var/www/html/data \
  -p 8010:80 \
  nextcloud
- docker run -d --memory 2048m --name immich_server \
  -v /home/jasforum/Developer/hackathons/Hackaburg25/dashboard/backend/data/immich:/app/data \
  -p 8020:2283 \
  altran1502/immich-server:v1.89.0/immich-server:latest
