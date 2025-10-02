from codes.connection_add_circuit import connection_add_circuit
from matplotlib import pyplot as plt
from qiskit import transpile
from qiskit_aer import AerSimulator

def test_connection_add() -> None:
    
    # Connection:Add circuit
    qc = connection_add_circuit()

    # Plotting circuit
    qc.draw("mpl", initial_state=True)
    plt.title(r"Add$^{A,B}_{C\to D}$", fontsize=16)
    plt.show()

    # Creating AER simulation locally
    aer_sim = AerSimulator(method='statevector')
    tqc = transpile(qc, aer_sim)
    result = aer_sim.run(tqc, shots=100).result()
    sv_init = result.data()["init"]
    sv_fin = result.data()["fin"]

    # Plotting initial statevector
    sv_init.draw("city")
    plt.suptitle("Before applying the Connection:Add circuit", fontsize=16)
    plt.show()

    # Plotting final statevector
    sv_fin.draw("city")
    plt.suptitle("After applying the Connection:Add circuit", fontsize=16)
    plt.show()