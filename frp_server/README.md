## This should be a cloud server which hosts frp for all the client box

### For now following configuration is setup

- vm: google cloud instance (34.41.148.109)
- baseos: ubuntu
- applictions: docker
- container: frp


### config
- mkdir -p /frp-server/conf
- vim /frp-server/conf/frps.ini
[common]
bind_port = 7000
dashboard_port = 7500
dashboard_user = admin
dashboard_pwd = teamsmiley

## data dir
- mkdir -p /frp-server/data

### start frps container
docker run -d \
  --name frp-server \
  -v /frp-server/conf/frps.ini:/frp/frps.ini \
  -v /frp-server/data:/frp/data \
  -p 7000:7000 \
  -p 7500:7500 \
  snowdreamtech/frps \
  -c /frp/frps.ini
