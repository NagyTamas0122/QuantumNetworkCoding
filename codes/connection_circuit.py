from codes.connection import con
from qiskit import QuantumCircuit, QuantumRegister

# Connection circuit function
def connection_circuit() -> QuantumCircuit:
    
    # Initialize quantum circuit
    qc = QuantumCircuit(QuantumRegister(1, name='A'),
                        QuantumRegister(1, name='B'),
                        QuantumRegister(1, name='C'),
                        QuantumRegister(1, name='D'))

    # Adding gates to the circuit
    qc.h(0)
    qc.h(2)
    qc.cx(0,1)
    qc.cx(2,3)
    qc.save_statevector(label="init")

    qc.append(con(), [0,2,3])
    qc.save_statevector(label="fin")

    return qc