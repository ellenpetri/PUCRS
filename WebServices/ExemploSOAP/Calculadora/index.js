const soap = require('soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';
var args = { intA: 1, intB: 2 };

soap.createClient(url, function (err, client) {
    client.Add({ intA: 2, intB: 3 }, function (err, result) {
        if (err)
            console.log('Erro: ', err);
        else
            console.log('Resultado da soma: ', result.AddResult);
    });

    client.Subtract({ intA: 5, intB: 3 }, function (err, result) {
        if (err)
            console.log('Erro: ', err);
        else
            console.log('Resultado da subtração: ', result.SubtractResult);
    });

    client.Multiply({ intA: 5, intB: 3 }, function (err, result) {
        if (err)
            console.log('Erro: ', err);
        else
            console.log('Resultado da multiplicação: ', result.MultiplyResult);
    });

    client.Divide({ intA: 18, intB: 2 }, function (err, result) {
        if (err)
            console.log('Erro: ', err);
        else
            console.log('Resultado da divisão: ', result.DivideResult);
    });
});