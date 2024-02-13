# Document Clustering 

## Overview
This project aims to develop a system that clusters documents, categorizing them into distinct clusters based on their content. This aids in the exploration and organization of diverse text information, thereby uncovering any pattern or insight within the document set. A stepwise methodology has been adopted to achieve this.

## Features
1.	**Data Preparation:** This first step involves importing a dataset composed of a variety of documents into a DataFrame. The documents span multiple areas such as sports, health, and business. Each document within the DataFrame represents textual content for clustering.

2.	**Text Preprocessing:** Preprocessing of text data is carried out for consistency and improving clustering results. This includes processes like tokenization, stopword removal, and stemming. 

3.	**Text Vectorization:** This refers to the conversion of text data into numerical vector forms for easier clustering. One common method involves Term Frequency-Inverse Document Frequency (TF-IDF). Still, other suitable methods may be chosen based on specific requirements.

4.	**Data Clustering:** With the vectorized data, an algorithm like K-means is implemented for dataset clustering. This algorithm is commonly used for unsupervised clustering and minimizes within-cluster sum of squared distances.

5.	**Cluster Prediction:** Upon the completion of data clustering, the system is equipped to predict a cluster for any new document. Predictions are based on the similarity existing between the new document and the centroids of previous clusters. 

6.	**Display of Clustered Documents:** Lastly, documents belonging to the predicted cluster would be displayed. This aids users in both the exploration and analysis of content within that cluster. 

## Installation
1. Clone the repository:
```git clone git@github.com:sanjok1988/clustering_documents.git```
2. Install dependencies:
```pip install -r requirements.txt```

## Usage
1. Run the main script:
```python app.py```

2. Access the search engine interface via web browser:
```http://localhost:5000```

## License
This project is licensed under the [MIT License](LICENSE).