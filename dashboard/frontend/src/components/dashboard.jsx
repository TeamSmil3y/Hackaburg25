import "./dashboard.css";
import { ServiceCard } from "./servicecard";
import {
  list_services,
  get_service_status,
  start_service,
  stop_service,
  restart_service,
  get_service_help,
} from "../api";
import { useEffect, useState } from "react";

function Dashboard() {
  const [services, setServices] = useState(null);

  useEffect(() => {
    async function fetchServices() {
      setServices(await list_services());
    }
    fetchServices();
  }, []);

  return (
    <div className="dashboard">
      <div className="dashboard-services">
        {services === null ? (
          <div className="loading"></div>
        ) : (
          Object.entries(services).map(([slug, service]) => {
            const service_name = service["name"];
            const service_logo = service["logo_url"];
            const service_status = service["status"];
            return (
              <ServiceCard
                service_name={service_name}
                service_logo={service_logo}
                service_status={service_status}
                key={slug}
              />
            );
          })
        )}
      </div>
    </div>
  );
}

export { Dashboard };
