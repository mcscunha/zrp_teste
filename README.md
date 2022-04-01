# Sistema em Flask para acesso a dados de Pokemons via API

---

#### Objetivo

Este projeto faz parte de uma avaliação online na empresa ZRP e serve como prova de conhecimento nos assuntos:
- Python 3 (manipulacao de dicionarios e listas)
- Flask (apresentacao dos dados no navegador e acesso a API de terceiros)
- Docker (uso de ambiente controlado)
- Git (distribuicao de codigos para outros membros)
- Tempo de resposta (conclusao em menos de 24 horas)


#### Requisitos
Apresentar um sistema montado com Flask que acessa uma API externa (Pokemons - https://pokeapi.co/api/v2/pokemons/nome_pokemon) e pegue os dados de resposta.
Com estes dados, filtre algumas informacoes de maneira que a resposta final seja semelhante a essa:

*Usando o pokemon "ditto" como filtro de procura*
```json
{
  abilities: ["imposter", "limber"],
  items: [
    {
      name:"metal-powder",
      cost: 1000,
    }, 
    {
      name:"quick-powder",
      cost: 1000,
    }
  ]
}
```
No primeiro item `abilities`, a lista deve estar em ordem alfabetica.

---

#### Passos adicionais

1. Quando tudo estiver pronto, subir os codigos em um repositorio no Github para o avaliador baixar e executar na maquina local

2. Escrever um README para instruir como executar o projeto. Deve ser bem simples, no maximo, 2 instrucoes para colocar no ar e avaliar

3. Para obter a resposta desejada, o usuario deve digitar no navegador: `http://localhost:8000/api/pokemons/ditto` e receber como resposta:
```json
{
    abilities: ["imposter", "limber"],
  items: [
      {
          name:"metal-powder",
      cost: 1000,
    }, 
    {
        name:"quick-powder",
      cost: 1000,
    }
  ]
}
```

---

#### Para executar esse projeto

Na linha de comando digite:
```sh
docker-compose up --build --remove-orphans
```
Abra o navegador e entre com a URL principal para instruçoes
`http://localhost:8000`