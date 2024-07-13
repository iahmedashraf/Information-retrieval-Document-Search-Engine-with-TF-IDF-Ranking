import tkinter as tk
from tkinter import scrolledtext
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize Tkinter
root = tk.Tk()
root.title("Document Search Engine")
root.geometry("600x400")

# Function to preprocess text
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    return tokens

# Function to build inverted index
def build_inverted_index(doc_name, doc_content, inverted_index, terms):
    # Preprocess document content
    tokens = preprocess_text(doc_content)

    # Update terms set
    terms.update(tokens)

    # Update inverted index
    for token in tokens:
        if token not in inverted_index:
            inverted_index[token] = set()
        inverted_index[token].add(doc_name)

# Function to retrieve documents matching the query
def retrieve_documents(query, inverted_index):
    query_tokens = preprocess_text(query)
    retrieved_docs = set()

    for token in query_tokens:
        if token in inverted_index:
            retrieved_docs.update(inverted_index[token])

    return {doc_name: documents[doc_name] for doc_name in retrieved_docs}

# Function to rank documents based on the current ranking method
def rank_documents(query, matched_documents):
    global current_ranking_method

    if current_ranking_method == "TF-IDF":
        # Compute TF-IDF vector for the query
        tfidf_vectorizer = TfidfVectorizer()
        query_tfidf = tfidf_vectorizer.fit_transform([query])

        # Compute TF-IDF vectors for each matched document
        document_names = list(matched_documents.keys())
        document_contents = list(matched_documents.values())
        document_tfidf = tfidf_vectorizer.transform(document_contents)

        # Compute cosine similarity between query and each document
        similarity_scores = cosine_similarity(query_tfidf, document_tfidf).flatten()

        # Pair similarity scores with document names
        document_similarity = dict(zip(document_names, similarity_scores))

        # Sort documents by similarity score
        sorted_documents = sorted(document_similarity.items(), key=lambda x: x[1], reverse=True)

        return sorted_documents
    elif current_ranking_method == "Other":
        # Placeholder for other ranking method
        return []

# Function to perform search
def perform_search():
    query = query_entry.get("1.0", tk.END).strip()
    matched_documents = retrieve_documents(query, inverted_index)

    if matched_documents:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Matched Documents:\n")
        for doc_name in matched_documents.keys():
            result_text.insert(tk.END, f"{doc_name}\n")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "No matched documents found.")

# Function to perform ranking
def perform_ranking():
    query = query_entry.get("1.0", tk.END).strip()
    matched_documents = retrieve_documents(query, inverted_index)

    if matched_documents:
        ranked_documents = rank_documents(query, matched_documents)

        if ranked_documents:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "Ranked Relevant Documents (TF-IDF):\n")
            for rank, (doc_name, similarity_score) in enumerate(ranked_documents, start=1):
                result_text.insert(tk.END, f"{rank}. {doc_name} - Similarity: {similarity_score}\n")
        else:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "No relevant documents found.")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "No matched documents found.")

# Create GUI components
query_label = tk.Label(root, text="Enter your query:")
query_label.pack(pady=5)

query_entry = scrolledtext.ScrolledText(root, width=60, height=3)
query_entry.pack(pady=5)

# Create the search button
search_button = tk.Button(root, text="Search", command=perform_search)
search_button.pack(pady=5)

# Create the ranking button
rank_button = tk.Button(root, text="Rank Documents (TF-IDF)", command=perform_ranking)
rank_button.pack(pady=5)

result_label = tk.Label(root, text="Search Result:")
result_label.pack(pady=5)

result_text = scrolledtext.ScrolledText(root, width=60, height=10)
result_text.pack(pady=5)

# Define the names of text files
txt_file_names = [
    "AI1.txt", "AI2.txt", "AI3.txt",
    "history1.txt", "history2.txt", "history3.txt",
    "sports1.txt", "sports2.txt", "sports3.txt"
]

# Initialize inverted index and terms set
inverted_index = {}
terms = set()

# Read each text file and process its content
documents = {}
for file_name in txt_file_names:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            documents[file_name] = content
            build_inverted_index(file_name, content, inverted_index, terms)
    except Exception as e:
        print(f"Error reading '{file_name}': {e}")

if not inverted_index:
    print("No documents found.")

# Initialize current_ranking_method variable
current_ranking_method = "TF-IDF"

root.mainloop()
