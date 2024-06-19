import streamlit as st
from langchain_openai import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from pathlib import Path
import os


openai_api_key = os.getenv('OPENAI_API_KEY')


def main():

    # st.set_page_config(page_title="Ask your CSV")
    st.set_page_config(page_title="Ask your Data 📈", page_icon="📊")
    st.header("Ask your Data 📈")
    st.markdown("### Upload a CSV file and ask questions about it!")

    csv_file = st.file_uploader("Upload a CSV file", type="csv", help="Only .csv files are supported.")
    if csv_file is not None:
        save_folder = r'code\uploaded_files'
        save_path = Path(save_folder, csv_file.name)
        with open(save_path, mode='wb') as w:
            w.write(csv_file.getvalue())

        str_path = str(save_path)
        agent = create_csv_agent(
            OpenAI(temperature=0.2, api_key=openai_api_key, model='gpt-3.5-turbo-instruct'), 
            str_path, verbose=True, allow_dangerous_code=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                response = agent.run(user_question)

                st.write(response)




    st.markdown("---")


if __name__ == "__main__":
    main()