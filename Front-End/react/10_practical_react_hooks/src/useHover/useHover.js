import React, { useEffect, useRef } from "react";

// React 16.8v
export const useHover = (onHover) => {
  const element = useRef();
  useEffect(() => {
    if (typeof onHover !== "function") {
      return;
    }
    // component 가 mount 될 때 eventListener 추가, dependency 가 없기 때문에 한 번만 실행됨
    // => componentDidMount, componentDidUpdate
    if (element.current) {
      element.current.addEventListener("mouseenter", onHover);
    }
    // component 가 mount 되지 않았을 때는 eventListener 가 배치되지 않게 함
    // => componentWillUnMount
    return () => {
      if (element.current) {
        element.current.removeEventListener("mouseenter", onHover);
      }
    };
  }, []); // [] => dependency
  return typeof onHover !== "function" ? undefined : element;
};
