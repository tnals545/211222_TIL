import React, { useEffect, useRef, useState } from "react";
import { createRoot } from "react-dom/client";

import { useNotification } from "./useNotification";

const App = () => {
  const tirggerNotif = useNotification("Can I steal your kimchi?", {
    body: "I love kimchi dont you?",
  });
  return (
    <div className="App" style={{ height: "1000vh" }}>
      <button onClick={tirggerNotif}>Hello</button>
    </div>
  );
};

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(<App />);
