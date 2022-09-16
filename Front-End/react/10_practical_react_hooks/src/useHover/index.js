import React, { useEffect, useRef, useState } from "react";
import { createRoot } from "react-dom/client";

import { useHover } from "./useHover";

const App = () => {
  const sayHello = () => console.log("say hello");
  const title = useHover(sayHello);
  return (
    <div className="App">
      <h1 ref={title}>Hi</h1>
    </div>
  );
};

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(<App />);
