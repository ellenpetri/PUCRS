const soap = require('soap');

var url = 'http://localhost:8001/wscalc1?wsdl';

soap.createClient(url, function(err, client) {
    if (err) {
        console.error(err);
        return;
    }
    client.multiplicar({ a: 5, b: 3 }, function(err, result) {
        if (err) {
            console.error(err);
            return;
        }
        console.log('Resultado da multiplicação: ', result.mulres);
    });
    client.somar({ a: 5, b: 3 }, function(err, result) {
        if (err) {
            console.error(err);
            return;
        }
        console.log('Resultado da soma: ', result.sumres);
    });
});