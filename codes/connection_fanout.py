from qiskit import QuantumCircuit
from qiskit.circuit import Instruction
from codes.connection import con

# Connection:Fanout algorithm (qubits: Control, Resource1, Target1, Resource2, Target2)
def fanout() -> Instruction:
    
    qc = QuantumCircuit(5)
    '''qc.cx(0,1)
    qc.cx(0,3)
    qc.cx(1,2)
    qc.cx(3,4)'''
    qc.append(con(), [0,1,2])
    qc.append(con(), [0,3,4])
    
    instruction = qc.to_instruction(label=r"Fanout$^{C}_{R_1\to T_1,R_2\to T_2}$")
    
    return instruction