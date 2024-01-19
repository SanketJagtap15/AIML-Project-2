from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

# Dictionary of admission-related responses
admission_responses = {
    'hi': 'Hi, I am your Admission Helper. How can I help you?',
    'hello': 'Hello, I am your Admission Helper. How can I help you?',
    'admission procedure': 'To apply for admission, visit our official website and fill out the online application form.',
    'admission requirements': 'The admission requirements include a minimum GPA of 3.0, a letter of recommendation, and a personal statement.',
    'admission deadline': 'The admission deadline is typically on March 1st each year.',
    'documents required': 'You will need to submit the following documents: academic transcripts, letters of recommendation, personal statement, and proof of identity.',
    'eligibility criteria': 'The eligibility criteria include a bachelor\'s degree in a relevant field, a competitive GRE score, and proficiency in English.',
    'application fee': 'There is an application fee of $50, which can be paid online during the application process.',
    'application review': 'Once your application is submitted, it will undergo a thorough review by the admissions committee.',
    'interview process': 'Shortlisted candidates may be called for an interview to assess their suitability for the program.',
    'default': 'I am sorry, but I do not have information on that. You can ask me about (admission procedure, admission requirements, admission deadline, documents required, eligibility criteria, application fee, application review, interview process etc.).'
}


# Dictionary to store user context
user_context = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/admission-chat', methods=['POST'])
def process_chat():
    user_input = request.json['user_input']

    # Get the bot's response
    bot_response = respond_to_query(user_input)

    return jsonify({'response': bot_response})


def respond_to_query(query):
    # Check if the query matches any predefined responses
    for key, response in admission_responses.items():
        if key in query.lower():
            return response

    # If the query is about a deadline, fetch real-time information
    if 'deadline' in query.lower():
        return fetch_admission_info()

    # If no match is found, provide a default response
    return admission_responses['default']


def fetch_admission_info():
    # Replace this with actual backend integration logic
    return "The admission deadline is January 31, 2024."


if __name__ == "__main__":
    app.run(debug=True)
