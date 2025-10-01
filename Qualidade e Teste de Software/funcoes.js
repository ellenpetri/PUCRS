const funcoes = {
    somarDoisValores: (v1, v2) => v1 + v2,
    subtrairDoisValores: (v1, v2) => v1 - v2,
    multiplicarDoisValores: (v1, v2) => v1 * v2,
    dividirDoisValores: (v1, v2) => v1 / v2,
    sempreNull : () => null,
    sempreTrue : () => true,
    sempreFalse : () => false,

    codigoValido: (codigo) => {
        if (codigo === null || codigo === undefined) 
            return false;
        if(codigo >=1000 && codigo <= 9999) 
            return true;
        return false;
    }
}

module.exports = funcoes;