import "./sidebar.css";
import { Link, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";

function Sidebar() {
  const location = useLocation();
  let active_path = location.pathname;

  const pages = {
    "/": "Services",
    "/p2p": "Peer-To-Peer Network",
    "/email": "Email",
  };
  console.log(active_path);
  return (
    <div className="sidebar">
      <h2>Hackaburg 2025</h2>
      <div className="sidebar-pages">
        {Object.entries(pages).map(([path, page]) => {
          return (
            <Link
              to={path}
              className={
                "sidebar-link " + (active_path === path ? "active" : "")
              }
            >
              {page}
            </Link>
          );
        })}
      </div>
    </div>
  );
}

export { Sidebar };
