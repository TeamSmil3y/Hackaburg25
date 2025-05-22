import "./servicecard.css";
import { Link } from "react-router-dom";
import { IoHelpCircleOutline } from "react-icons/io5";

function ServiceCard({ service_name, service_logo, status, key }) {
  return (
    <div className="service-card" key={key}>
      <img src={service_logo} alt={service_name} className="service-logo" />
      <h2 className="service-name">{service_name}</h2>
      <button className="service-button">start</button>
      <button className="service-button">stop</button>
      <button className="service-button">restart</button>
      <button className="service-button">{status}</button>
      <Link to={"/help/" + service_name} className="service-button">
        <IoHelpCircleOutline className="help-icon" />
      </Link>
    </div>
  );
}

export { ServiceCard };
