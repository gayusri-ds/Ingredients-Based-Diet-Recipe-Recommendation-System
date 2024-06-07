import streamlit as st
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# Load the saved models and data
tfidf = joblib.load(r'C:/Users/DELL/Desktop/My Projects/Indian food diet chatbot/Ingredients rec sys/tfidf_vectorizer.pkl')
tfidf_matrix = joblib.load(r'C:/Users/DELL/Desktop/My Projects/Indian food diet chatbot/Ingredients rec sys/tfidf_matrix.pkl')
df = joblib.load(r'C:/Users/DELL/Desktop/My Projects/Indian food diet chatbot/Ingredients rec sys/recipe_dataframe.pkl')

def recommend_recipes(user_input, df, tfidf, tfidf_matrix):
    user_tfidf = tfidf.transform([user_input])
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    
    recommended_indices = cosine_similarities.argsort()[-10:][::-1]
    return df.iloc[recommended_indices]

# Streamlit app
st.title('🍽️ Indian Food Recipe Recommendation 🥘')

st.markdown("""
Welcome to the Indian Food Recipe Recommendation System! Enter the ingredients you have, and discover delicious recipes you can make. 
Get ready to cook something amazing! 🍏🌽🍊🧅
""")

user_input = st.text_input("Enter ingredients or food items you have:")

if st.button('Recommend Recipes'):
    if user_input:
        recommendations = recommend_recipes(user_input, df, tfidf, tfidf_matrix)
        st.write("✨ Top recommended recipes for you:")
        for index, row in recommendations.iterrows():
            st.subheader(f"🍲 {row['TranslatedRecipeName']}")
            st.write(f"**Ingredients:** {row['TranslatedIngredients']} 🌶️🌽🥕🧅")
            st.write(f"🔗 [Recipe URL]({row['URL']})")
    else:
        st.write("🚫 Please enter some ingredients or food items to get started.")
