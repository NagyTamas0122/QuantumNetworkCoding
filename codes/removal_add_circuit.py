import removal_add

# Removal:Add circuit function
def removal_add_circuit() -> QuantumCircuit:

    # Initialize quantum circuit
    qc = QuantumCircuit(QuantumRegister(1, name='A'),
                        QuantumRegister(1, name='B'),
                        QuantumRegister(1, name='C'))

    # Initialize A and B quantum registers to superposition
    alpha = beta = gamma = delta = 1/np.sqrt(2)
    qc.initialize([alpha, beta], qc.qregs[0])
    qc.initialize([gamma, delta], qc.qregs[1])

    # Adding gates to the circuit
    qc.cx(0,2)
    qc.cx(1,2)
    qc.save_statevector(label="init")

    qc.append(remadd(), [0,1,2])
    qc.save_statevector(label="fin")

    return qc