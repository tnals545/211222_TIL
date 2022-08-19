import { useDispatch } from "react-redux";
import React from "react";
import { deleteToDo } from "../store";
import { Link } from "react-router-dom";

const ToDo = ({ text, id }) => {
  const dispatch = useDispatch();
  const onBtnClick = () => {
    dispatch(deleteToDo(id));
  };
  return (
    <li>
      <Link to={`${id}`}>{text}</Link>
      <button onClick={onBtnClick}>DEL</button>
    </li>
  );
};

export default ToDo;
