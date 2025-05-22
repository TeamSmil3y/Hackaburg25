import logo from "./logo.svg";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Dashboard } from "./components/dashboard";
import { Help } from "./components/help";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/help/:service_name" element={<Help />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
