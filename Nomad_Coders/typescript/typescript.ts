type Player<E> = {
  name: string;
  extraInfo: E;
};

type NicoExtra = {
  favFood: string;
};
type NicoPlayer = Player<NicoExtra>;

const nico: NicoPlayer = {
  name: "nico",
  extraInfo: {
    favFood: "kimchi",
  },
};

const lynn: Player<null> = {
  name: "lynn",
  extraInfo: null,
};

// array를 다른 방식으로 선언
type A = Array<number>; // == number[]

let a: A = [1, 2, 3, 4];

function printAllNumbers(arr: Array<number>) {}
