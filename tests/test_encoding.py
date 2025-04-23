from ..codes import encoding, helper
from matplotlib import pyplot as plt
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def test_encoding() -> None:
    
    # Encoding circuit
    qc = encoding()

    # Plotting circuit
    fig = plt.figure(figsize=(10,6))
    qc.draw("mpl", initial_state=True, fold=-1)
    plt.title("Encoding without additional registers", fontsize=16)
    plt.show()

    # Creating AER simulation locally
    aer_sim = AerSimulator(method='statevector')
    tqc = transpile(qc, aer_sim)
    result = aer_sim.run(tqc, shots=1000).result()
    sv_7 = result.data()["step 7"]

    # Trace out qubits except A and F
    dm_fin_af = trace_out(sv_7, [0,5])

    # Trace out qubits except B and E
    dm_fin_be = trace_out(sv_7, [1,4])

    # Plotting final density matrix (all qubits traced out except A, F)
    fig = plt.figure(figsize=(10,6))
    dm_fin_af.draw("city")
    plt.suptitle("After applying the encoding circuit this happens to A and F qubits (proof by checking density matrix)", fontsize=16)
    plt.show()

    # Plotting final density matrix (all qubits traced out except B, E)
    fig = plt.figure(figsize=(10,6))
    dm_fin_be.draw("city")
    plt.suptitle("After applying the encoding circuit this happens to B and E qubits (proof by checking density matrix)", fontsize=16)
    plt.show()

    # Building circuit for 2 qubit EPR pair Bell measurement (checking A, F qubits)
    probabilities_af, state_af = bell_measurement(dm_fin_af)

    # Plotting final result to A and F qubits (using Bell measurement)
    fig = plt.figure(figsize=(10,6))
    plot_histogram(probabilities_af)
    plt.title("After applying the encoding circuit this happens to A and F qubits (proof by doing Bell measurement)", fontsize=16)
    plt.show()
    print(f"Most likely Bell state: {state_af}")

    # Building circuit for 2 qubit EPR pair Bell measurement (checking B, E qubits)
    probabilities_be, state_be = bell_measurement(dm_fin_be)

    # Plotting final result to B and E qubits (using Bell measurement)
    fig = plt.figure(figsize=(10,6))
    plot_histogram(probabilities_be)
    plt.title("After applying the encoding circuit this happens to B and E qubits (proof by doing Bell measurement)", fontsize=16)
    plt.show()
    print(f"Most likely Bell state: {state_be}")

    # Debugging entanglement on the whole circuit
    #trace_debugger(sv_7, [0,5], 14)
    #trace_debugger(sv_7, [1,4], 14)