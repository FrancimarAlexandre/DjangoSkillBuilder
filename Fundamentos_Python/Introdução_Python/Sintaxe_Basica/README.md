Link de referência <a href = "https://pythoniluminado.netlify.app/sintaxe">Python iluminado</a>


# Sintaxe do Python

Python foi originalmente desenvolvido como uma linguagem de ensino, mas sua facilidade de uso e sintaxe limpa levaram-no a ser adotado tanto por iniciantes quanto por especialistas.

A sintaxe da linguagem de programação Python é o conjunto de regras que define como um programa Python será escrito e interpretado (tanto pelo sistema de execução quanto por leitores humanos).

## Palavras-chave em Python

As palavras-chave são termos reservados pela linguagem Python que não podem ser usados para nomear variáveis, funções ou qualquer outro identificador. Elas são fundamentais para definir a sintaxe e a estrutura da linguagem. É importante lembrar que as palavras-chave são sensíveis a maiúsculas e minúsculas (case-sensitive) e devem ser escritas exatamente como são.

A seguir está a lista de todas as palavras-chave em Python:

| Nome       | Descrição                                      |
|------------|------------------------------------------------|
| and        | operador lógico "e"                            |
| as         | usado para criar um alias                      |
| assert     | utilizado para debugging                       |
| async      | utilizado para escrever aplicações asyncio     |
| await      | utilizado para escrever aplicações asyncio     |
| break      | utilizado para sair de um loop                 |
| class      | define uma classe                              |
| continue   | continua para a próxima iteração do loop       |
| def        | define uma função                              |
| del        | deleta um objeto                               |
| elif       | utilizado em comandos condicionais, como else e if |
| else       | utilizado em comandos condicionais             |
| except     | utilizado para tratar exceções                 |
| False      | valor booleano, resulta de operações de comparação |
| finally    | bloco de código que executará independente de exceção |
| for        | utilizado para criar um loop                   |
| from       | utilizado para importar partes específicas de um módulo |
| global     | declara uma variável global                    |
| if         | utilizado para comandos condicionais           |
| import     | utilizado para importar módulos                |
| in         | verifica se um valor está presente em uma lista, tupla, etc |
| is         | testa se duas variáveis são iguais             |
| lambda     | cria uma função anônima                        |
| None       | representa um valor nulo                       |
| nonlocal   | declara uma variável não local                 |
| not        | operador lógico de negação                     |
| or         | operador lógico "ou"                           |
| pass       | comando nulo, um comando que não faz nada      |
| raise      | dispara uma exceção                            |
| return     | sai de uma função e retorna um valor           |
| True       | valor booleano, resulta de operações de comparação |
| try        | comando utilizado com exceções                 |
| while      | cria um loop while                             |
| with       | simplifica a manipulação de exceções           |
| yield      | finaliza uma função e retorna um gerador       |

Para obter as palavras-chave através do interpretador Python, você pode usar o seguinte comando:

```python
import keyword
print(keyword.kwlist)
```

Este comando retornará uma lista com todas as palavras-chave da linguagem Python.

## Identificadores

Identificadores são nomes dados a entidades como variáveis, funções, classes, etc., ajudando a diferenciar uma entidade da outra.

### Regras para Identificadores

- Podem conter letras em minúsculas (a a z), maiúsculas (A a Z), dígitos (0 a 9) ou underline (_).
- São sensíveis a maiúsculas e minúsculas (case-sensitive).
- Não podem começar com dígitos.
- Palavras-chave não podem ser usadas como identificadores.

Exemplos de identificadores válidos: `minhaClasse`, `variavel_1`, `minha_variavel`.

## Indentação

A indentação é crucial em Python, pois é usada para indicar blocos de código. Diferente de outras linguagens onde a indentação é apenas para melhorar a legibilidade, em Python ela é obrigatória.

### Regras de Indentação

- Use dois pontos (:) para iniciar um bloco de código e pressione [Enter].
- Todas as linhas em um bloco devem ter a mesma quantidade de espaços ou tabulações.
- É recomendado usar quatro espaços para cada nível de indentação.
- Não misture espaços e tabulações no mesmo bloco.

Exemplo:

```python
vida = 100
if vida > 0:
    print("Você está vivo")
```

## Comentários

Comentários em Python tornam o código mais legível e melhoram a comunicação entre programadores.

- Comentários de uma linha começam com `#`.

  ```python
  # Este é um comentário
  print("Códigos comentados são mais fáceis de compreender")
  ```

- Docstrings são utilizados para comentários que abrangem várias linhas.

  ```python
  """
  Este é um comentário
  que abrange várias
  linhas do programa
  """
  print("Procure sempre comentar o seu código")
  ```

## Instruções

Instruções em Python geralmente terminam com uma nova linha, mas é possível usar o caractere de continuação de linha (`\`) para indicar que a linha deve continuar.

Exemplo:

```python
total = 3 + \
    5 + \
    7
print(total)  # 15
```

O ponto e vírgula (`;`) permite várias instruções em uma única linha.

Exemplo:

```python
x, y = 9, 3; z = x * y; print(f'{x} x {y} = {z}')
# 9 x 3 = 27
```

Para detalhes específicos e boas práticas de estilo de programação em Python, recomendamos a leitura da [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).