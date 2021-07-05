import streamlit as st
from PIL import Image


def display_body():
    setup_other_components()
    st.write('# Welcome to quantumcat!')
    st.write('A high-level cross-platform open-source '
             'quantum computing python library so that the quantum community could concentrate on '
             'building quantum applications without much effort.')
    """
    [![GitHub forks](https://img.shields.io/github/forks/artificial-brain/quantumcat.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/artificial-brain/quantumcat/)
    """

    st.write('### Okay! But what does it means?')

    st.write('It means that you don\'t have to go through ton of mathematics like below to work on quantum computing.')

    st.image(Image.open('assets/quantum-maths.jpeg'), width=500)

    st.write('It also means that you don\'t have to code anymore in below low-level language '
             'such as gates and circuits.')

    st.image(Image.open('assets/quantum-circuit.png'), caption='Grover\'s Algorithm for solving Sudoku problem',
             width=700)

    st.write('### Ah Okay! But what if I am a researcher Or If I am okay to code in low-level'
             ' language, What does quantumcat has to offer me?')

    st.write('quantumcat is a cross-platform library and is built on the principle of write once and execute anywhere. '
             'You just have to follow one syntax and could run your circuit in one of the supported platforms '
             'such as Google Cirq, IBM Qiskit or Amazon Braket (Few others are in progress)'
             ' without the need to write code in multiple syntax.')

    st.write("### Let's consider an example of generating a random number based on quantum superposition")

    st.write('### Qiskit')

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

    st.write('### quantumcat')

    st.markdown("""
            ```
            result = RandomNumber(length=4, output_type=DECIMAL).execute(provider=providers.IBM_PROVIDER)
            # The above code would execute on IBM simulator
            ```
        """)

    st.write('### To execute on other platforms, Just change the provider value to Google or Amazon')

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

    st.write('Absolutely! It is an open source library published under Apache-2.0 License.')

    github_html = """
    <a href="https://github.com/artificial-brain/quantumcat/" target="_blank" rel="noopener noreferrer">
    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="50" height="50"/>
    </a>
    """

    st.markdown(github_html, unsafe_allow_html=True)


    st.write("## quantumcat API")
    st.write('We have also exposed few functionalities as an API so that you could '
             'consume it in any classical application without the need to write quantum code. ')

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

    st.write('* Please note that API is limited to 100 hits per day per IP address. '
             'For more usage kindly send us an email to entangled@artificialbrain.us')
    st.write("## Demo of Applications")
    col1, col2 = st.beta_columns(2)

    col1.subheader('QuantumWheel')
    col1.write('Let Nature help you to make a quick decision based on the principle '
               'of Quantum Superposition!')
    col1.image(Image.open('assets/quantumwheel-screenshot2.jpeg'))
    play_store_link = '[Download App](https://play.google.com/store/apps/details?id=com.artificial.brain.quantumwheel)'

    col1.markdown(play_store_link, unsafe_allow_html=True)

    col2.subheader('Reinforcement Learning Example')
    col2.write('Teaching a computer to play Snake with Reinforcement Learning where '
               'random actions are generated by quantum property such as superposition '
               'using quantumcat.')
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

    st.sidebar.markdown('__How to install__')
    st.sidebar.code('$ pip install quantumcat')


if __name__ == '__main__':
    display_body()

