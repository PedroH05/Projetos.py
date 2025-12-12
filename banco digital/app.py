import tkinter as tk
from tkinter import messagebox

from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from clientes.cliente import Cliente

cliente = Cliente("Pedro", "123.456.789-00", "Rua Exemplo, 123")
conta_cc = ContaCorrente(cliente, 1001, saldo=0, limite=500)
conta_cp = ContaPoupanca(cliente, 2001, saldo=0)

contas = {
    "Conta Corrente": conta_cc,
    "Conta Poupança": conta_cp
}

janela = tk.Tk()
janela.title("Banco Digital - Pedro")
janela.geometry("350x380")

tk.Label(janela, text="Escolha a conta:", font=("Arial", 12)).pack(pady=5)
conta_var = tk.StringVar(janela)
conta_var.set("Conta Corrente")

menu_contas = tk.OptionMenu(janela, conta_var, *contas.keys())
menu_contas.pack(pady=5)


tk.Label(janela, text="Valor:", font=("Arial", 12)).pack(pady=5)
valor_entry = tk.Entry(janela)
valor_entry.pack(pady=5)


def depositar():
    try:
        valor = float(valor_entry.get())
        conta = contas[conta_var.get()]
        conta.depositar(valor)
        messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado!")
    except:
        messagebox.showerror("Erro", "Valor inválido.")

def sacar():
    try:
        valor = float(valor_entry.get())
        conta = contas[conta_var.get()]
        if conta.sacar(valor):
            messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado!")
        else:
            messagebox.showerror("Erro", "Saque não permitido.")
    except:
        messagebox.showerror("Erro", "Valor inválido.")

def mostrar_saldo():
    conta = contas[conta_var.get()]
    messagebox.showinfo("Saldo", f"Saldo atual: R$ {conta.saldo:.2f}")

def historico():
    conta = contas[conta_var.get()]
    texto = ""
    for trans in conta.historico:
        texto += f"{trans}\n"

    if texto == "":
        texto = "Nenhuma transação ainda."

    messagebox.showinfo("Histórico", texto)

tk.Button(janela, text="Depositar", command=depositar, width=20).pack(pady=5)
tk.Button(janela, text="Sacar", command=sacar, width=20).pack(pady=5)
tk.Button(janela, text="Saldo", command=mostrar_saldo, width=20).pack(pady=5)
tk.Button(janela, text="Histórico", command=historico, width=20).pack(pady=5)


janela.mainloop()
