import streamlit as st
import numpy as np
import json

# Define matrix size (e.g., 5x5)
rows, cols_count = 5, 5

# Initialize session state to hold matrix state
if "matrix" not in st.session_state:
    st.session_state.matrix = np.zeros((rows, cols_count), dtype=int)

# Toggle button states
def toggle(row, col):
    st.session_state.matrix[row, col] = 1 - st.session_state.matrix[row, col]

# Display matrix with buttons
for row in range(rows):
    col_buttons = st.columns(cols_count)  # Renamed to col_buttons to avoid conflict
    for col in range(cols_count):
        label = f"{row},{col}"  # You can use a label or leave it blank
        toggled = st.session_state.matrix[row, col]
        if col_buttons[col].button(label):
            toggle(row, col)

# Save button to save the matrix state
if st.button("Save State"):
    with open("matrix_state.json", "w") as f:
        json.dump(st.session_state.matrix.tolist(), f)
    st.success("Matrix state saved!")
