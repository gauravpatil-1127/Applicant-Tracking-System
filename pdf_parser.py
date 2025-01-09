from langchain_community.document_loaders import PyMuPDFLoader

def pdf_parser(file_path):
    # Initialize the loader with the path to your PDF file
    loader = PyMuPDFLoader(file_path)

    # Load the documents from the PDF
    documents = loader.load()

    # Print the loaded documents
    return documents[0].page_content
    