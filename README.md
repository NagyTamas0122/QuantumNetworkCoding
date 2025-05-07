# Quantum Network Coding

This is the repository for the simulation of Quantum Network Coding in Python Qiskit.

QNC - like its classical counterpart (Linear Network Coding) - gives answer to a network's scaling problem. It is modelled in a Quantum Repeater Network environment. You can use this instead of entanglement swapping in a butterfly network-like telecommunication system.

All modells are based on scientific paper: https://journals.aps.org/pra/abstract/10.1103/PhysRevA.86.032331

Installation guide: https://docs.quantum.ibm.com/guides/install-qiskit

Example step-by-step installation guide:
  - Clone the repository
    - For example: `git clone <link to the repository>`
  - Set up virtual environment
    - For example:
      - `python3 -m venv .venv`
      - On Windows: `.venv\Scripts\activate` || On Linux: `source .venv/bin/activate`
  - Install libraries using the requirements.txt file in the docs folder
    - For example: `pip install -r docs/requirements.txt`
  - Execute the main.py
    - For example: On Windows `.venv\Scripts\python.exe main.py` || On Linux: `.venv/bin/python main.py`