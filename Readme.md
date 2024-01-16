# PDF Chatbot

## Welcome to your new PDF Chatbot!

This chatbot is designed to help you effortlessly navigate and extract information from PDF documents.

### Explore PDFs Like Never Before

- **Ask questions naturally:** Just type your questions in plain language, and the chatbot will do its best to understand and provide helpful answers.
- **Get informative responses:** The chatbot will analyze the PDF content and deliver comprehensive answers that address your specific queries.


### Key Features

- **Upload any PDF:** Compatible with a wide range of PDF documents.
- **Natural language processing:** Understands your questions and provides relevant responses.


### Optional Features (Coming Soon!)

- **Key point summaries:** Get a quick overview of the document's main takeaways.
- **Translation capabilities:** Access PDF content in multiple languages.
- **Report generation:** Create customized reports or presentations based on the PDF's information.

### Technology Stack

- OpenAI
- Langchain
- Streamlit

### Getting Started

#### Prerequisites
- Python 3.10 or above
- *Following libraries are neccessary to run this chatbot*
  - lanchain,open,streamlit  


#### Installation
Open your terminal on your machine and run following commands
- **Clone the repository**

```bash
  git clone https://github.com/mrqadeer/Hackathon-Final-Round-Batch-1.git
```
- **Go to repository folder**
  ```
  cd Hackathon-Final-Round-Batch-1
  ```
- **Run Setup**
  ```
  python setup.py
  ```
- **Run the chatbot**
  ```
  streamlit run app.py
  ```


#### Usage
When app is running you have two choices
- **Upload files**
  - Browse files button will take you to your browse window to select and upload files.
  - This application copies uploaded files to ```data-files``` directory in your project.
- **Local zipped files**
- To avail this feature you must copy zipped files into project folder ```data-files```
- And on streamlit app press ```Process``` on right side



