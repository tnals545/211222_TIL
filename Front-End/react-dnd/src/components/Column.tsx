import { useDrop } from "react-dnd";

import { ITEM_TYPE } from "@/common/contants";
import { ColumnProps } from "@/common/types";

const Column = ({ children, className, title }: ColumnProps) => {
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

export default Column;
