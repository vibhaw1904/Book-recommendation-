from flask import Flask, jsonify,request
from flask_cors import CORS
import joblib
import numpy as np
app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "http://localhost:3000"}})
# CORS(app, resources={r"/recommend": {"origins": "http://localhost:3000/recommend"}})
# Load your model and data from the 'popular.pkl' file
model = joblib.load('popular.pkl')
model2=joblib.load('pt.pkl')
model3=joblib.load('books.pkl')
model4=joblib.load('similarity_scores.pkl')
popular_data = model  
pt=model2
books=model3
similarity_scores=model4

@app.route('/', methods=['GET'])
def get_popular_data():
    # Convert the DataFrame to a list of dictionaries
    popular_data_dict = popular_data.to_dict(orient='records')

    # Use jsonify to return the list as JSON
    return jsonify({'popularData': popular_data_dict})

# @app.route('/recommend', methods=['GET'])
# def recommend():
#     try:
#         user_input = request.args.get('userInput')  # Extract the user input from query parameter

#         # Replace this section with your recommendation logic
#         index = np.where(pt.index == user_input)[0][0]
#         similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

#         recommendation_data = []
#         for i in similar_items:
#             item = {}
#             temp_df = books[books['Book-Title'] == pt.index[i[0]]]
#             item['Book-Title'] = temp_df['Book-Title'].values[0]
#             item['Book-Author'] = temp_df['Book-Author'].values[0]
#             item['Image-URL-M'] = temp_df['Image-URL-M'].values[0]
#             recommendation_data.append(item)

#         return jsonify({'recommendations': recommendation_data})
#     except Exception as e:
#          return jsonify({'error': str(e)})
if __name__ == '__main__':
    app.run(debug=True)
