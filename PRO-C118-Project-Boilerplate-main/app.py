from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route('/save_review', methods=['POST'])
def save_review():
    data = request.get_json()

    review = data.get('review')
    sentiment = data.get('sentiment')
    # Add more data fields as needed

    # Define the CSV file path
    csv_file_path = 'reviews.csv'

    # Write data to the CSV file
    with open(csv_file_path, 'a', newline='') as csvfile:
        fieldnames = ['Review', 'Sentiment']  # Add more fields as needed
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'Review': review,
            'Sentiment': sentiment,
            # Add more data fields as needed
        })

    # Return the response with sentiment and emoticon path
    response_data = {
        'sentiment': sentiment,
        'emoticonPath': '/path/to/emoticon.png'  # Replace with the actual path
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
