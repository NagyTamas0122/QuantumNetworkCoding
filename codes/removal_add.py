from qiskit import QuantumCircuit
from qiskit.circuit import Instruction

# Removal:Add algorithm (qubits: Resource, Target1, Target2)
def remadd() -> Instruction:
    
    qc = QuantumCircuit(3)
    qc.h(2)
    qc.cz(2,1)
    qc.cz(2,0)
    
    instruction = qc.to_instruction(label=r"RemAdd$_{R\to T_1,T_2}$")
    
    return instruction