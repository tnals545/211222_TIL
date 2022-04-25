function Clazz(msg){
    this.name = 'I am Class';
    this.message = msg;

    message2 = 'find me!';
    this.print = function(){
        console.log(message2);
    };
}

var myClazz = new Clazz('good to see u!');
console.log(myClazz.message);
console.log(myClazz.message2);
myClazz.print();