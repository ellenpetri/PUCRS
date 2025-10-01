const soap = require('soap');
const url = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl';

soap.createClient(url, function (err, client) {
    if (err) {
        console.error('Error creating SOAP client:', err);
        return;
    } else {
        client.consultaCEP({ cep: '91520260' }, function (err, result) {
            if (err) {
                console.error('Error calling consultaCEP:', err);
                return;
            } else {
                console.log('Address information:', result);
            }
        });
    }
});