1. Introduction:

The global perfume industry is a multi-billion-dollar market shaped by consumer preferences, brand reputation, and pricing strategies. Using data science techniques such as data analysis, trend identification, and predictive modelling, this dataset helps explore key factors influencing the perfume market. It includes details like brand, perfume name, rating, price (USD), gender target, bottle size (ml), launch year, stock quantity, and fragrance notes to provide valuable insights.

By applying statistical analysis and machine learning models, we can uncover patterns in consumer purchasing behaviour, pricing strategies, and fragrance trends. Through feature engineering, we can analyse relationships between fragrance notes and consumer ratings or the impact of launch year on sales performance. These insights help businesses refine pricing strategies, improve inventory management, and stay competitive in the fragrance industry.

This data-driven approach allows businesses to use demand forecasting, customer segmentation, and competitive analysis for better decision-making. Using visualization tools like Matplotlib and Seaborn, we can present key findings in a clear and actionable manner.

2.Problem Definition & Dataset Selection

Problem Definition of Project:

The perfume industry is highly competitive, with brands constantly adjusting pricing, marketing strategies, and inventory to meet consumer demand. However, businesses often struggle to set optimal prices due to fluctuating market trends, consumer preferences, and other influencing factors. Incorrect pricing can lead to lost revenue, overstocking or understocking, and reduced customer satisfaction.

To make informed decisions, businesses need a data-driven approach to analyze pricing trends, fragrance preferences, and product availability. This project aims to examine the perfume market, focusing on factors that influence pricing, ratings, and stock availability. By leveraging analytical techniques, we can help businesses optimize their strategies for pricing, inventory management, and marketing.

Problem Statement of Dataset: 

The perfume market consists of a wide variety of brands, scents, and pricing strategies. Companies often struggle to determine the right price point for their products, as multiple factors—such as brand reputation, fragrance composition, bottle size, and consumer ratings—play a role in consumer purchasing decisions. Without a structured approach, pricing decisions may rely on intuition rather than concrete data, leading to inefficiencies in sales and inventory management.

This project will analyze and predict perfume pricing using a dataset containing attributes such as brand, perfume name, rating, price (USD), gender, bottle size (ml), launch year, stock quantity, and fragrance notes. The key objectives include:

1.	Identifying the factors that influence perfume pricing.

2.	Exploring consumer preferences based on ratings, fragrance notes, and gender categories.

3.	Analyzing stock quantity trends to understand demand and supply dynamics.

4.	Examining historical trends in perfume launches and their impact on pricing.

5.	Developing insights to help businesses optimize pricing strategies and inventory management.

The ultimate goal is to provide data-driven insights that help businesses enhance their market position and improve revenue generation while ensuring fair pricing for consumers.


Objectives of Dataset:

1. Understand the Factors Influencing Perfume Prices
o	Analyze how attributes like brand, fragrance notes, bottle size, and gender category affect price (USD).
o	Identify which variables have the strongest correlation with pricing.

2. Explore Consumer Preferences and Ratings
o	Investigate the relationship between consumer ratings and perfume pricing.
o	Determine if higher-rated perfumes tend to have higher prices and better sales.

3. Analyze Inventory and Demand Trends
o	Examine stock quantity to understand supply and demand variations.
o	Identify whether certain brands or fragrance types are frequently out of stock.

4. Evaluate Historical Trends in the Perfume Industry
o	Explore how launch years affect pricing and popularity.
o	Identify whether older or newer perfumes have a pricing advantage.

5. Perform Feature Engineering
o	Create new features such as perfume age (current year - launch year) to enhance analysis.
o	Convert categorical variables (e.g., fragrance notes, gender, brand) into numerical formats for machine learning.

6. Provide Actionable Insights for Businesses
o	Offer recommendations for pricing strategies based on data analysis.
o	Identify underperforming or overstocked perfumes that may need better marketing or discounting strategies.

7. Visualize Key Market Trends
o	Create charts and graphs to display trends in pricing, stock availability, and fragrance popularity.

Use data visualization tools like Matplotlib and Seaborn to present findings effectively.

Dataset Variables:

The dataset includes key variables that influence perfume pricing, consumer ratings, and inventory management.

1. Brand & Perfume Name
o	The manufacturer and specific perfume product (e.g., Chanel No. 5, Dior Sauvage).
o	Helps analyze brand reputation and its impact on pricing.

2. Rating
o	Consumer rating of the perfume (e.g., 4.5, 3.8, 5.0).
o	Indicates customer satisfaction and its potential effect on pricing and sales.

3. Price (USD)
o	The retail price of the perfume (e.g., $50, $120, $250).
o	The target variable for pricing analysis and optimization.

4. Gender
o	Indicates whether the perfume is marketed as male, female, or unisex.
o	Helps analyze how gender-based targeting affects consumer choices and pricing.

5. Bottle Size (ml)
o	The volume of the perfume bottle (e.g., 30ml, 50ml, 100ml).
o	Affects pricing strategies and consumer preferences.

6. Launch Year
o	The year the perfume was introduced (e.g., 1995, 2010, 2022).
o	Used to assess the impact of product age on pricing and demand.

7. Stock Quantity
o	The number of available units for each perfume.
o	Helps evaluate supply and demand dynamics in the market.

8. Fragrance Notes
o	Key scent components of the perfume (e.g., citrus, floral, woody, musky).
Used to analyze trends in consumer fragrance preferences and how they affect pricing.
Dataset Attributes:
1. Fragrance Category
o	The general scent profile of the perfume (e.g., Fresh, Oriental, Woody, Floral).
o	Helps categorize perfumes based on common fragrance families.

2. Price Range Classification
o	Categorizes perfumes into different pricing segments (e.g., Budget, Mid-range, Luxury).
o	Useful for identifying market positioning and consumer affordability trends.

3. Brand Popularity Score
o	A computed metric based on average rating and total reviews for a brand’s perfumes.

Helps compare brand reputation and consumer trust.
Dataset Types:
1. Numerical Variables
o	Represent quantitative data used for statistical analysis and modeling.
o	Examples: Price (USD), Rating, Stock Quantity, Bottle Size (ml), Launch Year.
2. Categorical Variables
o	Represent qualitative data used for grouping and comparison.
o	Examples: Brand, Gender, Fragrance Notes, Fragrance Category.
3. Target Variable
o	The dependent variable used for prediction.
o	Example: Price (USD).

By understanding these variables and their relationships, we can:
•	Conduct Exploratory Data Analysis (EDA) to uncover market trends.
•	Engineer new features such as perfume age (current year - launch year) to improve analysis.
•	Develop a predictive model to estimate perfume pricing accurately.
