import React, { useEffect, useRef, useState } from "react";
import { createRoot } from "react-dom/client";

import { useBeforeLeave } from "./useBeforeLeave";

const App = () => {
  const begForLife = () => console.log("pls don't leave");
  useBeforeLeave(begForLife);
  return (
    <div className="App">
      <h1>Hello</h1>
    </div>
  );
};

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(<App />);
