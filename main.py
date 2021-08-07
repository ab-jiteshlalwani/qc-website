import streamlit as st
from PIL import Image


def display_body():
    setup_other_components()
    st.write('# Welcome to quantumcat!')
    st.write('quantumcat is a platform-independent, open-source, high-level '
             'quantum computing library, which allows the quantum community to focus '
             'on developing platform-independent quantum applications without much effort.')
    """
    [![GitHub forks](https://img.shields.io/github/forks/artificial-brain/quantumcat.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/artificial-brain/quantumcat/)
    """

    st.write('### It is based on two principles:')
    st.write('1) Write once and execute on any supported quantum provider using one syntax.')
    st.write('2) quantumcat should enable researchers and developers to create quantum applications '
             'using high-level programming in the future so that they can focus on developing quantum '
             'applications instead of learning low-level concepts such as gates and circuits.')

    st.write("### Let's consider an example of generating a random number based on quantum superposition.")

    st.write('#### IBM Qiskit')

    st.markdown("""
    ```      
    q = QuantumRegister(16,'q')
    c = ClassicalRegister(16,'c')
    circuit = QuantumCircuit(q,c)
    circuit.h(q) # Applies hadamard gate to all qubits
    circuit.measure(q,c) # Measures all qubits 
    
    # Use Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')
    
    # Execute the circuit on the qasm simulator
    result = execute(circuit, simulator, shots=1).result()
    
    counts = result.get_counts()   
    ```
""")

    st.write('#### quantumcat')

    st.markdown("""
            ```
            result = RandomNumber(length=4, output_type=DECIMAL).execute(provider=providers.IBM_PROVIDER)
            # The above code would execute on IBM simulator
            ```
        """)

    st.write('To execute on other platforms, Just change the provider value to Google or Amazon')

    st.markdown("""
                ```
                result = RandomNumber(length=4, output_type=DECIMAL).execute(provider=providers.GOOGLE_PROVIDER)
                # The above code would execute on Google Cirq simulator

                result = RandomNumber(length=4, output_type=DECIMAL).execute(provider=providers.AMAZON_PROVIDER)
                # The above code would execute on Amazon Braket simulator
                ```
            """)

    st.write('### To execute on actual IBM quantum device')

    st.markdown("""
         ```
         from quantumcat.applications.generator import RandomNumber
         from quantumcat.utils import providers

         result = RandomNumber(length=4, output_type=DECIMAL).execute(provider=providers.GOOGLE_PROVIDER, 
         api='API KEY from IBM Quantum dashboard', device='IBM DEVICE NAME such as ibmq_manila or ibmq_quito')
         # The above code would execute on actual IBM quantum device
         ```
     """)

    st.write('### Is it free?')

    st.write('Yes, absolutely! The library is open source and licensed under Apache-2.0.')

    github_html = """
    <a href="https://github.com/artificial-brain/quantumcat/" target="_blank" rel="noopener noreferrer">
    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="50" height="50"/>
    </a>
    """

    st.markdown(github_html, unsafe_allow_html=True)


    st.write("## quantumcat APIs")
    st.write('We also exposed several of our functionalities as APIs, so that '
             'users can also integrate them into classical applications without '
             'writing the quantum code. ')

    st.write("### Random Number")
    st.markdown("""
        ```
        # POST Request
        https://api.quantumcat.io/generateRandomNumber
        # JSON Body to run on simulator
        {
          "length": 3,
          "provider": "GOOGLE / IBM / AMAZON"
        }
        # JSON Body to run on actual IBM device
        {
          "length": 3,
          "provider": "IBM",
          "api": "API KEY from IBM Quantum dashboard",
          "device": "IBM DEVICE NAME such as ibmq_manila or ibmq_quito"
        }
        ```
    """)

    st.write("### Password")
    st.markdown("""
           ```
           # POST Request
           https://api.quantumcat.io/generatePassword
           # JSON Body
           {
             "length": 8
           }
           # Length should be between 5 - 20
           # Password is generated in hexadecimal format using QRNG@ANU JSON API
           ```
       """)

    st.write("### OTP")
    st.markdown("""
               ```
               # POST Request
               https://api.quantumcat.io/generateOTP
               # 5 digits OTP is generated using QRNG@ANU JSON API
               ```
           """)

    st.write('*There is a daily limit of 100 API hits per IP address. '
             'For more information, contact us at entangled@artificialbrain.us')
    st.write("## Demo of Applications")
    col1, col2 = st.beta_columns(2)

    col1.subheader('QuantumWheel')
    col1.write('Let Nature help you to make a quick decision based on the principle '
               'of Quantum Superposition!')
    col1.image(Image.open('assets/quantumwheel-screenshot2.jpeg'))
    play_store_link = '[Download App](https://play.google.com/store/apps/details?id=com.artificial.brain.quantumwheel)'

    col1.markdown(play_store_link, unsafe_allow_html=True)

    col2.subheader('Reinforcement Learning Example')
    col2.write('Using quantumcat, an algorithm can be trained to play Snake with random actions'
               ' generated by quantum properties such as superposition.')
    video_file = open('assets/trained_snake.mp4', 'rb')
    video_bytes = video_file.read()
    col2.video(video_bytes)

    snake_demo_url = '[Snake AI Demo](https://quantumcat.io/snakedemo)'
    col2.markdown(snake_demo_url, unsafe_allow_html=True)

    footer_style = """
    <p style="margin-top: 2em;">Developed by Artificial Brain LLC</p>
    """
    # st.markdown(footer_style, unsafe_allow_html=True)



    # col2.subheader('Monty Hall problem (Coming Soon)')
    # col2.write('Placing randomly prize behind one of the 4 doors where the door is '
    #            'selected randomly using quantum property such as superposition '
    #            'using quantumcat.')
    # video_file = open('assets/trained_snake.mp4', 'rb')
    # original = Image.open('assets/monty-hall-problem.png')
    # col2.image(original, use_column_width=True)



def setup_other_components():
    quantumcat_logo_url = "https://raw.githubusercontent.com/artificial-brain/quantumcat/" \
                     "assets/quantumcat/logo/quantum_cat_logo.jpg"

    # Set page title and favicon.
    st.set_page_config(
        page_title="quantumcat", page_icon=quantumcat_logo_url,
    )

    hide_streamlit_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}   
            footer:after {
                content:'Developed by Artificial Brian LLC'; 
                visibility: visible;
                display: block;
                position: relative;
                padding: 5px;
                top: 2px;
                font-size: 20px;
                font-weight: 500;
                color: rgb(38, 39, 48);
                font-family: "IBM Plex Sans", sans-serif;
            }                   
            </style>
       """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.sidebar.markdown('__Installation__')
    st.sidebar.code('$ pip install quantumcat')


if __name__ == '__main__':
    display_body()

