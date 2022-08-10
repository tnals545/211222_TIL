// object의 타입을 명시적으로 정해줄 수 있다.
// 하지만 아래의 Age와 Name처럼 너무 과하게 사용하는 것은 좋지 않다.
// 코드가 깔끔해지고 효율적으로 사용할 수 있는 상황에서 사용하자.
type Age = string;
type Name = number;
type Player = {
  name: Age;
  age?: Name;
};

const playerMaker = (name: string): Player => ({ name });
// name:string -> 입력되는 name의 타입 지정
// : Player -> 출력되는 타입 지정

const nico = playerMaker("nico");
nico.age = 12;
