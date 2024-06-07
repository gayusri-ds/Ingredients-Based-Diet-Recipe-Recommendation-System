# 🥗 Ingredients-Based Recipe Recommendation System and Streamlit Deployment 🍲

## Project Overview

This project implements an ingredients-based recommendation system that suggests recipes based on the ingredients users have. The system is deployed using Streamlit to provide a user-friendly web interface.

## 1. Data Preprocessing

The initial step involves preprocessing the dataset to clean and prepare it for use in the recommendation system.

### Steps:
- Load the preprocessed dataset and ensure it contains necessary columns (`TranslatedRecipeName`, `TranslatedIngredients`, `URL`).

## 2. Ingredients-Based Recommendation System

An advanced feature of the project is the ingredients-based recommendation system that suggests recipes based on the ingredients users have.

### Steps:
- 🥒 Train a TF-IDF Vectorizer on the ingredients column to convert text data into numerical features.
- 🍅 Implement a function to recommend recipes based on cosine similarity between user input ingredients and dataset ingredients.

## 3. Streamlit Deployment of Ingredients-Based Recommendation System

🍛 The ingredients-based recommendation system was also deployed using Streamlit to provide an interactive web interface for users to input their available ingredients and get recipe recommendations.

### Features:
- Interactive web interface for user inputs.
- Dynamic filtering of recipes based on user-provided ingredients.
- Display of recommended recipes with a user-friendly layout.

### How to Run the Project

1. **Data Preprocessing**: Ensure the dataset is preprocessed and contains the necessary columns.
2. **Ingredients-Based Recommendation System**:
   - Implement and test the recommendation system locally.
   - **Streamlit Deployment**: Run the Streamlit app for an interactive web-based recommendation system.


### Conclusion

This project provides a comprehensive solution for recommending recipes based on user-provided ingredients. The deployment of the recommendation system using Streamlit makes it easily accessible and user-friendly.

### Acknowledgments

link to 6000 recipe dataset : 'https://data.mendeley.com/datasets/xsphgmmh7b/1'
Special thanks to the dataset providers and the open-source community for their invaluable resources and support.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.

