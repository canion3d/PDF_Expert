from dotenv import load_dotenv
import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os
import gpt4all
import os
import streamlit_elements
from streamlit_elements import elements, mui, html

#All testing steps and process directions written by Michele Le, Ayoub El Bzioui, and Ty Canion of RBI GMbH#

from streamlit_option_menu import option_menu

LoginImage = st.image('jrcm_logo_002.jpg', use_column_width=1)
LoginText = st.markdown("<h1 style='text-align: center; color: black;'>PDFExpert!</h1>", unsafe_allow_html=True)
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

st.image("C:\\Users\\Tyrone.Canion\\Desktop\\Projects\\RBI_App\\pdf.jpg, use_column_width=1")

def Academy(st):
    if check_password() == True:
        add_indentation()
        hide_pages(["TCU_Testing", "SDS"])
        #global st # declare st as a global variable
        import streamlit as st
        LoginImage.empty()
        LoginText.empty()

        show_ul_style = """
        <style>
            ul { display: block !important; }
        </style>
        """
        # Call the markdown method to display the CSS style
        st.markdown(show_ul_style, unsafe_allow_html=True)

        # 1. horizontal menu

        selected = option_menu(None, ["Home", "Customers", "Management", "Tooling", "Incident Management", "RBI Academy", "Rexx Portal"],
            icons=['house', 'cloud-upload', 'menu-app', 'menu-app','menu-app', 'file-spreadsheet'],
            menu_icon="cast", default_index=0, orientation="horizontal",styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "15px"},
                "nav-link": {"font-size": "12px", "text-align": "left", "margin":"10px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "red"},
            }
        )

       # if "Home" == selected: os.startfile("C:\\Users\\Tyrone.Canion\\Desktop\\Projects\\RBI_App\\home.py")

        #if "Customers" == selected: open("C:\\Users\\Tyrone.Canion\\Desktop\\Projects\\RBI_App\\pages\\Customers.py")

        if selected ==  "Management" : os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Diagnostic Tool Set 8.16\DTS Monaco.lnk")

        if selected == "Tooling": os.startfile("C:\\Users\\Tyrone.Canion\\AppData\\Local\\Postman\\app-9.31.0\\postman.exe")

        if selected ==  "Incident Management" : os.startfile("https://gsep.daimler.com/jira/secure/RapidBoard"
                                                                         ".jspa?rapidView=75097&projectKey=TCUSQ&selectedIssue=TCUSQ-85")

        if selected == "Rexx Portal" : os.startfile("https://rbi-online.rexx-systems.com/login.php?goto=%2Fportal%2Frx%2F%3FtargetRealm%3Dportal%26menu%3D1%26script%3Dmy_workday%2Fmy_workday.php")

        st.write("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto');
        html, body, [class*="css"]  {
           font-family: 'Roboto'
        }
        </style>
        """, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Welcome to PDFExpert!", "How to use PDFExpert", "Use PDFExpert Now!"])

with tab1:
   st.header("Welcome to PDFExpert!")
   #st.image("pages/pdf.jpg", width=200)
   st.markdown("# Why should I use PDFExpert?")

   st.markdown("## Here are some use cases to get the most out of PDFExpert:")

   st.markdown("1. Educational Material: Students can ask questions about specific concepts, equations, or examples in their PDF textbooks or lecture notes.Teachers can create interactive PDFs with embedded questions for students to test their understanding and receive immediate feedback.")

   st.markdown("2. Legal Documents:Lawyers or legal professionals can ask questions about specific sections, clauses, or legal terms in legal contracts, agreements, or court filings. Individuals seeking legal advice can ask questions about their rights, responsibilities, or implications of certain clauses in legal documents.")

   st.markdown("3. Research Papers:Researchers can ask questions about specific research methodologies, findings, or conclusions in academic papers. Students or professionals can seek clarification on complex concepts, data analysis methods, or experimental procedures mentioned in scientific papers. ")

   st.markdown("4. Technical Documentation:Developers or engineers can ask questions about APIs, code snippets, or configuration details mentioned in technical documentation. Users of a software or hardware product can seek assistance by asking questions about installation procedures, troubleshooting steps, or advanced settings in the user manuals. ")

   st.markdown("5. Business Reports: Business analysts can ask questions about key metrics, trends, or insights mentioned in financial reports, market research studies, or sales analyses. Executives can ask questions about specific sections or recommendations in strategic business plans or industry forecasts.")

   st.markdown("6. Government Documents: Citizens can ask questions about policies, regulations, or eligibility criteria mentioned in government publications such as tax forms, application forms, or citizen guides. Researchers or journalists can seek information or clarification on government reports, public inquiries, or white papers.")

   st.markdown("7. Personal Documents: Individuals can ask questions about specific information in their personal documents, such as resumes, CVs, or personal statements. Users can seek guidance on filling out application forms, visa documents, or insurance claims.")

   st.markdown("And many more use cases!")

   st.markdown("Go ahead and type your question in the provided text field and tap on the **Submit** or **Ask** button!")

with tab2:
   #st.header("How to use Ask A .PDF")
   #st.image(".pdf.jpg", width=200)
   st.markdown("# How to use PDFExpert")

   st.markdown("## Uploading a .PDF File:")
   st.markdown("1. Launch the Ask A .PDF app.")
   st.markdown("2. On the main screen, you will find an option to upload a .PDF file.")
   st.markdown("3. Tap on the **Upload** button and browse your device's storage to locate the desired .PDF file.")
   st.markdown("4. Select the file you wish to extract information from and confirm the upload.")

   st.markdown("## Extracting Answers:")
   st.markdown(
       "1. After uploading the .PDF file, the app will start processing the document to extract relevant information.")
   st.markdown(
       "2. Once the processing is complete, you will be presented with a user interface where you can input questions.")
   st.markdown("3. Formulate your question based on the content of the .PDF file you uploaded.")
   st.markdown("4. Type your question in the provided text field and tap on the **Submit** or **Ask** button.")

   st.markdown("## Receiving Answers:")
   st.markdown(
       "1. The app will use OpenAI technology to analyze the content of the .PDF file and generate relevant answers to your question.")
   st.markdown("2. After a brief processing time, the app will display the answer on your screen.")
   st.markdown("3. Read the provided answer to gain insights and information from the .PDF file.")

with tab3:
   st.header("PDFExpert!")
   #st.image("pages/pdf.jpg", width=200)#

import streamlit as st
import time

progress_text = st.empty()
my_bar = st.progress(0)

progress_text.markdown("**Just a moment while we prepare the environment!**")

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

progress_text.markdown("**The environment is ready!**")

def main():
    load_dotenv()
    print(os.getenv("OPENAI_API_KEY"))
    st.header("Have a questions for any .pdf document, we've got the answer! 💬")

    # upload file
    pdf = st.file_uploader("Upload your PDF now to get quick answers for any PDF document!", type=".pdf")

    # extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        from pydantic import BaseModel
        from typing import List
        from langchain.embeddings.openai import OpenAIEmbeddings

        class Input(BaseModel):
            text: str

        def generate_embeddings(inputs: List[Input]):
            embeddings = OpenAIEmbeddings(OPENAI_API_KEY=OPENAI_API_KEY)

        # Call your function with the necessary inputs

        # create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # show user input
        user_question = st.text_input("Ask a question about your PDF:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)
                print(cb)

            st.write(response)

    # Display a message if no PDF file is uploaded
        #else: st.error("No PDF file is loaded. Please upload a PDF file.")

if __name__ == '__main__':
    main()


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
               <style>
               #MainMenu {visibility: hidden;}
               footer {visibility: hidden;}
               header {visibility: hidden;}
               </style>
               """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.balloons()