from codes.connection import con
from codes.connection_add import add
from codes.connection_fanout import fanout
from codes.removal import rem
from codes.removal_add import remadd
from qiskit import QuantumCircuit, QuantumRegister

# Encoding circuit function
def encoding() -> QuantumCircuit:

    # Initialize quantum circuit
    qc = QuantumCircuit(QuantumRegister(1, name='A'),
                        QuantumRegister(1, name='B'),
                        QuantumRegister(1, name='C'),
                        QuantumRegister(1, name='D'),
                        QuantumRegister(1, name='E'),
                        QuantumRegister(1, name='F'),
                        QuantumRegister(1, name='G'),
                        QuantumRegister(1, name='H'),
                        QuantumRegister(1, name='I'),
                        QuantumRegister(1, name='J'),
                        QuantumRegister(1, name='K'),
                        QuantumRegister(1, name='L'),
                        QuantumRegister(1, name='M'),
                        QuantumRegister(1, name='N'))
    
    # Adding gates to the circuit

    # Input
    qc.h(0)
    qc.h(2)
    qc.h(4)
    qc.h(6)
    qc.h(8)
    qc.h(10)
    qc.h(12)
    qc.cx(0,1)
    qc.cx(2,3)
    qc.cx(4,5)
    qc.cx(6,7)
    qc.cx(8,9)
    qc.cx(10,11)
    qc.cx(12,13)
    #qc.save_statevector(label="input")
    qc.barrier(label="input")

    # Step 1
    qc.append(con(), [0,2,3])
    qc.append(con(), [4,6,7])
    #qc.save_statevector(label="step 1")
    qc.barrier(label="step 1")

    # Step 2
    qc.append(add(), [3,7,8,9])
    #qc.save_statevector(label="step 2")
    qc.barrier(label="step 2")

    # Step 3
    qc.append(fanout(), [9,10,11,12,13])
    #qc.save_statevector(label="step 3")
    qc.barrier(label="step 3")

    # Step 4
    qc.cx(11,1)
    qc.cx(13,5)
    #qc.save_statevector(label="step 4")
    qc.barrier(label="step 4")

    # Step 5
    qc.append(rem(), [11,9])
    qc.append(rem(), [13,9])
    #qc.save_statevector(label="step 5")
    qc.barrier(label="step 5")

    # Step 6
    qc.append(remadd(), [3,7,9])
    #qc.save_statevector(label="step 6")
    qc.barrier(label="step 6")

    # Step 7
    qc.append(rem(), [3,0])
    qc.append(rem(), [7,4])
    qc.save_statevector(label="step 7")

    return qc