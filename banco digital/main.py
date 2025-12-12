from clientes.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca

cliente = Cliente("Pedro", "123.456.789-00", "Rua Exemplo, 123")

conta_cc = ContaCorrente(cliente, numero_conta=1001, saldo=0, limite=500)
conta_cp = ContaPoupanca(cliente, numero_conta=2001, saldo=0)

print("\n--- DEPÓSITOS ---")
conta_cc.depositar(300)
conta_cp.depositar(200)

print("\n--- SAQUES ---")
conta_cc.sacar(100)
conta_cp.sacar(50)

print("\n--- TRANSFERÊNCIAS ---")
conta_cc.transferir(50, conta_cp)
conta_cp.transferir(30, conta_cc)

print("\n--- SALDOS ---")
print(conta_cc)
print(conta_cp)

print("\n--- HISTÓRICO CC ---")
conta_cc.exibir_extrato()

print("\n--- HISTÓRICO CP ---")
conta_cp.exibir_extrato()
