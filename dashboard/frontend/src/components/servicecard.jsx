import "./servicecard.css";
import { start_service, stop_service, restart_service } from "../api";
import { Link } from "react-router-dom";
import { IoHelpCircleOutline } from "react-icons/io5";
import { FaPowerOff, FaLink } from "react-icons/fa6";
import { RiSettings2Fill } from "react-icons/ri";
import { Popup } from "reactjs-popup";

function ServiceCard({ service, service_logo }) {
  const url =
    window.location.protocol +
    "//" +
    window.location.hostname +
    ":" +
    service.port;
  return (
    <div
      className={"service-card " + "service-" + service.status}
      key={service.name}
    >
      <img src={service_logo} alt={service.name} className="service-logo" />
      <div className="service-controls">
        <h2 className="service-name">
          {service.name}
          <span className="service-controls">
            <RiSettings2Fill size={"1.5rem"} />
          </span>
        </h2>
        {service.status === "running" ? (
          <button
            className="service-button running"
            onClick={() => {
              stop_service(service.name);
            }}
          >
            <FaPowerOff className="power-icon" />{" "}
            <span className="status-msg">{service.status}</span>
          </button>
        ) : (
          <button
            className="service-button stopped"
            onClick={() => {
              start_service(service.name);
            }}
          >
            <FaPowerOff className="power-icon" />{" "}
            <span className="status-msg">{service.status}</span>
          </button>
        )}
        <a href={url} className="service-link">
          <FaLink size={"1.5rem"} />
        </a>
        <br style={{ marginBottom: "2rem" }} />
        <Link to={"/help/" + service.name} className="service-button help">
          Help
          <IoHelpCircleOutline className="help-icon" size={"1.5rem"} />
        </Link>
      </div>
    </div>
  );
}

export { ServiceCard };
