# Document Search Engine with TF-IDF Ranking

This project implements a document search engine with a graphical user interface (GUI) using Tkinter. The engine uses TF-IDF (Term Frequency-Inverse Document Frequency) for ranking the relevance of documents to a given query. The search engine preprocesses the text data, builds an inverted index, and retrieves and ranks documents based on the query input.

## Features

- **GUI**: Built using Tkinter, allowing users to input queries and view results in a scrollable text widget.
- **Text Preprocessing**: Tokenizes text, removes stopwords, and normalizes text.
- **Inverted Index**: Efficiently retrieves documents matching the query.
- **TF-IDF Ranking**: Ranks documents based on their relevance to the query using cosine similarity.
- **Extensibility**: Placeholder for additional ranking methods.

## Requirements

- Python 3.x
- Tkinter
- NLTK (Natural Language Toolkit)
- scikit-learn

## How It Works

1. **Text Preprocessing**: The input text is tokenized, converted to lowercase, and stopwords are removed.
2. **Building Inverted Index**: An inverted index is built to map terms to document names.
3. **Query Processing**: The query is preprocessed similarly to the documents.
4. **Document Retrieval**: The inverted index is used to find documents that contain the query terms.
5. **TF-IDF Ranking**: The retrieved documents are ranked based on TF-IDF and cosine similarity.

### TF-IDF and Cosine Similarity

**TF-IDF** (Term Frequency-Inverse Document Frequency) is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents (corpus). It is used to convert text data into numerical features that can be used for similarity measurement.

- **Term Frequency (TF)**: Measures how frequently a term occurs in a document.
- **Inverse Document Frequency (IDF)**: Measures how important a term is by comparing the term's frequency across all documents in the corpus.

The TF-IDF value for a term in a document is the product of its TF and IDF values.

**Cosine Similarity** is a measure of similarity between two non-zero vectors. It calculates the cosine of the angle between the vectors, which represents their orientation and not their magnitude. In the context of text documents, it is used to measure the similarity between the TF-IDF vectors of the query and the documents.

The cosine similarity is given by:

\[ \text{cosine similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|} \]

where:
- \( \mathbf{A} \) and \( \mathbf{B} \) are the TF-IDF vectors of the query and a document.
- \( \mathbf{A} \cdot \mathbf{B} \) is the dot product of the vectors.
- \( \|\mathbf{A}\| \) and \( \|\mathbf{B}\| \) are the magnitudes (norms) of the vectors.

By computing the cosine similarity between the query and each document, we obtain a score that indicates how similar each document is to the query. The documents are then ranked based on these scores.

## GUI Components

- **Query Entry**: A scrollable text widget for users to enter their search queries.
- **Search Button**: Initiates the document retrieval process.
- **Rank Button**: Ranks the retrieved documents using TF-IDF.
- **Result Display**: A scrollable text widget to display the matched and ranked documents.

## Usage

1. Enter a search query in the text entry widget.
2. Click the "Search" button to find matching documents.
3. Click the "Rank Documents (TF-IDF)" button to rank the matched documents based on their relevance to the query.

## Example Documents

The project includes example text files:
- AI1.txt, AI2.txt, AI3.txt
- history1.txt, history2.txt, history3.txt
- sports1.txt, sports2.txt, sports3.txt

These files are used to build the initial inverted index and can be replaced or expanded with additional text files.

## Setup

1. Clone the repository.
2. Ensure you have the required libraries installed:
   ```bash
   pip install nltk scikit-learn
