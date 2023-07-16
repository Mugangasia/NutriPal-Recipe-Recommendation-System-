import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the trained model and other necessary data
model = 'content_user_model.pkl'  
vectorizer_file = 'tfidf_vectorizer.pkl'  
kenyan_data_file = 'Kenyan.csv'  
foreign_data_file = 'Foreign.csv'  

# Load vectorizer from file
vectorizer = pd.read_pickle(vectorizer_file)

# Load Kenyan data
kenyan_data = pd.read_csv(kenyan_data_file)
kenyan_data['text'] = kenyan_data['ingredients'] + ' ' + kenyan_data['steps']
kenyan_features = vectorizer.transform(kenyan_data['text'])

# Load Foreign data (if available)
if foreign_data_file:
    foreign_data = pd.read_csv(foreign_data_file)
    foreign_data['text'] = foreign_data['ingredients'] + ' ' + foreign_data['steps']
    foreign_features = vectorizer.transform(foreign_data['text'])
else:
    foreign_data = None

# Define the Streamlit app
def main():
    # Set the title and subtitle of the app
    st.title("NutriPal Recipe Recommender")
    st.subheader("Discover your next delicious recipe!")

    # Create user input field
    user_input = st.text_area("Enter your preferences")

    # Create input field for calories
    calories = st.number_input("Enter calories", min_value=0, max_value=1000 )

    # Create dropdown menu for recipe types
    recipe_type = st.selectbox("Select Recipe Type", ["Kenyan", "Foreign"])

    # Add a button to trigger the recommendation
    if st.button("Get Recommendations"):
        # Perform recommendation based on selected recipe type
        if recipe_type == "Kenyan":
            recommendations = recommend_recipes(user_input, calories, kenyan_data, kenyan_features)
        else:
            recommendations = recommend_recipes(user_input, calories, foreign_data, foreign_features)
        
        # Display recommendations
        st.subheader("Recommended Recipes")
        st.dataframe(recommendations)
# Function to recommend top-N recipes based on user preferences
def recommend_recipes(user_preferences, calories, data, features, top_n=5):
    # Transform user preferences into a TF-IDF feature vector
    user_preferences_features = vectorizer.transform([user_preferences])

    # Calculate the cosine similarity between user preferences and recipes
    similarity_scores = cosine_similarity(user_preferences_features, features)

    # Get the indices of the top-N similar recipes within the specified calorie limit
    valid_indices = data[data['calories'] <= calories].index
    top_indices = similarity_scores.argsort()[0]
    top_indices = [idx for idx in top_indices if idx in valid_indices][-top_n:][::-1]

    # Get the recipe details and create a DataFrame
    recommendations = data.loc[top_indices, ['name', 'ingredients', 'steps']]
    recommendations.reset_index(drop=True, inplace=True)

    return recommendations

if __name__ == "__main__":
    main()