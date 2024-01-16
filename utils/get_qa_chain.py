# importing libraries
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate

class QAChain:
    """
    A class that represents a chain of question answers chain
    """
    def get_qa_chain(vectorstore, num_chunks: int):
        """
        :param vectorstore:This takes a vector store
        :param num_chunks: Number of chunks
        :return: Return Question Answer Chain
        """

        # Defining Template Prompt of LLM
        prompt_template = """
        **Task:** Extract a precise answer from the given context and question.
        
        **Strict Instructions:**
        - Answer only based on the provided context.
        - If the answer is not found in the context, respond with "N/A."
        - Avoid making assumptions or guesses.
        - Refrain from generating creative text formats, like poems, code, scripts, musical pieces, email, letters, etc.
        - Adhere to a factual and informative style.
        - Maintain a respectful and professional tone.
        - Avoid disclosing private information or expressing personal opinions or beliefs.
        - Stick to the task at hand and avoid going off-topic or engaging in unrelated conversations.
        Context: {context}
        Question: {question}"""

        # Define PromptTemplate class instance

        prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"], validate_template=False)
        chain_type_kwargs = {"prompt": prompt}

        qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model="gpt-3.5-turbo-16k"), chain_type="stuff",
                                         retriever=vectorstore.as_retriever(search_type="similarity",
                                                                            search_kwargs={"k": num_chunks}),
                                         chain_type_kwargs=chain_type_kwargs, return_source_documents=True)

        return qa
