type Words = {
  [key: string]: string;
};

class Dict {
  private words: Words;
  constructor() {
    this.words = {};
  }
  add(word: Word) {
    if (this.words[word.term] === undefined) {
      this.words[word.term] = word.def;
    }
  }
  def(term: string) {
    return this.words[term];
  }
}

class Word {
  constructor(public term: string, public def: string) {}
}

const kimchi = new Word("kimchi", "한국의 음식");

const dict = new Dict();

dict.add(kimchi);
dict.def("kimchi");

// challenge
// 단어를 삭제하고, 단어를 업데이트하는 메소드를 만들고
// Word 클래스에서는 단어의 정의를 추가하거나 수정하는 메소드,
// 그리고 단어를 출력하는 메소드 같은걸 만들기
// 그냥 클래스랑 메소드, 그리고 private나 public 같은 것들을 사용해서 뭔가를 만들어보기
