class Dict {
  constructor() {
    this.words = {};
  }
  // word 추가
  add(word) {
    if (this.words[word.term] === undefined) {
      this.words[word.term] = [word.def];
      return `Added ${word.term}`;
    } else {
      return `The name ${word.term} already exists`;
    }
  }
  // word 제거
  del(term) {
    Object.keys(this.words).map((key) => {
      if (key === term) {
        delete this.words[term];
      }
    });
    return Object.keys(this.words);
  }
  // word 리스트로 출력
  wordList() {
    return Object.keys(this.words);
  }
  // 입력한 word에 맞는 definition(정의) 출력
  wordDef(term) {
    return this.words[term];
  }
}
class Word {
  constructor(term, def) {
    this.term = term;
    this.def = def;
  }
  // def 추가
  defAdd(def) {
    var _a;
    (_a = dict.words[this.term]) === null || _a === void 0
      ? void 0
      : _a.push(def);
    return dict.words[this.term];
  }
  // def 제거
  defRemove(delDef) {
    const value = dict.words[this.term];
    value === null || value === void 0
      ? void 0
      : value.map((val) => {
          if (delDef === val) {
            const idx = value.indexOf(val);
            delete value[idx];
          }
        });
    dict.words[this.term] =
      value === null || value === void 0
        ? void 0
        : value.filter((element) => element !== undefined);
    return dict.words[this.term];
  }
  // 기존에 있는 def 수정
  defRevise(befDef, newDef) {
    const value = dict.words[this.term];
    value === null || value === void 0
      ? void 0
      : value.map((val) => {
          if (befDef === val) {
            const idx = value.indexOf(val);
            value[idx] = newDef;
          }
        });
    return value;
  }
}
const kimchi = new Word("kimchi", "한국의 음식");
const cola = new Word("cola", "콜라");
const soda = new Word("soda", "사이다");
const dict = new Dict();
dict.add(kimchi); // 'Added kimchi'
dict.add(cola); // 'Added cola'
dict.add(soda); // 'Added soda'
kimchi.defAdd("빨간색"); // ['한국의 음식', '빨간색']
cola.defAdd("검정색"); // ['콜라', '검정색']
soda.defAdd("무색"); // ['사이다', '무색']
kimchi.defRevise("빨간색", "빨강"); // ['한국의 음식', '빨강']
cola.defRevise("검정색", "검정"); // ['콜라', '검정']
soda.defRevise("무색", "무"); // ['사이다', '무']
kimchi.defRemove("빨강"); // ['한국의 음식']
cola.defRemove("검정"); // ['콜라']
soda.defRemove("무"); // ['사이다']
dict.wordDef("kimchi"); // ['한국의 음식']
dict.wordDef("cola"); // ['콜라']
dict.wordDef("soda"); // ['사이다']
dict.wordList(); // ['kimchi', 'cola', 'soda']
dict.del("kimchi"); // ['cola', 'soda']
dict.del("cola"); // ['soda']
dict.del("soda"); // []
