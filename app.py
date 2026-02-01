import streamlit as st
import pymysql as sql
import pandas as pd
db=sql.connect(host="localhost",user="root",password="Yoge@2006",database="DSA")
smt=db.cursor()
st.markdown("""
<style>
.redalign{
    text-align: center;
    color: red;
    font-style: italic;
}
</style>

<h2 class="redalign">DSA Portal</h2>
""", unsafe_allow_html=True)
st.sidebar.title("Welcome user")
if "page" not in st.session_state:
    st.session_state.page = "login"
if st.session_state.page == "login":
    st.title("Login Page")
    tab1=st.tabs(["Login"])
    with tab1[0]:
        uid=st.text_input("Enter User ID")
        upas=st.text_input("Enter Password",type="password")
        if(st.button("Login")):
            q=f"select *from student where student_id={uid} and password='{upas}'"
            smt.execute(q)
            result=smt.fetchall()
            if(result):
               st.success("Login Successful")
               st.balloons()
               st.session_state.page = "dashboard"
               st.session_state.uid = uid


            else:
             st.error("Invalid User ID or Password")
elif st.session_state.page == "dashboard":
    st.title("Welcome user",st.session_state.uid)
    st.markdown("""
         <h2 style="text-align: center; color: green; font-style: italic;">You can check your marks</h2>
                """,unsafe_allow_html=True)
    option = st.selectbox("select option",
["View Quiz1","view quiz2","view midterm","view Active Marks","view IV","View PE"])

    if option == "View Quiz1":
       q = f"select quiz1 from marks where student_id = {st.session_state.uid}"
       smt.execute(q)
       result = smt.fetchall()
       df = pd.DataFrame(result, columns=["Quiz1 Marks"])
       st.dataframe(df)
    elif option =="view quiz2":
        q = f"select quiz2 from marks where student_id = {st.session_state.uid}"
        smt.execute(q)
        result = smt.fetchall()
        df = pd.DataFrame(result, columns=["Quiz2 Marks"])
        st.dataframe(df)
    elif option =="view midterm":
        q = f"select midterm from marks where student_id = {st.session_state.uid}"
        smt.execute(q)
        result = smt.fetchone()
        df = pd.DataFrame([result], columns=["Midterm Marks"])
        st.dataframe(df)
    elif option =="view Active Marks":
        q = f"select AM from marks where student_id = {st.session_state.uid}"
        smt.execute(q)
        result = smt.fetchone()
        df = pd.DataFrame([result], columns=["Active Marks"])
        st.dataframe(df)
    elif option =="view IV":
        q = f"select IV from marks where student_id = {st.session_state.uid}"
        smt.execute(q)
        result = smt.fetchone()
        df = pd.DataFrame([result], columns=["IV Marks"])
        st.dataframe(df)
    elif option =="View PE":
        q = f"select PE from marks where student_id = {st.session_state.uid}"
        smt.execute(q)
        result = smt.fetchone()
        df = pd.DataFrame([result], columns=["PE Marks"])
        st.dataframe(df)
    st.write("you can check your attendance here")
    option=st.selectbox("select option",["select component","View Attendance"])
    if option=="View Attendance":
        q = f"""
SELECT student.student_name,
       attendance.total_present,
       attendance.total_absent,
       attendance.total
FROM attendance
JOIN student ON attendance.student_id = student.student_id
WHERE student.student_id = {st.session_state.uid}
"""

        smt.execute(q)
        result = smt.fetchall()
        df=pd.DataFrame(result,columns=["Student Name","Total_present","Total_absent","Total"])
        st.dataframe(df)