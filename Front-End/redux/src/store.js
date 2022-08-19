import { legacy_createStore } from "redux";
import { createAction, createReducer } from "@reduxjs/toolkit";

export const addToDo = createAction("ADD");
export const deleteToDo = createAction("DELETE");

/*
const reducer = (state = [], action) => {
  switch (action.type) {
    case addToDo.type:
      console.log(action);
      return [{ text: action.payload, id: Date.now() }, ...state];
    case deleteToDo.type:
      return state.filter((toDo) => toDo.id !== action.payload);
    default:
      return state;
  }
};
*/

const reducer = createReducer([], {
  [addToDo]: (state, action) => {
    state.push({ text: action.payload, id: Date.now() });
  },
  [deleteToDo]: (state, action) =>
    state.filter((toDo) => toDo.id !== action.payload),
});

const store = legacy_createStore(reducer);

export default store;
