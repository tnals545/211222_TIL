import { configureStore, createSlice } from "@reduxjs/toolkit";

const toDos = createSlice({
  name: "toDosReducer",
  initialState: [],
  reducers: {
    add: (state, action) => {
      state.push({ text: action.payload, id: Date.now() });
      console.log(action.payload);
    },
    remove: (state, action) =>
      state.filter((toDo) => toDo.id !== action.payload),
  },
});

console.log(toDos.actions.payload);

export const { add, remove } = toDos.actions;

export default configureStore({ reducer: toDos.reducer });
