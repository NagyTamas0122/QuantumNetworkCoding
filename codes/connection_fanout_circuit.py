import connection_fanout

# Connection:Fanout circuit function
def connection_fanout_circuit() -> QuantumCircuit:

    # Initialize quantum circuit
    qc = QuantumCircuit(QuantumRegister(1, name='A'),
                        QuantumRegister(1, name='B'),
                        QuantumRegister(1, name='C'),
                        QuantumRegister(1, name='D'),
                        QuantumRegister(1, name='E'))

    # Initialize A quantum register to superposition
    alpha = beta = 1/np.sqrt(2)
    qc.initialize([alpha, beta], qc.qregs[0])

    # Adding gates to the circuit
    qc.h(1)
    qc.h(3)
    qc.cx(1,2)
    qc.cx(3,4)
    qc.save_statevector(label="init")
    
    qc.append(fanout(), [0,1,2,3,4])
    qc.save_statevector(label="fin")
    
    return qc