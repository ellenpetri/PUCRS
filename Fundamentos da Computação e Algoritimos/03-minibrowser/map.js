//TDD - Tete Driven Development

var novoMapa = new Map();

class HistoryMap{

}

//Acesso site as 11/11/2011 as 11 da noite
novoMapa.set('11/11/2011 - 23:30 - URL', {title: 'Título do site', url: 'url sozinha'});
novoMapa.set('11/11/2011 - 23:30 - URL', {});
novoMapa.set('11/11/2011 - 23:31 - URL', {});

console.log(novoMapa.get('11/11/2011 - 23:30 - URL'));

