from qiskit import QuantumCircuit
from qiskit.circuit import Instruction

# Removal algorithm (qubits: Resource, Target)
def rem() -> Instruction:
    
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cz(0,1)
    
    instruction = qc.to_instruction(label=r"Rem$_{R\to T}$")
    
    return instruction