from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

qc = QuantumCircuit(2, 2)

# Step 1: Superposition
qc.h(0)
qc.h(1)

# Step 2: Oracle (mark |11>)
qc.cz(0, 1)

# Step 3: Diffuser
qc.h(0)
qc.h(1)

qc.x(0)
qc.x(1)

qc.cz(0, 1)

qc.x(0)
qc.x(1)

qc.h(0)
qc.h(1)

# Step 4: Measurement
qc.measure([0, 1], [0, 1])

# Simulator
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

counts = result.get_counts(qc)
print("Measurement Results:", counts)


from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

# Draw circuit in text
print("\nQuantum Circuit:")
print(qc)

# Draw circuit as image
circuit_drawer(qc, output='mpl', filename='grover_circuit.png')
print("\nCircuit saved as 'grover_circuit.png' in project folder.")

# Plot histogram of measurement results
plot_histogram(counts)
plt.show()
