import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Variaveis
# Idade do imovel, área, distancia do centro e valor condominio

IDADE_IMOVEL_INPUT = 0
AREA_INPUT = 0
DISTANCIA_CENTRO_INPUT = 0
VALOR_CONDOMINIO = 0

# Definindo as variaveis de entrada e saida do sistema fuzzy
idade_do_imovel = ctrl.Antecedent(np.arange(0, 200, 1), 'idade_do_imovel')
area = ctrl.Antecedent(np.arange(12, 200, 1), 'area')
distancia_centro = ctrl.Antecedent(np.arange(0, 20, 1), 'distancia_centro')
valor_condominio = ctrl.Antecedent(np.arange(100, 600, 100), 'valor_condominio')
valor = ctrl.Consequent(np.arange(25000, 1000000, 2500), 'valor')

# Popula as variaveis com as funções de membership
idade_do_imovel.automf(3, 'idade_do_imovel', ['low', 'mid', 'high'])
area.automf(3, 'area', ['low', 'mid', 'high'])
distancia_centro.automf(3, 'distancia_centro', ['low', 'mid', 'high'])
valor_condominio.automf(3, 'valor_condominio', ['low', 'mid', 'high'])
valor.automf(3, 'valor', ['low', 'mid', 'high'])

# Definindo as variaveis de entrada do usuario
while True:
    IDADE_IMOVEL_INPUT = int(
        input('Digite um valor entre 0 e 200 para a idade do imovel: '))
    if IDADE_IMOVEL_INPUT < 0 or IDADE_IMOVEL_INPUT > 200:
        print('\nErro: você digitou um valor muito alto ou muito baixo!\n')
    else:
        break

while True:
    AREA_INPUT = int(
        input('Digite um valor entre 12 e 200 para a area do imovel: '))
    if AREA_INPUT < 12 or AREA_INPUT > 200:
        print('\nErro: você digitou um valor muito alto ou muito baixo!\n')
    else:
        break

while True:
    DISTANCIA_CENTRO_INPUT = int(
        input('Digite um valor entre 2 e 20 para a distancia do centro: '))
    if DISTANCIA_CENTRO_INPUT < 2 or DISTANCIA_CENTRO_INPUT > 20:
        print('\nErro: você digitou um valor muito alto ou muito baixo!\n')
    else:
        break

while True:
    VALOR_CONDOMINIO = int(
        input('Digite um valor entre 100 e 600 para o valor do condominio: '))
    if VALOR_CONDOMINIO < 100 or VALOR_CONDOMINIO > 600:
        print('\nErro: você digitou um valor muito alto ou muito baixo!\n')
    else:
        break
    
# Regras
rules = []
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['high'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['high'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['high'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['mid'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['mid'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['mid'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['high'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['high'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['high'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['mid'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['mid'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['mid'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['high'] & area['low'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['mid'] & area['low'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['low'] & valor_condominio['high'], valor['low']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['low'] & valor_condominio['mid'], valor['mid']))
rules.append(ctrl.Rule(idade_do_imovel['low'] & area['low'] & distancia_centro['low'] & valor_condominio['low'], valor['high']))




valorCtrl = ctrl.ControlSystem(rules)
valorTotal = ctrl.ControlSystemSimulation(valorCtrl)

valorTotal.input['idade_do_imovel'] = IDADE_IMOVEL_INPUT
valorTotal.input['area'] = AREA_INPUT
valorTotal.input['distancia_centro'] = DISTANCIA_CENTRO_INPUT
valorTotal.input['valor_condominio'] = VALOR_CONDOMINIO

valorTotal.compute()

def PrintValor(val):
    print('\n Valor do imovel: R$ {:.2f}'.format(val))

PrintValor(valorTotal.output['valor'])
valor.view(sim=valorTotal)
plt.show()
