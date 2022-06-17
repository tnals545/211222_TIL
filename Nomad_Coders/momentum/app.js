const calculator = {
  add: function add(a, b) {
    console.log(a + b);
  },
  min: function min(a, b) {
    console.log(a - b);
  },
  div: function div(a, b) {
    console.log(a / b);
  },
  mul: function mul(a, b) {
    console.log(a * b);
  },
  pow: function pow(a, b) {
    console.log(a ** b);
  },
};

calculator.add(1, 2);
calculator.min(1, 2);
calculator.div(1, 2);
calculator.mul(1, 2);
calculator.pow(1, 2);
