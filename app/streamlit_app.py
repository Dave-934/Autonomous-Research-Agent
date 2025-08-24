# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import streamlit as st
# from src.agent import run_research_pipeline

# st.set_page_config(page_title="Autonomous Research Agent", page_icon="🤖", layout="wide")

# st.title("🤖 Autonomous Research Agent")
# st.write("Ask me a question and I’ll generate a structured research report with sources.")

# query = st.text_input("Enter your research topic/question:")

# if st.button("Run Research"):
#     if not query.strip():
#         st.warning("⚠️ Please enter a valid research question.")
#     else:
#         with st.spinner("🔎 Researching..."):
#             report = run_research_pipeline(query)

#         st.success("✅ Research complete! PDF saved as `research_report.pdf`")

#         # Show formatted preview
#         st.subheader("📄 Report Preview")
#         st.markdown(report)

#         # Download PDF
#         filename = "research_report.pdf"
#         if os.path.exists(filename):
#             with open(filename, "rb") as f:
#                 st.download_button(
#                     label="📥 Download PDF Report",
#                     data=f,
#                     file_name=filename,
#                     mime="application/pdf"
#                 )













# import sys
# import os
# import time
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import streamlit as st
# from src.agent import run_research_pipeline


# st.set_page_config(page_title="Autonomous Research Agent", page_icon="🤖", layout="wide")


# st.title("🤖 Autonomous Research Agent")
# st.write("Ask me a question. The agent remembers your previous questions for multi-turn research.")


# # Initialize conversation history list in session state once
# if "conversation_history" not in st.session_state:
#     st.session_state.conversation_history = []


# query = st.text_input("Enter your research topic/question:")


# def typewriter_effect(text: str, speed: float = 0.004):
#     container = st.empty()
#     for i in range(1, len(text) + 1):
#         container.markdown(text[:i])
#         time.sleep(speed)


# if st.button("Generate Report"):
#     if not query.strip():
#         st.warning("⚠️ Please enter a valid research question.")
#     else:
#         with st.spinner("🔎 Researching..."):
#             result = run_research_pipeline(query, st.session_state.conversation_history)

#         if "error" in result:
#             st.error(f"Error: {result['error']}")
#         else:
#             st.success("✅ Research complete! PDF saved as `research_report.pdf`")

#             # Show formatted summary with typewriter effect
#             st.subheader("📄 Report Preview")
#             typewriter_effect(result.get("summary", "No summary generated."))

#             # Update conversation history for next turn
#             st.session_state.conversation_history = result["conversation_history"]


# if st.button("Clear Conversation History"):
#     st.session_state.conversation_history = []
#     st.success("Conversation history cleared. You can start fresh.")


# # Download PDF file section
# filename = "research_report.pdf"
# if os.path.exists(filename):
#     with open(filename, "rb") as f:
#         st.download_button(
#             label="📥 Download PDF Report",
#             data=f,
#             file_name=filename,
#             mime="application/pdf"
#         )


































import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.agent import run_research_pipeline

st.set_page_config(page_title="Autonomous Research Agent", page_icon="🤖", layout="wide")

st.title("🤖 Autonomous Research Agent")
st.write("Ask me a question. The agent remembers your previous questions for multi-turn research.")

# Initialize conversation history list in session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

def typewriter_effect(text: str, speed: float = 0.004):
    container = st.empty()  # create an empty placeholder to update inside chat_message
    for i in range(1, len(text) + 1):
        container.markdown(text[:i])
        time.sleep(speed)

# Display entire conversation so far with chat bubbles
for turn in st.session_state.conversation_history:
    with st.chat_message("user" if turn["role"] == "user" else "assistant"):
        st.markdown(turn["content"])

# Accept user input
if prompt := st.chat_input("Enter your research topic/question:"):

    # Display user message in chat message container and save to history
    st.session_state.conversation_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run research pipeline with current conversation history for multi-turn context
    with st.spinner("🔎 Researching..."):
        result = run_research_pipeline(prompt, st.session_state.conversation_history)

    # Handle errors
    if "error" in result:
        st.error(f"Error: {result['error']}")
    else:
        # Assistant message container with typewriter effect inside
        with st.chat_message("assistant"):
            typewriter_effect(result.get("summary", "No summary generated."))

        # Append assistant's reply to conversation history
        st.session_state.conversation_history.append({"role": "assistant", "content": result.get("summary", "")})

    # Download PDF button below chat input
    filename = "research_report.pdf"
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            st.download_button(
                label="📥 Download PDF Report",
                data=f,
                file_name=filename,
                mime="application/pdf"
            )

# Button to clear history if desired
if st.button("Clear Conversation History"):
    st.session_state.conversation_history = []
    st.success("Conversation history cleared. You can start fresh.")
