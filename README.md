# Agente Aspirador
Atividade Avaliativa I - Inteligência Artificial <br>
- Alunos: 
  - André Lima
  - Carlos Mateus

## Objetivo 
Implementação de um Agente Racional que limpa um quarto com o mínimo possível de ações, o objetivo é que todo o ambiente esteja limpo e o agente retorne ao lar.

## Características da Atividade
- Todo o ambiente é dividido em quadrados de 4 por 4.
- O agente (aspirador de pó) tem uma energia inicial de 100 pontos.
- O agente pode se mover apenas para o Norte, Sul, Leste ou Oeste. Ele não pode se mover diagonalmente
- Cada ação custa 1 ponto de energia. Por exemplo, cada movimento custa 1 ponto de energia, cada aspiração custa 1 ponto de energia.
- O agente possui uma bolsa que coleta sujeira. A capacidade máxima é de 10.
- Após cada aspiração, o agente precisa verificar sua bolsa; se estiver cheia, ele deve voltar para Casa (localização A), esvaziar a bolsa e começar a aspirar novamente.

Ambiente:
<br>
![Screenshot_1](https://github.com/Treten312/agente-aspirador/assets/94249590/997716c8-0023-4fe8-98d8-78e78488caa6) 

## Parte A - Indentificação do P.E.A.S (Performance, Environment, Actuators and Sensors).

| Agente | Performance | Ambiente | Atuadores | Sensores |
| --- | --- | --- | --- | --- |
| Aspirador | Quantidade de sujeira limpa, Eficiencia de energia | Grade de quadrados 4x4 | Motores de movimento, Mecânismo de aspiração, Mecânismo de esvaziamente de bolsa | Sensor de sujeira, Sensor de energia, Sensor de proximidade |

## Parte B - Criação de código em Java ou Python para implementar o Agente Racional.
Checklist de implementações necessárias:
- [x] Implementação do ambiente estático, definir um array ou alguma outra estrutura de dados que representará as localizações (de A a P). 
- [x] Uma função/método para determinar qual ação tomar. A decisão deve ser: Mover (em que direção), aspirar sujeira ou voltar para casa.
- [x] Uma função/método para determinar em qual direção seguir.
- [ ] Uma função/método para identificar a rota e navegar de volta para casa a partir da localização atual.
- [ ] Uma função/método para testar se o objetivo desejado foi alcançado ou não.
