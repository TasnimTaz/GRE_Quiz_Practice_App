import streamlit as st
import time
from api_calling import generate_quiz

st.set_page_config(layout="wide")
st.title("AI-Powered GRE Practice System Using Large Language Models",anchor=False)
st.markdown("AI-powered GRE practice system that dynamically generates questions, evaluates your answers, and tracks performance over time.")
st.divider()
    
with st.sidebar:
    st.header("Settings")
    
    sub = st.selectbox("Select Subject",
                 options=["English","Math","Mixed"],
                 index=None,placeholder="subjects"
                 )
    
    dif = st.selectbox("Choose Difficulty level",
                 options=["Easy","Medium","Hard"],
                 index=None,placeholder="difficulties"
                 )
    
    button = st.button("Attempt Quizzes",type="primary")
    

if button:
    has_error = False
    if not sub:
        st.error("Select any Subject")
        has_error = True
    if not dif:
        st.error("Choose any difficulty level")
        has_error = True
    
    if not has_error:
        with st.container(border=True):
            left, right = st.columns([3, 1])
            
            with left:
                with st.spinner("AI is generating your quizzes..."):    
                    st.subheader(f"Your {dif} level {sub} quiz is ready!")
                    questions = generate_quiz(sub,dif)
                    
                    with st.form("quiz_form"):
                        for q in questions:
                            st.markdown(f"**{q['id']}. {q['question']}**")

                            st.radio(
                                "Choose:",
                                options=list(q['options'].keys()),
                                format_func=lambda k: f"{k}. {q['options'][k]}",
                                key=f"q_{q['id']}",
                                index=None
                            )
                        
                        st.write("\n")
                        submitted_button= st.form_submit_button("Submit",type="primary")
                        
            with right:
                st.subheader("⏱ Time Left")

                ph = st.empty()
                N = 5 * 60 + 30

                for secs in range(N, 0, -1):
                    mm, ss = secs // 60, secs % 60

                    ph.markdown(
                        f"""
                        <div style="
                            background-color:#b0f5e9;
                            padding:10px;
                            border-radius:10px;
                            text-align:center;
                            font-size:22px;
                            font-weight:bold;
                            color:#012e26;
                        ">
                            {mm:02d}:{ss:02d}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    time.sleep(1)
                    