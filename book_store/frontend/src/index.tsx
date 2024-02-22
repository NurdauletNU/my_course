import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import "./css/bootstrap/bootstrap.css";
import "./css/fontawesome/css/all.css";
import Router from "./components/router";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  // <React.StrictMode>
  <Router />,
  // </React.StrictMode>
);
