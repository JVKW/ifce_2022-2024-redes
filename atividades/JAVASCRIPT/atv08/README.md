# Roteiro de Prática - Lista de Tarefas (To-Do List)

Neste tutorial, vamos criar uma aplicação simples de lista de tarefas (To-Do List) usando HTML, CSS e JavaScript. O objetivo é ensinar como manipular o DOM e utilizar eventos para criar uma aplicação interativa. Vamos implementar recursos de adição, marcação de conclusão e exclusão de tarefas. Siga o passo a passo!

## Resultado Final Esperado

  <img src="img-instrucoes/resultado.png">

---

## Estrutura do Projeto

- **index.html**: Estrutura HTML da aplicação.
- **index.css**: Estilos para tornar a lista visualmente agradável.
- **script.js**: Lógica de manipulação de DOM e eventos em JavaScript.

---

## 1. Estrutura Básica do HTML

Começaremos criando a estrutura HTML da nossa aplicação, com um campo de entrada, um botão
de adicionar e uma lista onde as tarefas serão exibidas.

### Código HTML:

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>To-Do List</title>
    <link rel="stylesheet" href="index.css" />
    <script src="main.js" defer></script>
  </head>
  <body>
    <div class="container">
      <div class="entrada">
        <input
          type="text"
          placeholder="Informe o nome da tarefa..."
          id="campoEntrada"
        />
        <button id="btnAdicionar">Adicionar</button>
      </div>

      <div>
        <h3>Tarefas</h3>
        <ul id="listaTarefas"></ul>
      </div>
    </div>
  </body>
</html>
```

> **Explicação**: Aqui, temos um campo de entrada (`<input>`), um botão de adicionar (`<button>`) e uma lista (`<ul>`) onde as tarefas serão exibidas. Os `IDs` atribuídos facilitarão a manipulação desses elementos a partir do JavaScript.

## 2. Estilo Visual com CSS

Agora, vamos estilizar nossa lista de tarefas para deixá-la visualmente agradável. Vamos adicionar estilos para o layout, botões e a aparência das tarefas concluídas.

### Passo a Passo:

1. Crie um arquivo chamado `index.css`.
1. Adicione o estilo básico, incluindo um estilo para tarefas concluídas e para o efeito de erro.

### Código CSS (index.css):

```css
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

* {
  box-sizing: border-box;
}

body {
  padding: 0;
  margin: 0;
  height: 100vh;
  width: 100vw;
  font-family: Verdana;
  display: flex;
  justify-content: center;
  background-color: #f0f8ff;
}

.container {
  width: 400px;
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  row-gap: 1rem;
}

.entrada {
  display: flex;
  width: 100%;
  gap: 1rem;

  & > * {
    padding: 0.5rem;
    font-size: 1rem;
  }

  & input {
    flex: 1;
    border: none;
    border-bottom: 1px solid #40a640;
    outline: none;
    background-color: transparent;
  }

  & button {
    background-color: #40a640;
    color: #ffffff;
    border: none;
    cursor: pointer;
    border-radius: 4px;

    &:hover {
      background-color: #59b959;
    }
  }
}

#listaTarefas {
  width: 100%;
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  row-gap: 12px;

  & button {
    all: unset;
  }

  & li {
    cursor: pointer;
    display: flex;
    background-color: #ffffff;
    border-radius: 4px;

    & span {
      flex: 1;
      padding: 12px;
    }

    & i {
      padding: 12px;
      border-radius: 4px;
    }

    & i:hover {
      background-color: #dc143c;
      color: #ffffff;
    }
  }

  & li:hover {
    background-color: #d4dce2;
  }
}

span.concluida {
  text-decoration: line-through;
  color: #778899;
}

#campoEntrada.input-erro {
  border-bottom: 1px solid #dc143c;
  background-color: #ffe5e5;
}
```
> **Explicação**: Este código CSS utiliza a biblioteca [Bootstrap Icons](https://icons.getbootstrap.com/) para os ícones. Ele também emprega seletores aninhados usando o `&`, uma funcionalidade comum em pré-processadores CSS como Sass, porém já é suportado nativamente pelo CSS. Abaixo está uma explicação detalhada de cada parte.
>
> **Importação da Biblioteca Bootstrap Icons**
> ```css
> @import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");
> ```
>  - Esta linha importa a biblioteca Bootstrap Icons diretamente de um CDN, permitindo o uso de ícones como o de "lixeira" para excluir tarefas. Esse recurso facilita a adição de ícones padrão sem precisar baixar os arquivos localmente.
>
> **Resumo dos Seletores Aninhados com &**
> - O `&` é usado para criar seletores aninhados, permitindo que estilos dependam do contexto onde estão. Ele é substituído pelo seletor pai, facilitando a organização do CSS e a aplicação de estilos condicionais.
> - **Exemplo:** 
> ```css
> .entrada {
>  display: flex;
>  width: 100%;
>  gap: 1rem;
>
>  & > * {
>    padding: 0.5rem;
>    font-size: 1rem;
>  }
>
>  & input {
>    flex: 1;
>    border: none;
>    border-bottom: 1px solid #40a640;
>    outline: none;
>    background-color: transparent;
>  }
> ...
> }
> ```
> - O seletor `& > *` está dentro do contexto do seletor `.entrada`, logo é a mesma coisa que `.entrada > *`. Assim como o seletor `& input`, que tem o mesmo efeito de `.entrada input`.
> - Lembrando que o `>` é um seletor de filho imediato, enquanto o `*` seleciona todos os elementos em um determinado contexto (`.entrada > *` — seleciona todos os elementos que são filhos imediatos do elemento com a classe `entrada`).

---

## 3. Adicionando JavaScript para Manipulação do DOM

Agora vamos criar a lógica da aplicação em JavaScript para adicionar, marcar e remover tarefas.

### Código JavaScript (script.js):

```javascript
const campoEntrada = document.getElementById("campoEntrada");
const btnAdicionar = document.getElementById("btnAdicionar");

const listaTarefas = document.getElementById("listaTarefas");
// Adicionar tarefa
btnAdicionar.addEventListener("click", function () {
  const tarefaTexto = campoEntrada.value.trim();
  if (tarefaTexto !== "") {
    const tarefa = document.createElement("li");
    tarefa.textContent = tarefaTexto;
    // Botão de concluir tarefa
    tarefa.addEventListener("click", function () {
      tarefa.classList.toggle("concluida");
    });
    // Botão de excluir tarefa
    const btnExcluir = document.createElement("button");
    btnExcluir.textContent = "Excluir";
    btnExcluir.addEventListener("click", function () {
      listaTarefas.removeChild(tarefa);
    });
    tarefa.appendChild(btnExcluir);
    listaTarefas.appendChild(tarefa);
    campoEntrada.value = "";
  } else {
    campoEntrada.classList.add("input-erro");

    setTimeout(() => campoEntrada.classList.remove("input-erro"), 1500);
  }
});
```

---

## Conclusão

Este projeto de Lista de Tarefas é uma introdução prática para manipulação de DOM e eventos
com JavaScript. Ele ensina como criar, modificar e excluir elementos dinamicamente no HTML,
além de gerenciar estados visuais com CSS e interação de usuários.
