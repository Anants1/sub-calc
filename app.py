from operator import sub
import streamlit as st

def sub(a, b):
  return a - b

def main():
    st.title("Simple Calculator")
    st.write("This is a simple calculator app")

    a = st.number_input("Enter a number")

    b = st.number_input("Enter another number")

    operation = st.selectbox("Select Operation", ["Subtract"])

    if operation == "Subtract":
        st.write("The answer is ",sub(a, b))


if __name__ == '__main__':
    main()



    








