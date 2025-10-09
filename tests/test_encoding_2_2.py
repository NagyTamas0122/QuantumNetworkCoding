from codes.encoding_2_2 import encoding_2_2
from codes.helper import trace_out, bell_measurement, trace_debugger, list_qubit_registers
from matplotlib import pyplot as plt
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def test_encoding_2_2() -> None:
    
    # Encoding circuit
    qc = encoding_2_2()
    list_qubit_registers(qc)

    # Plotting circuit
    qc.draw("mpl", initial_state=True, fold=-1)
    plt.title("Encoding (N=2, M=2) circuit without additional registers", fontsize=16)
    plt.show()

    # Creating AER simulation locally
    aer_sim = AerSimulator(method='statevector')
    tqc = transpile(qc, aer_sim)
    result = aer_sim.run(tqc, shots=1000).result()
    sv_8 = result.data()["step 8"]

    # Trace out qubits except A and F
    dm_fin_af = trace_out(16, sv_8, [0,5])

    # Trace out qubits except B and E
    dm_fin_be = trace_out(16, sv_8, [1,4])

    # Plotting final density matrix (all qubits traced out except A, F)
    dm_fin_af.draw("city")
    plt.suptitle("After applying the Encoding circuit this happens to A and F qubits (proof by checking density matrix)", fontsize=16)
    plt.show()

    # Plotting final density matrix (all qubits traced out except B, E)
    dm_fin_be.draw("city")
    plt.suptitle("After applying the Encoding circuit this happens to B and E qubits (proof by checking density matrix)", fontsize=16)
    plt.show()

    # Building circuit for 2 qubit EPR pair Bell measurement (checking A, F qubits)
    probabilities_af, state_af, purity_af = bell_measurement(dm_fin_af)

    # Plotting final result to A and F qubits (using Bell measurement)
    plot_histogram(probabilities_af)
    plt.title("After applying the Encoding circuit this happens to A and F qubits (proof by doing Bell measurement)", fontsize=16)
    plt.show()
    print(f"Most likely Bell state for entangled A, F qubits: {state_af}\n")
    print(f"Purity of the Bell state of entangled A, F qubits: {purity_af:.4f}\n")

    # Building circuit for 2 qubit EPR pair Bell measurement (checking B, E qubits)
    probabilities_be, state_be, purity_be = bell_measurement(dm_fin_be)

    # Plotting final result to B and E qubits (using Bell measurement)
    plot_histogram(probabilities_be)
    plt.title("After applying the Encoding circuit this happens to B and E qubits (proof by doing Bell measurement)", fontsize=16)
    plt.show()
    print(f"Most likely Bell state for entangled B, E qubits: {state_be}\n")
    print(f"Purity of the Bell state of entangled B, E qubits: {purity_be:.4f}\n")
    
    # Debugging entanglement on the whole circuit
    #trace_debugger(sv_8, [0,5], 16)
    #trace_debugger(sv_8, [1,4], 16)