type PlayerA = {
  firstName: string;
};

interface PlayerB {
  firstName: string;
}

class User implements PlayerA {
  constructor(public firstName: string) {}
}
