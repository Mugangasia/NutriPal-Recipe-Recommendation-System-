import streamlit as st
import pandas as pd
import numpy as np

# Load the recipe data
df = pd.read_csv('Kenyan_recipe.csv')

def recommend_recipes_by_calories(df, target_calories, num_recipes=3):
    # Filter recipes with similar calorie counts
    similar_recipes = df[df['calories'].between(target_calories - 100, target_calories + 100)]

    # Sort the recipes by their similarity to the target calorie count
    similar_recipes = similar_recipes.sort_values(by=['calories'], ascending=True)

    # Select the top N most similar recipes
    recommended_recipes = similar_recipes.head(num_recipes)

    return recommended_recipes

def main():
    # Set the page title
    st.title('Recipe Recommendation System')

    # Add a sidebar section
    st.sidebar.title('User Input')

    # Get user input for target calories
    target_calories = st.sidebar.number_input('Enter Target Calories', min_value=0)

    # Add a button to trigger recipe recommendations
    if st.sidebar.button('Get your Best Healthy Recipes'):
        # Generate recommendations based on user input
        recommendations = recommend_recipes_by_calories(df, target_calories)

        # Display the recommendations
        if len(recommendations) > 0:
            st.header('Recommended Recipes')
            for index, row in recommendations.iterrows():
                st.subheader(row['name'])
                st.write('**Ingredients:**')
                ingredients_list = row['ingredients'].split('\n')
                for ingredient in ingredients_list:
                    st.write('- ' + ingredient)

                st.write('**Steps:**')
                steps_list = row['steps'].split('\n')
                for i, step in enumerate(steps_list, start=1):
                    st.write(f'{i}. {step}')

                st.write('**Nutritional Information:**')
                st.write('- Calories:', row['calories'])
                st.write('- Total Fat:', row['total fat (PDV)'])
                st.write('- Sugar:', row['sugar (PDV)'])
                st.write('- Sodium:', row['sodium (PDV)'])
                st.write('- Protein:', row['protein (PDV)'])
                st.write('- Saturated Fat:', row['saturated fat (PDV)'])
                st.write('- Carbohydrates:', row['carbohydrates (PDV)'])

                st.write('---')
        else:
            st.write('No recommendations found.')

# Run the app
if __name__ == '__main__':
    main()
