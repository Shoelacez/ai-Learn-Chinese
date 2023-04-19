import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ['OPENAI_KEY']


def generate_quiz(difficulty, num_questions):
    # Define the prompt based on user parameters
    prompt = f"Generate a Chinese vocabulary quiz with {num_questions} questions and {difficulty} difficulty."

    # Send the prompt to ChatGPT
    response = openai.Completion.create(
        engine="davinci",  # specify the GPT-3 engine to use
        prompt=prompt,
        temperature=0.7,  # controls the "creativity" of the generated text
        max_tokens=1024,  # controls the maximum length of the generated text
        n=1,  # number of responses to generate
        stop=None  # stop generation at specified string
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    # Process the generated text to extract the quiz questions and answers
    # You can use regular expressions or other methods to do this

    # Return the processed quiz questions and answers to the user
    return generated_text


print(generate_quiz('hard', 10))
