import "./servicecard.css";
import { start_service, stop_service, restart_service } from "../api";
import { Link } from "react-router-dom";
import { IoHelpCircleOutline } from "react-icons/io5";
import { FaPowerOff } from "react-icons/fa6";

function ServiceCard({ slug, service_name, service_logo, status }) {
  return (
    <div className="service-card" key={slug}>
      <img src={service_logo} alt={service_name} className="service-logo" />
      <div>
        <h2 className="service-name">{service_name}</h2>
        {status === "running" ? (
          <button
            className="service-button running"
            onClick={() => {
              stop_service(slug);
            }}
          >
            <FaPowerOff className="power-icon" />
          </button>
        ) : (
          <button
            className="service-button stopped"
            onClick={() => {
              start_service(slug);
            }}
          >
            <FaPowerOff className="power-icon" />
          </button>
        )}
        <Link to={"/help/" + slug} className="service-button help">
          Help
          <IoHelpCircleOutline className="help-icon" size={"1.5rem"} />
        </Link>
      </div>
    </div>
  );
}

export { ServiceCard };
