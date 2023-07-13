# NutriPal-Recipe-Recommendation-System-
# Capstone Project at Moringa School Phase 5 
NutriPal Recipe Recommendation System
# Project Overview 
In the rapidly growing health and wellness industry, individuals are increasingly seeking practical solutions to make informed dietary choices and improve their overall well-being. However, navigating the vast array of diet plans, meal delivery services, and health apps can be overwhelming. Stakeholders in this industry face the critical challenge of providing personalized and accurate nutrition recommendations that meet individual's unique needs and preferences.

A significant problem is the lack of tailored nutrition guidance available in the market. Existing solutions often offer generic diet plans that do not consider individual factors such as age, gender, body composition, dietary restrictions, and cultural preferences. Consequently, individuals may experience frustration and disappointment when these solutions fail to deliver the desired results, leading to a decline in motivation and a higher likelihood of abandoning their healthy eating goals.

Furthermore, the fast-paced nature of modern lifestyles presents another obstacle. Many individuals struggle to find the time and energy required to research, plan, and prepare nutritious meals regularly. This often results in resorting to unhealthy eating habits, negatively impacting their overall health and well-being.

By providing accurate and personalized nutrition recommendations, stakeholders in the health and wellness industry can differentiate their offerings, enhance customer satisfaction, and foster long-term adherence to healthy eating habits. Additionally, utilizing advanced technologies and user-friendly interfaces can create a competitive advantage and position stakeholders as leaders in the market.

# Problem Statement
The global prevalence of obesity and other diet-related chronic diseases is increasing. This is due in part to the increasing availability of unhealthy foods and the difficulty people have in making healthy food choices.

A food recommendations system could help people make healthier food choices by providing personalized recommendations based on their individual needs and preferences. This could help people improve their diet and reduce their risk of developing chronic diseases.

# Solution Statement
Lack of personalized nutrition recommendations: Existing solutions often rely on generic dietary guidelines that are based on population-level data. This approach can be effective for some individuals, but it may not be optimal for everyone. For example, generic guidelines may not take into account an individual's genetic makeup, which can play a role in determining how their body responds to different foods. Additionally, generic guidelines may not be tailored to an individual's lifestyle or health goals. For example, someone who is trying to lose weight may need different recommendations than someone who is trying to manage a chronic disease.

Time and effort constraints for meal planning: Busy lifestyles can make it difficult for individuals to find the time and energy to plan and prepare healthy meals. This can be especially challenging for people who work long hours or have young children. Additionally, meal planning can be time-consuming and complex, especially if an individual has food allergies or intolerances.

# Objectives
### Main objective.
Develop a Food/Recipe Recommendation System that suggests nutritious food to individuals and promoting a healthy lifestyle.

### Specific Objectives.
* Identify the key features and factors that impact an individual's overall health, and determine which ones should be incorporated into the food recommendation system.

* Clean and preprocess the nutrition data available in the dataset, and combine it with external data sources to create a comprehensive nutrition database that can be used by the recommendation system.

* Develop and implement recommendation algorithms that can generate personalized food recommendations based on the user's individual characteristics such as age, gender, degree of physical activity, locally available foods, and dietary customs.

* Create a chatbot that can interact with users and collect relevant information such as dietary preferences, and restrictions, as well as any other relevant information that can be used to personalize food recommendations.

* Integrate the recommendation algorithms and chatbot into a user-friendly and intuitive interface that allows users to easily access and interact with the system.

* Deploy the food recommendation system and chatbot, and conduct user testing to gather feedback and identify areas for improvement.

# Metrics Of Success.
Our recommender system will be considered successful if it meets the following criteria:

* Have a recall score of ```80%``` and above.
* Have a mean absolute precission at least ```90%.```
* Have a coverage of around 90%.This means that the model is able to recommend a wide variety of nutritious foods and recipes to users

# Data Understanding
This project will include ```3``` datasets

* *Recipes*

* *Nutrition*

* *Kenyan Local Food Recipes*

Recipes data set was obtained from [here](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions) . It contains a list of ```231636``` rows of recipes and ```12``` columns.

* name - Recipe name
* id - Recipe ID
* minutes - Minutes to prepare recipe
* contributor_id - User ID who submitted this recipe
* submitted - Date recipe was submitted
* tags - Food.com tags for recipe
* nutrition - Nutrition information (calories (#), total fat (PDV), sugar (PDV) ,sodium (PDV) , protein (PDV) , saturated fat (PDV) , and carbohydrates (PDV))
* n_steps - Number of steps in recipe
* steps - Text for recipe steps, in order
* description - User-provided description
* ingredients - List of ingredient names
* n_ingredients - Number of ingredients
  
The nutrition dataset was obtained from [here](https://www.kaggle.com/datasets/trolukovich/nutritional-values-for-common-foods-and-products).

This dataset contains information on approximately ```8.8``` thousand types of food. The dataset includes various features related to the nutrition value of each food item per ```100gram``` serving. There are ```75``` features in total, you can find features like ```calories, vitamin_d, zink, protein, lactose.``` As you can see features names are very self-explanatory, so a description is not provided.

The Kenyan Dataset was ontained from [here](https://cookpad.com)
The dataset contains information about recipes, including their ```names```, ```cooking time (in minutes)```, ```ingredients```, ```steps```, ```serving size```, and ```nutritional information.```
There are ```218``` entries (recipes) in the dataset.

The ```'Serving'``` column represents the serving size of each recipe.
The ```'calories',``` ```'total fat (PDV)'```, ```'sugar (PDV)'```, ```'sodium (PDV)'```, ```'protein (PDV)'```, ```'saturated fat (PDV)'```, and ```'carbohydrates (PDV)'``` columns  provide nutritional information for each recipe, expressed as a percentage of the re
*recommended daily value (PDV).
