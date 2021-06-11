import streamlit as st


def print_hi():
    st.write('## Welcome to quantumcat!')
    st.write('A high-level cross-platform open-source '
             'quantum computing library so that the quantum community could concentrate on '
             'building quantum applications without much effort.')
    """
    [![GitHub forks](https://img.shields.io/github/forks/artificial-brain/quantumcat.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/artificial-brain/quantumcat/)
    """

    st.write("### Comparison of generating a random number")

    st.write('#### Qiskit')

    st.markdown("""
    ```
    from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ
    from qiskit.tools.monitor import job_monitor
        
    IBMQ.enable_account('ENTER API TOKEN HERE')
    provider = IBMQ.get_provider(hub='ibm-q')
        
    q = QuantumRegister(16,'q')
    c = ClassicalRegister(16,'c')
    circuit = QuantumCircuit(q,c)
    circuit.h(q) # Applies hadamard gate to all qubits
    circuit.measure(q,c) # Measures all qubits 
        
    backend = provider.get_backend('ibmq_qasm_simulator')
    result = execute(circuit, backend, shots=1)
    ```
""")

    st.write('#### quantumcat')

    st.markdown("""
        ```
        from quantumcat.applications.generator import RandomNumber
        
        result = RandomNumber(length=4, output_type=DECIMAL).execute(api='YOUR API KEY', device='IBM DEVICE NAME')
        # The above code would execute on IBM
        ```
    """)

    st.write('#### To execute on any platform, Just add providers paramater to execute()')

    st.markdown("""
            ```
            from quantumcat.applications.generator import RandomNumber
            from quantumcat.utils import providers

            result = RandomNumber(length=4, output_type=DECIMAL).execute(providers=providers.GOOGLE_PROVIDER)
            # The above code would execute on Google
            
            result = RandomNumber(length=4, output_type=DECIMAL).execute(providers=providers.AMAZON_PROVIDER)
            # The above code would execute on Amazon
            ```
        """)

    col1, col2 = st.beta_columns(2)
    col1.subheader('Reinforcement Learning Example')
    col2.subheader('Monty Hall problem')


if __name__ == '__main__':
    print_hi()

