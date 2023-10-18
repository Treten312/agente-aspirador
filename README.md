# Agente Aspirador
Atividade Avaliativa I - Inteligência Artificial <br>
- Alunos: <br>
  - André Lima
  - Carlos Mateus

## Objetivo 
Implementação de um Agente Racional que limpa um quarto com o mínimo possível de ações, o objetivo é que todo o ambiente esteja limpo e o agente retorne ao lar.

## Parte A - Indentificação do PEAS (Performance, EnviroNment, Actuators and Sensors).

| Agente | Performance | Ambiente | Atuadores | Sensores |
| --- | --- | --- | --- | --- |
| Aspirador | Quantidade de sujeira limpa, Eficiencia de energia | Grade de quadrados 4x4 | Motores de movimento, Mecânismo de aspiração, Mecânismo de esvaziamente de bolsa | Sensor de sujeira, Sensor de energia, Sensor de proximidade |

## Parte B - Criação de código em Java ou Python para implementar o Agente Racional.
Checklist de implementações necessárias:
- [ ] Implementação do ambiente estático, definir um array ou alguma outra estrutura de dados que representará as localizações (de A a P). 
- [ ] Uma função/método para determinar qual ação tomar. A decisão deve ser: Mover (em que direção), aspirar sujeira ou voltar para casa.
- [ ] Uma função/método para determinar em qual direção seguir.
- [ ] Uma função/método para idenƟficar a rota e navegar de volta para casa a parƟr da localização atual.
- [ ] Uma função/método para testar se o objeƟvo desejado foi alcançado ou não.
