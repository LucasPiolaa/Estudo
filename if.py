salário = float(input('Informe o salário: '))

if salário <= 3000:
    print('programador junior')
elif salário > 3000 and salário <= 6000:
    print('programador pleno')
elif salário > 6000 and salário <= 15000:
    print('programador sênior')
else:
    print('gerente de projetos')
