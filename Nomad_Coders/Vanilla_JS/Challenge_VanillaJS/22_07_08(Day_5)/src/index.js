import "./style.css";

const docBody = document.body;

const Small = "small";
const Medium = "medium";
const Big = "big";

function windowResize() {
  let innerWidth = window.innerWidth;
  if (innerWidth < 800) {
    docBody.classList.add(Small);
    docBody.classList.remove(Medium);
  } else if (innerWidth >= 800 && innerWidth <= 1200) {
    docBody.classList.add(Medium);
    docBody.classList.remove(Big, Small);
  } else {
    docBody.classList.add(Big);
    docBody.classList.remove(Medium);
  }
}

window.addEventListener("resize", windowResize);
