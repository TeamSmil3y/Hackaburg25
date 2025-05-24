## This should be a cloud server which hosts frp for all the client box

### For now following configuration is setup

- vm: google cloud instance (34.41.148.109)
- baseos: ubuntu
- applictions: docker
- container: frp

## FRP Server
### config
- mkdir -p /frp-server/conf
- vim /frp-server/conf/frps.ini
[common]
bind_port = 7000
dashboard_port = 7500
dashboard_user = admin
dashboard_pwd = teamsmiley
vhost_http_port = 80
vhost_https_port = 443

### data dir
- mkdir -p /frp-server/data

### start frps server container
docker run -d \
  --name frp-server \
  -v /frp-server/conf/frps.ini:/frp/frps.ini \
  -v /frp-server/data:/frp/data \
  -p 7000:7000 \
  -p 7500:7500 \
  -p 80:80 \
  -p 443:443 \
  snowdreamtech/frps \
  -c /frp/frps.ini

## FRP Client
### config
- mkdir -p /frp-client/conf
- vim /frp-client/conf/frpc.ini
[common]
server_addr = hb.teamsmiley.org
server_port = 7000

[dash]
type = http
local_ip = 127.0.0.1
local_port = 80
custom_domains = dash.smiley.hb.teamsmiley.org
use_https = true

[local-dash]
type = http
local_ip = 127.0.0.1
local_port = 3000
custom_domains = local.dash.smiley.hb.teamsmiley.org
use_https = true

[backend]
type = http
local_ip = 127.0.0.1
local_port = 8080
custom_domains = backend.smiley.hb.teamsmiley.org
use_https = true

[nextcloud]
type = http
local_ip = 127.0.0.1
local_port = 8010
custom_domains = cloud.smiley.hb.teamsmiley.org
use_https = true

[photos]
type = http
local_ip = 127.0.0.1
local_port = 8020
custom_domains = photos.smiley.hb.teamsmiley.org
use_https = true

### start frps client container
docker run -d \
  --name frp-client \
  --restart unless-stopped \
  -v /frp-client/conf/frpc.ini:/frp/frpc.ini \
  --net=host \
  snowdreamtech/frpc \
  -c /frp/frpc.ini
