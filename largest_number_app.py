import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")
    
    st.write("Enter three numbers:")
    a = st.number_input("First number", value=0)
    b = st.number_input("Second number", value=0)
    c = st.number_input("Third number", value=0)
    
    if st.button("Find Largest"):
        largest = find_largest(a, b, c)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
