from ..codes import connection_fanout_circuit
from matplotlib import pyplot as plt
from qiskit import transpile
from qiskit_aer import AerSimulator

def test_connection_fanout() -> None:
    
    # Connection:Fanout circuit
    qc = connection_fanout_circuit()

    # Plotting circuit
    fig = plt.figure(figsize=(10,6))
    qc.draw("mpl", initial_state=True)
    plt.title(r"Fanout$^{A}_{B\to C,D\to E}$", fontsize=16)
    plt.show()

    # Creating AER simulation locally
    aer_sim = AerSimulator(method='statevector')
    tqc = transpile(qc, aer_sim)
    result = aer_sim.run(tqc, shots=100).result()
    sv_init = result.data()["init"]
    sv_fin = result.data()["fin"]

    # Plotting initial statevector
    fig = plt.figure(figsize=(10,6))
    sv_init.draw("city")
    plt.suptitle("Before applying the connection:fanout circuit", fontsize=16)
    plt.show()

    # Plotting final statevector
    fig = plt.figure(figsize=(10,6))
    sv_fin.draw("city")
    plt.suptitle("After applying the connection:fanout circuit", fontsize=16)
    plt.show()