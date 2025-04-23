from codes.removal import rem
from qiskit import QuantumCircuit, QuantumRegister

# Removal circuit function
def removal_circuit() -> QuantumCircuit:

    # Initialize quantum circuit
    qc = QuantumCircuit(QuantumRegister(1, name='A'),
                        QuantumRegister(1, name='B'),
                        QuantumRegister(1, name='C'))

    # Adding gates to the circuit
    qc.h(0)
    qc.cx(0,1)
    qc.cx(0,2)
    qc.save_statevector(label="init")

    qc.append(rem(), [0,1])
    qc.save_statevector(label="fin")

    return qc