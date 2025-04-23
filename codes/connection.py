from qiskit import QuantumCircuit
from qiskit.circuit import Instruction

# Connection algorithm (qubits: Control, Resource, Target)
def con() -> Instruction:
    
    qc = QuantumCircuit(3)
    qc.cx(0,1)
    qc.cx(1,2)
    
    instruction = qc.to_instruction(label=r"Con$^{C}_{R\to T}$")
    
    return instruction