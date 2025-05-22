const API_BASE = "http://localhost:8080";

class Service {}

async function request(path) {
  return (await fetch(API_BASE + path)).text();
}

async function list_services() {
  return JSON.parse(await request("/services/list"));
}

async function get_service_status(service_name) {
  return JSON.parse(await request(`/services/${service_name}/status`));
}

async function start_service(service_name) {
  return JSON.parse(await request(`/services/${service_name}/start`));
}

async function stop_service(service_name) {
  return JSON.parse(await request(`/services/${service_name}/stop`));
}

async function restart_service(service_name) {
  return JSON.parse(await request(`/services/${service_name}/restart`));
}

async function get_service_help(service_name) {
  return JSON.parse(await request(`/services/${service_name}/help`));
}

export {
  list_services,
  get_service_status,
  start_service,
  stop_service,
  restart_service,
  get_service_help,
};
