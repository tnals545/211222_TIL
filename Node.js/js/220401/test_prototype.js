function Clazz(msg){
    this.name = 'I am Class';
    this.message = msg;

    message2 = 'find me!';
}

Clazz.prototype.getMessage = function(){
    return this.message;
}

Clazz.prototype.getMessage2 = function(){
    return this.message2;
}

var myClazz = new Clazz('good to see u!');
console.log(myClazz.getMessage());
console.log(myClazz.getMessage2());
