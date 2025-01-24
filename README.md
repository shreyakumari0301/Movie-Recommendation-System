## 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System**, an end-to-end content-based recommendation system that suggests movies based on their metadata. The project uses `CountVectorizer` for feature extraction and cosine similarity for calculating recommendations.

---

## Features

- **Content-Based Recommendations**: Suggests movies similar to a user-provided movie based on metadata (e.g., tags).
- **Text Preprocessing**:
  - Removal of stopwords using NLTK.
  - Lowercasing and tokenization.
- **Vectorization**: Uses `CountVectorizer` to create feature vectors for movies.
- **Similarity Calculation**: Employs cosine similarity to compare movies.
- **Evaluation Metrics**:
  - **Coverage**: Measures the diversity of recommended movies.
  - Additional metrics like precision and recall can be added.

---

## Installation

Follow these steps to set up the project:

## Prerequisites

- Python 3.8 or higher
- Required libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `nltk`

## Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   
Run the Script: Open the Jupyter Notebook or Python script and execute the cells.

## How It Works

**Data Preprocessing:**

Converts tags into lowercase.
Removes stopwords using NLTK.
Feature Extraction:

Uses CountVectorizer to convert the preprocessed tags column into numerical feature vectors.
Recommendation Algorithm:

Computes cosine similarity between feature vectors.
Recommends top n movies based on the similarity scores.
Evaluation:

Evaluates system diversity using the coverage metric.

 ## Future Improvements
1. Hybrid Recommendations: Combine collaborative filtering with content-based filtering for better results.
2. Advanced Models: Use embeddings (e.g., Word2Vec, BERT) for feature representation.
3. Evaluation Metrics: Add precision, recall, and NDCG to measure recommendation quality.

## Contributing
Contributions are welcome! If you'd like to improve this project, please:

Fork the repository.
Create a new branch.
Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
Author: Shreya Kumari
Email: 23f2003785@ds.study.iitm.ac.in
GitHub: shreyakumari0301

