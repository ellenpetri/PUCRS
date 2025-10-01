const funcoes = require('./funcoes');

test('somarDoisValores 1 + 2 = 3', () => {
    expect(funcoes.somarDoisValores(1, 2)).toBe(3);
});

test('subtrairDoisValores 5 - 3 = 2', () => {
    expect(funcoes.subtrairDoisValores(5, 3)).toBe(2);
});

test('multiplicarDoisValores 4 * 3 = 12', () => {
    expect(funcoes.multiplicarDoisValores(4, 3)).toBe(12);
});
test('dividirDoisValores 10 / 2 = 5', () => {
    expect(funcoes.dividirDoisValores(10, 2)).toBe(5);
});
test('dividirDoisValores 10 / 0 = Infinity', () => {
    expect(funcoes.dividirDoisValores(10, 0)).toBe(Infinity);
});
test('dividirDoisValores 0 / 10 = 0', () => {
    expect(funcoes.dividirDoisValores(0, 10)).toBe(0);
});
test('dividirDoisValores 0 / 0 = NaN', () => {
    expect(funcoes.dividirDoisValores(0, 0)).toBe(NaN);
});
test('somarDoisValores -1 + -1 = -2', () => {
    expect(funcoes.somarDoisValores(-1, -1)).toBe(-2);
});
test('subtrairDoisValores -5 - -3 = -2', () => {
    expect(funcoes.subtrairDoisValores(-5, -3)).toBe(-2);
});
test('multiplicarDoisValores -4 * 3 = -12', () => {
    expect(funcoes.multiplicarDoisValores(-4, 3)).toBe(-12);
});
test('multiplicarDoisValores -4 * -3 = 12', () => {
    expect(funcoes.multiplicarDoisValores(-4, -3)).toBe(12);
});
test('somarDoisValores 1.5 + 2.5 = 4', () => {
    expect(funcoes.somarDoisValores(1.5, 2.5)).toBe(4);
});
test('subtrairDoisValores 5.5 - 3.5 = 2', () => {
    expect(funcoes.subtrairDoisValores(5.5, 3.5)).toBe(2);
});
test('multiplicarDoisValores 4.5 * 2 = 9', () => {
    expect(funcoes.multiplicarDoisValores(4.5, 2)).toBe(9);
});
test('dividirDoisValores 10.5 / 2 = 5.25', () => {
    expect(funcoes.dividirDoisValores(10.5, 2)).toBe(5.25);
});

test('sempreNull deve retornar null', () => {
    expect(funcoes.sempreNull()).toBeNull();
});

test('sempreTrue deve retornar true', () => {
    expect(funcoes.sempreTrue()).toBeTruthy();
}); 

test('sempreFalse deve retornar false', () => {
    expect(funcoes.sempreFalse()).toBeFalsy();
});

test('codigoValido deve retornar true para codigo 1000', () => {
    expect(funcoes.codigoValido(1000)).toBeTruthy();
});

test('codigoValido deve retornar true para codigo 5000', () => {
    expect(funcoes.codigoValido(5000)).toBeTruthy();
});

test('codigoValido deve retornar true para codigo 9999', () => {
    expect(funcoes.codigoValido(9999)).toBeTruthy();
});

test('codigoValido deve retornar false para codigo 999', () => {
    expect(funcoes.codigoValido(999)).toBeFalsy();
});