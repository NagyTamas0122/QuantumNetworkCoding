from codes.connection import con
from codes.connection_add import add
from codes.connection_fanout import fanout
from codes.removal import rem
from codes.removal_add import remadd
from qiskit import QuantumCircuit, QuantumRegister

# Encoding circuit function
def encoding_2_2() -> QuantumCircuit:

    # Initialize quantum circuit
    qc = QuantumCircuit(QuantumRegister(1, name='A'), #0
                        QuantumRegister(1, name='B'), #1
                        QuantumRegister(1, name='C'), #2
                        QuantumRegister(1, name='D'), #3
                        QuantumRegister(1, name='E'), #4
                        QuantumRegister(1, name='F'), #5
                        QuantumRegister(1, name='G'), #6
                        QuantumRegister(1, name='H'), #7
                        QuantumRegister(1, name='I1'), #8
                        QuantumRegister(1, name='J1'), #9
                        QuantumRegister(1, name='I2'), #10
                        QuantumRegister(1, name='J2'), #11
                        QuantumRegister(1, name='K'), #12
                        QuantumRegister(1, name='L'), #13
                        QuantumRegister(1, name='M'), #14
                        QuantumRegister(1, name='N')) #15
    
    # Adding gates to the circuit

    # Input
    qc.h(0)
    qc.h(2)
    qc.h(4)
    qc.h(6)
    qc.h(8)
    qc.h(10)
    qc.h(12)
    qc.h(14)
    qc.cx(0,1)
    qc.cx(2,3)
    qc.cx(4,5)
    qc.cx(6,7)
    qc.cx(8,9)
    qc.cx(10,11)
    qc.cx(12,13)
    qc.cx(14,15)
    #qc.save_statevector(label="input")
    qc.barrier(label="input")

    # Step 1
    qc.append(con(), [0,2,3])
    qc.append(con(), [4,6,7])
    #qc.save_statevector(label="step 1")
    qc.barrier(label="step 1")

    # Step 2
    qc.append(con(), [9,10,11])
    qc.append(rem(), [9,8])
    #qc.save_statevector(label="step 2")
    qc.barrier(label="step 2")

    # Step 3
    qc.append(add(), [3,7,8,11])
    #qc.save_statevector(label="step 3")
    qc.barrier(label="step 3")

    # Step 4
    qc.append(fanout(), [11,12,13,14,15])
    #qc.save_statevector(label="step 4")
    qc.barrier(label="step 4")

    # Step 5
    qc.cx(13,1)
    qc.cx(15,5)
    #qc.save_statevector(label="step 5")
    qc.barrier(label="step 5")

    # Step 6
    qc.append(rem(), [13,11])
    qc.append(rem(), [15,11])
    #qc.save_statevector(label="step 6")
    qc.barrier(label="step 6")

    # Step 7
    qc.append(remadd(), [3,7,11])
    #qc.save_statevector(label="step 7")
    qc.barrier(label="step 7")

    # Step 8
    qc.append(rem(), [3,0])
    qc.append(rem(), [7,4])
    qc.save_statevector(label="step 8")

    return qc