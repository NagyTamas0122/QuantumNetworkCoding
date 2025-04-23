from qiskit import QuantumCircuit
from qiskit.circuit import Instruction

# Connection:Add algorithm (qubits: Control1, Control2, Resource, Target)
def add() -> Instruction:
    
    qc = QuantumCircuit(4)
    qc.cx(0,2)
    qc.cx(1,2)
    qc.cx(2,3)
    
    instruction = qc.to_instruction(label=r"Add$^{C_1,C_2}_{R\to T}$")
    
    return instruction