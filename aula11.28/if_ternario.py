# condição ternária acontece em formato de linha

salario =  float(input('Informe o valor do seu salário: '))

if salario >= 2500.0:
    print("IR será cobrado.")
else:
    print("IR não será cobrado.")

controle = 'IR será cobrado.' if salario >= 2500.00 else 'IR não será cobrado.' # sempre a condição verdadeira primeiro.

controle_ir = 'OK 1' if salario >= 2500.0 else 'OK 2' if True else 'Fim.'

print(controle_ir)