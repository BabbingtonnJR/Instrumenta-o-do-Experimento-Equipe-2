# Situação do Aluno

Uma escola quer automatizar o resultado dos alunos no fim do semestre. Cada
aluno tem uma lista de notas, e a situação dele depende da média dessas notas.

Você precisa escrever a função `situacao_aluno(notas)` no arquivo
`src/notas.py`. Ela recebe uma lista de notas e devolve um texto dizendo a
situação do aluno.

A regra da escola é:

- média **7 ou mais**: `"Aprovado"`
- média **de 5 até menos de 7**: `"Recuperação"`
- média **menor que 5**: `"Reprovado"`

## Requisitos

1. A função deve se chamar `situacao_aluno` e ficar no arquivo `src/notas.py`.
2. A função deve calcular a média simples das notas (soma dividida pela quantidade).
3. A função deve devolver `"Aprovado"`, `"Recuperação"` ou `"Reprovado"`, escrito
   exatamente assim, conforme a regra acima.
4. Se a lista de notas estiver vazia, a função deve lançar `ValueError`.
5. Se alguma nota for menor que 0 ou maior que 10, a função deve lançar `ValueError`.

## Exemplos

```
Entrada: [8, 9, 10]
Saída:   "Aprovado"

Entrada: [7, 7, 7]
Saída:   "Aprovado"        (média exatamente 7 já aprova)

Entrada: [6, 5, 7]
Saída:   "Recuperação"

Entrada: [2, 3, 4]
Saída:   "Reprovado"

Entrada: []
Saída:   ValueError

Entrada: [8, 11, 9]
Saída:   ValueError        (não existe nota 11)
```

## Restrições

- As notas podem ser números inteiros ou com vírgula (ex.: `7.5`).
- Cada nota vale de 0 a 10.
- A lista pode ter até 20 notas.
- Use só Python puro, sem instalar bibliotecas na solução.

## Critérios de conclusão

A tarefa está pronta quando:

1. Todos os testes da pasta `tests` passam com `pytest -v`.
2. O nome da função e do arquivo não foram alterados.
3. O arquivo de testes não foi modificado.
4. A função não usa `print()` nem `input()`, apenas devolve o resultado com `return`.
5. O código foi enviado ao repositório em até 25 minutos.

## Estrutura

```
projeto/
├── README.md
├── requirements.txt
├── src/
│   └── notas.py        <- implemente aqui
└── tests/
    └── test_notas.py   <- testes (não mexer)
```

## Como rodar os testes

Dentro da pasta `projeto`:

```
pip install -r requirements.txt
pytest -v
```