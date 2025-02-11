import streamlit as st


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")



genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")



agree = st.checkbox("Do you Love Bijaiya?")

if agree:
    st.write("Every Body loves Bijaiya!")



def square(x):
    return x * x

x = st.number_input("Enter a number")

if st.button("Square"):
    st.write(f"{x} squared is {square(x)}")


if (st.button("calculate aquare")):
    result = square(x)
    st.text(result)

