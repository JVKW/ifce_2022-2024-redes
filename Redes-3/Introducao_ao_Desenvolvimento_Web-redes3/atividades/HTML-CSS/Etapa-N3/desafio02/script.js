import { collection, addDoc, doc, deleteDoc, query, onSnapshot, updateDoc } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-firestore.js";
import { db } from "./firebase.js";
import { monitarTarefas } from './controllers.js';  // Importa a função de monitoramento de tarefas

const campoEntrada = document.getElementById("campoEntrada");
const btnAdicionar = document.getElementById("btnAdicionar");
const listaTarefas = document.getElementById("listaTarefas");

async function novaTarefa() {
    const nomeTarefa = campoEntrada.value.trim();

    if (nomeTarefa === "") {
        campoEntrada.classList.add("input-erro");
        setTimeout(() => campoEntrada.classList.remove("input-erro"), 1500);
        return;
    }

    try {
        const ref = collection(db, "tarefas");
        await addDoc(ref, { descricao: nomeTarefa, status: "pendente" });
        campoEntrada.value = "";
        carregarTarefas();
    } catch (error) {
        console.error("Erro ao adicionar tarefa:", error);
    }
}

function exibirTarefa(id, descricao, status) {
    const itemTarefa = document.createElement("li");
    const span = document.createElement("span");
    const btnExcluir = document.createElement("button");

    span.innerText = descricao;
    if (status === "concluida") {
        span.classList.add("concluida");
    }

    // Alternar status da tarefa
    span.onclick = async () => {
        const novoStatus = span.classList.toggle("concluida") ? "concluida" : "pendente";
        try {
            const ref = doc(db, "tarefas", id);
            await updateDoc(ref, { status: novoStatus });
        } catch (error) {
            console.error("Erro ao atualizar status:", error);
        }
    };

    // Botão de exclusão
    btnExcluir.innerHTML = "<i class='bi bi-trash'></i>";
    btnExcluir.onclick = async () => {
        try {
            const ref = doc(db, "tarefas", id);
            await deleteDoc(ref);
        } catch (error) {
            console.error("Erro ao excluir tarefa:", error);
        }
    };

    itemTarefa.appendChild(span);
    itemTarefa.appendChild(btnExcluir);
    listaTarefas.appendChild(itemTarefa);
}

function carregarTarefas() {
    const ref = collection(db, "tarefas");
    const q = query(ref);

    onSnapshot(q, (snapshot) => {
        listaTarefas.innerHTML = "";
        snapshot.forEach((doc) => {
            const { descricao, status } = doc.data();
            exibirTarefa(doc.id, descricao, status);
        });
    });
};

btnAdicionar.onclick = novaTarefa;

campoEntrada.onkeydown = (evento) => {
    if (evento.key === "Enter") {
        novaTarefa();
    }
};

carregarTarefas();

// Usuário teste
// A implementação de Login de Usuários não está aplicada, por enquanto, o valor id usuário padrão segue 'Teste'
const usuarioId = 'Test';


monitarTarefas(usuarioId);
