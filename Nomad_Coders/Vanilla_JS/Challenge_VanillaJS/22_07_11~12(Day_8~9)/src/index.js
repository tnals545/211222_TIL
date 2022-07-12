const numberForm = document.getElementById("number-form");
const rangeInput = document.querySelector("#number-range input");
const guessInput = document.querySelector("#number-guess input");
const numberButton = document.querySelector("#number-guess button");
const greeting = document.querySelector("#greeting");
const winOrlost = document.querySelector("#win-lost");

function btnClick() {
  const range = rangeInput.value;
  let machineChose = Math.round(Math.random() * range);
  const guess = guessInput.value;
  greeting.innerText = `You chose: ${guess}, the machine chose: ${machineChose}.`;
  if (guess === machineChose) {
    winOrlost.innerText = "You won!";
  } else {
    winOrlost.innerText = "You lost!";
  }
}

function btnSubmit(event) {
  event.preventDefault();
}

numberForm.addEventListener("submit", btnSubmit);
numberButton.addEventListener("click", btnClick);
