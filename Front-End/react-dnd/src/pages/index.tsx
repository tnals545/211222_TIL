import { DndProvider, useDrag, useDrop } from "react-dnd";
import { useRef, useState } from "react";
import { HTML5Backend } from "react-dnd-html5-backend";
import { TouchBackend } from "react-dnd-touch-backend";
import { tasks } from "@/common/tasks";
import { COLUMN_NAMES } from "@/common/contants";

export const ITEM_TYPE = "SOME_COMPONENT";

interface ItemState {
  id: number;
  name: string;
  column: string;
}

const MovableItem = ({ name, index, moveCardHandler, setItems }: any) => {
  const changeItemColumn = (currentItem: any, columnName: string) => {
    setItems((prevState: ItemState[]) =>
      prevState.map((e: ItemState) => {
        return {
          ...e,
          column: e.name === currentItem.name ? columnName : e.column,
        };
      })
    );
  };

  const ref = useRef<HTMLDivElement>(null);

  const [, drop] = useDrop({
    accept: ITEM_TYPE,
    hover(item: any, monitor: any) {
      if (!ref.current) {
        return;
      }
      const dragIndex = item.index;
      const hoverIndex = index;
      // Don't replace items with themselves
      if (dragIndex === hoverIndex) {
        return;
      }
      // Determine rectangle on screen
      const hoverBoundingRect = ref.current?.getBoundingClientRect();
      // Get vertical middle
      const hoverMiddleY =
        (hoverBoundingRect.bottom - hoverBoundingRect.top) / 2;
      // Determine mouse position
      const clientOffset = monitor.getClientOffset();
      // Get pixels to the top
      const hoverClientY = clientOffset.y - hoverBoundingRect.top;
      // Only perform the move when the mouse has crossed half of the items height
      // When dragging downwards, only move when the cursor is below 50%
      // When dragging upwards, only move when the cursor is above 50%
      // Dragging downwards
      if (dragIndex < hoverIndex && hoverClientY < hoverMiddleY) {
        return;
      }
      // Dragging upwards
      if (dragIndex > hoverIndex && hoverClientY > hoverMiddleY) {
        return;
      }
      // Time to actually perform the action
      moveCardHandler(dragIndex, hoverIndex);
      // Note: we're mutating the monitor item here!
      // Generally it's better to avoid mutations,
      // but it's good here for the sake of performance
      // to avoid expensive index searches.
      item.index = hoverIndex;
    },
  });

  const [{ isDragging }, drag] = useDrag({
    type: ITEM_TYPE,
    item: { index, name },
    end: (item, monitor) => {
      const dropResult: any = monitor.getDropResult();
      if (dropResult) {
        const { name } = dropResult;
        const { DO_IT, IN_PROGRESS, AWAITING_REVIEW, DONE } = COLUMN_NAMES;
        switch (name) {
          case DO_IT:
            changeItemColumn(item, DO_IT);
            break;
          case IN_PROGRESS:
            changeItemColumn(item, IN_PROGRESS);
            break;
          case AWAITING_REVIEW:
            changeItemColumn(item, AWAITING_REVIEW);
            break;
          case DONE:
            changeItemColumn(item, DONE);
            break;
        }
      }
    },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
  });

  const opacity = isDragging ? 0.4 : 1;

  drag(drop(ref));

  return (
    <div ref={ref} className="movable-item" style={{ opacity }}>
      {name}
    </div>
  );
};

const Column = ({ children, className, title }: any) => {
  const [, drop] = useDrop({
    accept: ITEM_TYPE,
    drop: () => ({ name: title }),
  });

  return (
    <div ref={drop} className={className}>
      {title}
      {children}
    </div>
  );
};

const App = () => {
  const [items, setItems] = useState(tasks);
  const isMobile = typeof window !== "undefined" && window.innerWidth < 600;

  const moveCardHandler = (dragIndex: number, hoverIndex: number) => {
    const dragItem = items[dragIndex];

    if (dragItem) {
      setItems((prevState) => {
        const coppiedStateArray = [...prevState];
        const prevItem = coppiedStateArray.splice(hoverIndex, 1, dragItem);
        coppiedStateArray.splice(dragIndex, 1, prevItem[0]);
        return coppiedStateArray;
      });
    }
  };

  const returnItemsForColumn = (columnName: string) => {
    return items
      .filter((item) => item.column === columnName)
      .map((item, index) => (
        <MovableItem
          key={item.id}
          name={item.name}
          setItems={setItems}
          index={index}
          moveCardHandler={moveCardHandler}
        />
      ));
  };

  const { DO_IT, IN_PROGRESS, AWAITING_REVIEW, DONE } = COLUMN_NAMES;

  return (
    <div className="container">
      <DndProvider backend={isMobile ? TouchBackend : HTML5Backend}>
        <Column title={DO_IT} className="column first-column">
          {returnItemsForColumn(DO_IT)}
        </Column>
        <Column title={IN_PROGRESS} className="column second-column">
          {returnItemsForColumn(IN_PROGRESS)}
        </Column>
        <Column title={AWAITING_REVIEW} className="column first-column">
          {returnItemsForColumn(AWAITING_REVIEW)}
        </Column>
        <Column title={DONE} className="column second-column">
          {returnItemsForColumn(DONE)}
        </Column>
      </DndProvider>
    </div>
  );
};

export default App;
