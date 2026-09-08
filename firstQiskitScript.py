from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler
import matplotlib.pyplot as plt

# 1. Initialize the Bell state circuit (|Φ+> state)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print(qc)
qc.draw('mpl')
plt.show()

# 2. Connect to IBM Quantum service and select 'ibm_fez'
QiskitRuntimeService().save_account(channel='ibm_quantum_platform',token='krkSgKhCtWa05zkyZo7ztFHf5VK44PSJV6FODAjNi-KA',overwrite=True)
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)

# 3. Transpile the circuit to match the backend's Instruction Set Architecture (ISA) -- Critical
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)
print(isa_circuit)
isa_circuit.draw('mpl')
plt.show()

# 4. Run the circuit using the Sampler primitive
sampler = Sampler(mode=backend)
job = sampler.run([isa_circuit], shots=1024)
result = job.result()

# 5. Extract counts and compute the probabilities
pub_result = result[0]
counts = pub_result.data.meas.get_counts()
total_shots = sum(counts.values())

print("Measurement Counts:", counts)
print("\nCalculated Probabilities:")
for outcome, count in counts.items():
  probability = (count / total_shots) * 100
  print(f"State |{outcome}⟩: {probability:.2f}% ({count}/{total_shots} shots)")
