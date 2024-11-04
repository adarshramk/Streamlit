import streamlit as st
st.title("Portfolio")

st.write("\n")
st.write('''I'm Adarsh Ram.K, currently pursuing my B.Tech in IT. Coding has always 
         been a passion of mine—I love solving problems and finding creative ways to make technology work for people.
          My ultimate goal is to become a data scientist, so I'm focused on building my skills in data analytics, 
         machine learning, and everything else I need to succeed in this field.
          I'm excited about the journey ahead and eager to make a real impact through data science.''')
st.write("\n")
st.write("Brief Introduction")
c1,c2=st.columns(2)
l1=["Name","Department","College",""]
l2=["Adarsh Ram . K","Information Technology","Kgisl Institute of Technology"]
for i in range(3):
    c1.write(l1[i])
    c2.write(l2[i])


st.write("\n")
st.write("Choose a game to play:")
st.write("\n")
c1.link_button("Machine Number Guesser","/machine_number_guesser")
c2.link_button("User Number Guesser","/user_number_guesser")
