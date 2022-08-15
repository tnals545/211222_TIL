const clockTitle = document.querySelector(".js-clock");

function dDay() {
  const target = new Date("2022-12-25");
  const now = new Date();
  const timeRemaining = target - now;
  const targetDay = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
  const targetHour = String(
    Math.floor((timeRemaining / (1000 * 60 * 60)) % 24)
  ).padStart(2, "0");
  const targetMin = String(
    Math.floor((timeRemaining / (1000 * 60)) % 60)
  ).padStart(2, "0");
  const targetSec = String(Math.floor((timeRemaining / 1000) % 60)).padStart(
    2,
    "0"
  );

  clockTitle.innerText = `${targetDay}d ${targetHour}h ${targetMin}m ${targetSec}s`;
}

dDay();
setInterval(dDay, 1000);
