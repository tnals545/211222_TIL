const calculator = {
  add: function add(a, b) {
    return a + b;
  },
  min: function min(a, b) {
    return a - b;
  },
  div: function div(a, b) {
    return a / b;
  },
  mul: function mul(a, b) {
    return a * b;
  },
  pow: function pow(a, b) {
    return a ** b;
  },
};

const addResult = calculator.add(2, 3);
const minResult = calculator.min(addResult, 10);
const mulResult = calculator.mul(10, minResult);
const divResult = calculator.div(mulResult, addResult);
const powResult = calculator.pow(divResult, minResult);
