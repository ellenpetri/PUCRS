/*console.log('Hello world');
console.log('Fundamentos de computação e algoritimos');

{
    let f_name = 'Ellen';
    const ZIP = 50046;
    var age = 25;
}

console.log(age)

//const - valores que não podem ser alterados
//let - criar variáveis locais
//var - variáveis globais


//Comandos básicos

// [COMANDOS DE REPETIÇÃO] - For, while e do

// [COMANDOS DE SELEÇÃO] - If, else,  switch case e ternário

// [FUNÇÕES]

integrador();

function integrador (){
    for (let i = 0; i <10 ; i++){
        if (i%2 == 0)
            console.log(i+": é par")
        else
        console.log(i+": é impar")
    }
}*/

// LISTA ENCADEADA

class Node{
    constructor(element){
        this.element = element;
        this.next = null;
    }
}

class LinkedList{
    constructor(){
        this.count = 0
        this.header = null
        this.tail = null
    }

    add(element){
        if(this.count == 0)
            this.header = this.tail = element
        else
            this.tail.next = element
            this.tail = element
        this.count++
    }
    print(){
        var aux = this.header
        while(aux != null){
            console.log(aux.element)
            aux = aux.next
        }
    }
}

var myLL = new LinkedList()

myLL.add(new Node(1))
//myLL.print()

myLL.add(new Node(2))
//myLL.print()

myLL.add(new Node(4))
//myLL.print()

myLL.add(new Node(3))
myLL.print()