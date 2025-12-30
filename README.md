# Grover’s Algorithm Simulation

## Overview
This project is a simple simulation of **Grover’s Search Algorithm** using Python and Qiskit.  
Grover’s algorithm is a quantum algorithm that can search an unsorted database faster than a classical approach by using quantum superposition and amplitude amplification.

The implementation uses a 2-qubit system to clearly demonstrate how the oracle marks a target state and how the diffuser increases its probability during measurement.

## What This Project Does
- Implements Grover’s Algorithm for a 2-qubit quantum system
- Creates an oracle to mark the target state
- Applies the diffuser to amplify the marked state
- Simulates the circuit using Qiskit Aer
- Visualizes the quantum circuit
- Displays a histogram of measurement outcomes

## Tech Stack
- Python  
- Qiskit  
- Matplotlib  

## How to Run the Project

### 1. Install dependencies
Make sure Python is installed, then run:
```bash
pip install qiskit qiskit-aer matplotlib pylatexenc
```
TO execute the code,
```bash
python grover.py
