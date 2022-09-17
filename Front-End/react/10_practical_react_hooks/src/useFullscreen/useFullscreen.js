import { useRef } from "react";

export const useFullscreen = (callback) => {
  const element = useRef();
  // fullscreen 상태 console에 출력하는 function
  const runCb = (isFull) => {
    if (callback && typeof callback === "function") {
      callback(isFull);
    }
  };
  // fullscreen으로 만들어주는 function
  const triggerFull = () => {
    if (element.current) {
      element.current.requestFullscreen();
      runCb(true);
    }
  };
  // fullscreen 빠져나오는 function
  const exitFull = () => {
    // fullscreen인지 check
    const checkFullscreen = document.fullscreenElement;
    if (checkFullscreen !== null) {
      document.exitFullscreen();
      runCb(false);
    }
  };
  return { element, triggerFull, exitFull };
};
