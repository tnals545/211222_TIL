const colors = [
  "#ef5777",
  "#575fcf",
  "#4bcffa",
  "#34e7e4",
  "#0be881",
  "#f53b57",
  "#3c40c6",
  "#0fbcf9",
  "#00d8d6",
  "#05c46b",
  "#ffc048",
  "#ffdd59",
  "#ff5e57",
  "#d2dae2",
  "#485460",
  "#ffa801",
  "#ffd32a",
  "#ff3f34",
];
const btn = document.querySelector("button");

function btnClick() {
  // 랜덤하게 고른 2개의 색이 겹치지 않게 코딩
  const colorIndexArray = [];
  for (let i = 0; i < 2; i++) {
    let colorIndex = Math.floor(Math.random() * colors.length);
    if (!colorIndexArray.includes(colorIndex)) {
      colorIndexArray.push(colorIndex);
    } else {
      i--;
    }
  }
  // body의 style에 선택된 색상 적용
  const color1 = colors[colorIndexArray[0]];
  const color2 = colors[colorIndexArray[1]];
  document.body.style = `background: linear-gradient(0.25turn, ${color1}, ${color2});`;
}

btn.addEventListener("click", btnClick);
