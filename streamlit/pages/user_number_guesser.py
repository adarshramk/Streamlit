#User number guesser

import streamlit as st

def user_guess():
    import random as ran
    if 'guess' not in st.session_state:
        st.session_state.guess=0
    if 'tries' not in st.session_state:
        st.session_state.tries=1
    if 'num' not in st.session_state:
        st.session_state.num=ran.randint(0,20)


    check=0
    st.title('User number guessing game')
    attempts=st.number_input("Enter maximum number of tries",step=1)

        
    st.write("Make your guess between 0 and 20")
    if st.session_state.tries<attempts and check==0:
        st.write(st.session_state.tries,attempts)
        st.session_state.guess=st.number_input("Enter your guess",step=1)
        if st.button("Submit"):
            if st.session_state.guess==st.session_state.num:
                st.success("Ok you won")
                check=1
            else:
                st.write("Nah....Try again")
                st.session_state.tries+=1


    elif st.session_state.tries==attempts or check==1:
        st.success("Yay I Won!!!")

user_guess()
