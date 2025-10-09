from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, DensityMatrix, partial_trace
from typing import Tuple, List, Dict
import numpy as np

# Trace out some qubits from a statevector while keeping others
def trace_out(total_qubits: int, sv: Statevector, keep_qubit_list: List[int]) -> DensityMatrix:
    
    all_qubits = list(range(total_qubits))
    trace_out = [q for q in all_qubits if q not in keep_qubit_list]
    dm = partial_trace(sv, trace_out)
    
    return dm

# Creating Quantum circuit for 2 qubit EPR pair Bell measurement
def bell_measurement(dm: DensityMatrix) -> Tuple[Dict, str, str]:
    
    qc_bell = QuantumCircuit(2)
    qc_bell.cx(0,1)
    qc_bell.h(0)
    
    dm_bell = dm.evolve(qc_bell)
    probabilities = dm_bell.probabilities_dict()
    likely_result = max(probabilities, key=probabilities.get)
    bell_map = {
        '00': r'|Φ⁺⟩ = (|00⟩ + |11⟩) / √2',
        '01': r'|Ψ⁺⟩ = (|01⟩ + |10⟩) / √2',
        '10': r'|Φ⁻⟩ = (|00⟩ - |11⟩) / √2',
        '11': r'|Ψ⁻⟩ = (|01⟩ - |10⟩) / √2',
    }
    bell_state = bell_map.get(likely_result, 'Unknown')
    
    purity = np.real(np.trace(dm.data @ dm.data))
    
    return probabilities, bell_state, purity

# Helper function to debug entanglement on a whole circuit
def trace_debugger(global_state: Statevector | DensityMatrix, target_qubits: List[int], total_qubits: int) -> None:
    
    if isinstance(global_state, Statevector):
        global_state = DensityMatrix(global_state)

    all_indices = list(range(total_qubits))
    rest_indices = [i for i in all_indices if i not in target_qubits]
    
    reduced_state = partial_trace(global_state, rest_indices)
    rho_squared = reduced_state.data @ reduced_state.data
    full_purity = np.trace(rho_squared.data).real

    print(f"\nPurity of target qubits {target_qubits}: {full_purity:.4f}")
    if np.isclose(full_purity, 1.0):
        print("Target pair is NOT entangled with the rest.")
    else:
        print("Target pair IS entangled with the rest of the system.")

    entangled_with = []
    for i in rest_indices:
        subset = partial_trace(global_state, [j for j in all_indices if j not in target_qubits + [i]])
        purity = np.trace(subset.data @ subset.data).real
        if not np.isclose(purity, 1.0):
            entangled_with.append(i)
            print(f"\tEntangled with qubit {i} (purity: {purity:.4f})")

    if not entangled_with:
        print("No individual qubit is entangled with the pair.")

# List all of the quantum registers of a circuit
def list_qubit_registers(qc: QuantumCircuit):
    for i, q in enumerate(qc.qubits):
        print(f"{i}: {q}")
    print("\n")