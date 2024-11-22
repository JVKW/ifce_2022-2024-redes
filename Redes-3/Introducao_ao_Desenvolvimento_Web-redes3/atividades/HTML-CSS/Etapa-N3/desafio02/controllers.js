import { collection, addDoc, query, where, getDocs, doc, updateDoc, deleteDoc, onSnapshot } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-firestore.js";
import { db } from './firebase.js';

async function adicionarTarefa(descricao, status, usuarioId) {
    try {
        const ref = collection(db, "tarefas");
        await addDoc(ref, { descricao, status, usuarioId });
        console.log("Tarefa adicionada com sucesso!");
    } catch (error) {
        console.error("Erro ao adicionar tarefa:", error);
    }
};

async function listarTarefas(usuarioId) {
    try {
        const ref = collection(db, "tarefas");
        const q = query(ref, where("usuarioId", "==", usuarioId));
        const snapshot = await getDocs(q);

        snapshot.forEach((doc) => {
            console.log(doc.id, " => ", doc.data());
        });
    } catch (error) {
        console.log("Erro ao listar tarefas:", error);
    }
}

async function atualizarTarefa(idTarefa, novosDados) {
    try {
        const ref = doc(db, "tarefas", idTarefa);
        await updateDoc(ref, novosDados);
        console.log("Tarefa " + idTarefa + " atualizada!");
    } catch (error) {
        console.error("Erro ao atualizar tarefa:", error);
    }
}

async function excluirTarefa(idTarefa) {
    try {
        const ref = doc(db, "tarefas", idTarefa);
        await deleteDoc(ref);
        console.log("Tarefa excluída!");
    } catch (error) {
        console.error("Erro ao excluir a tarefa:", error);
    }
}

function monitarTarefas(usuarioId) {
    const ref = collection(db, "tarefas");
    const q = query(ref, where("usuarioId", "==", usuarioId));

    onSnapshot(q, (snapshot) => {
        snapshot.forEach((doc) => {
            console.log(doc.id, " => ", doc.data());
        });
    });
}

export { adicionarTarefa, listarTarefas, atualizarTarefa, excluirTarefa, monitarTarefas };
