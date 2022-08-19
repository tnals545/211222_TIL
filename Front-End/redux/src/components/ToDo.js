import { useDispatch } from "react-redux";
import React from "react";
import { deleteToDo } from "../store";

const ToDo = ({ text, id }) => {
  const dispatch = useDispatch();
  const onBtnClick = () => {
    dispatch(deleteToDo(id));
  };
  return (
    <li>
      {text} <button onClick={onBtnClick}>DEL</button>
    </li>
  );
};

export default ToDo;
