from codes.connection_add import add
from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

# Connection:Add circuit function
def connection_add_circuit() -> QuantumCircuit:

    # Initialize quantum circuit
    qc = QuantumCircuit(QuantumRegister(1, name='A'),
                        QuantumRegister(1, name='B'),
                        QuantumRegister(1, name='C'),
                        QuantumRegister(1, name='D'))

    # Initialize A and B quantum registers to superposition
    alpha = beta = gamma = delta = 1/np.sqrt(2)
    qc.initialize([alpha, beta], qc.qregs[0])
    qc.initialize([gamma, delta], qc.qregs[1])

    # Adding gates to the circuit
    qc.h(2)
    qc.cx(2,3)
    qc.save_statevector(label="init")

    qc.append(add(), [0,1,2,3])
    qc.save_statevector(label="fin")

    return qc