import streamlit as st
def machine_guess():
    # Initializing variables
    if 'high' not in st.session_state:
        st.session_state.high = 100
    if 'low' not in st.session_state:
        st.session_state.low = 0
    if 'guess' not in st.session_state:
        st.session_state.guess = 0
    if 'start' not in st.session_state:
        st.session_state.start = 0
    if 'playing' not in st.session_state:
        st.session_state.playing = False
    if 'attempts' not in st.session_state:
        st.session_state.attempts=1

    # Create a placeholder to update the guessing output on a single line
    output_placeholder = st.empty()

    # Functions
    def guessmaker():
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        output_placeholder.write(f"Is your number {st.session_state.guess}?")

    def change(inp):
        if inp == 'Yes':
            output_placeholder.success("I won!")
            st.write("Number of attempts taken",st.session_state.attempts)
            st.session_state.start = 0
            st.session_state.playing = False
        elif inp == 'Greater':
            st.session_state.low = st.session_state.guess + 1
            guessmaker()
        elif inp == 'Lesser':
            st.session_state.high = st.session_state.guess - 1
            guessmaker()

    # Logic
    if st.session_state.start == 0:
        st.session_state.low = st.number_input("Enter low", step=1, min_value=0)
        st.session_state.high = st.number_input("Enter high", step=1, min_value=0)
        

        if st.session_state.low < st.session_state.high:
            st.session_state.start = 1
            st.session_state.playing = True
            st.write(f"Range: {st.session_state.low} to {st.session_state.high}")
        else:
            st.warning("Please ensure that the low value is less than the high value.")
    elif st.session_state.playing:
        guessmaker()
        c1, c2 = st.columns(2)
        inp = c2.selectbox("Choose", ['Yes', 'Greater', 'Lesser'])
        
        if st.button("Submit"):
            change(inp)
            st.session_state.attempts+=1

machine_guess()