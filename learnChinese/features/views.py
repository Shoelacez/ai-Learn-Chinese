from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dotenv import load_dotenv
import openai, os
import random
from .models import Conversation

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)


# Create your views here.
def home(request):
    return render(request, 'features/home.html')


def user_reviews(request):
    return render(request, 'features/user_reviews.html')


@login_required
def chineseGPT(request):
    return render(request, 'features/chineseGPT.html')


def translation_bot(request):
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        language = request.POST.get('language')
        # prompt = user_input
        prompt = f"Translate these texts from English to {language}: {user_input}"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            stop='.',
            temperature=0.5
        )

        chatbot_response = response["choices"][0]["text"]

    context = {"response": chatbot_response}
    return render(request, 'features/translation.html', context)


def generate_quiz(request, difficulty='intermediate', num_questions=1, topic='food', language='english'):
    questions = []

    # retrieve form data and generate quiz
    if api_key is not None and request.method == "POST":
        # print(request.POST)
        difficulty = request.POST.get("difficulty")
        num_questions = int(request.POST.get('num_questions'))
        topic = request.POST.get("topic")
        language = request.POST.get("language")
        openai.api_key = api_key
        prompt = f"Generate a Chinese multiple choice quiz in {language} with the topic '{topic}' with {num_questions} unique questions and {difficulty} difficulty according to HSK syllabus.The format of the response should be exactly like this, \n<Question number>: <the generated question>?\nA. <choice 1>\nB. <choice 2>\nC. <choice 3>\nD. <choice 4>\nAns. <answer to the question>"

        for i in range(num_questions):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=4000,
                n=1,
                stop=None
            )
            generated_quiz = response["choices"][0]["text"]
            lines = generated_quiz.split("\n")
            question = lines[2].split(": ")[1]
            a = lines[3].split(". ")[1]
            b = lines[4].split(". ")[1]
            c = lines[5].split(". ")[1]
            d = lines[6].split(". ")[1]
            ans = lines[7].split(". ")[1]

            # add question, answer choices, and correct answer to list
            questions.append({'question': question, 'a': a, 'b': b, 'c': c, 'd': d, 'correct_ans': ans})

            print((len(questions)))
        # Handle form submission [Currently Not working]
        # if request.POST.get("submit"):
        #     user_answers = []
        #     for i in range(num_questions):
        #         user_answer = request.POST.get(f"answer_{i + 1}")
        #         user_answers.append(user_answer)
        #
        #     # Compare user's answers with correct answers
        #     score = 0
        #     for i in range(num_questions):
        #         if user_answers[i] == questions[i]['correct_ans']:
        #             score += 1
        #
        #     context = {
        #         'difficulty': difficulty,
        #         'num_questions': num_questions,
        #         'questions': questions,
        #         'user_answers': user_answers,
        #         'score': score,
        #     }
        #     return render(request, 'features/AIquiz_result.html', context)

    context = {
        'difficulty': difficulty,
        'num_questions': num_questions,
        'questions': questions,
    }
    return render(request, 'features/AIquiz.html', context)





def conversation_simulation(request):
    if api_key is not None and request.method == "POST":
        difficulty = request.POST.get('difficulty')
        scenario = request.POST.get('scenario')
        # Set up OpenAI API
        openai.api_key = api_key

        # Define your conversation prompt
        prompt = f"Create a long dialogue between A and B in this scenario '{scenario}',the conversation has to be in accordance to the HSK syllabus with a difficulty of {difficulty}. The response should be in this exact format, <current speaker>: <chinese dialogue>.\t<pinyin>.\t Don't include english"
        # Generate the conversation script
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
            timeout=60,
        )

        print(response)

        # Extract the conversation from generated_convo
        generated_convo = response.choices[0].text
        convo_lines = generated_convo.split("\n")
        conversation = []
        for line in convo_lines:
            if line:
                name = line.split(":")[0]
                dialogue = line.split(".\t")[0]
                conversation.append((name.strip(), dialogue.strip()))

        # Save the conversation to the database
        # Conversation.objects.create(
        #     scenario=scenario,
        #     difficulty=difficulty,
        #     conversation=conversation
        # )
        #
        # convos = Conversation.objects.all()

        # Pass conversation to template
        context = {'conversation': conversation, 'scenario': scenario}
        return render(request, 'features/convo_simulation.html', context)

    else:
        return render(request, 'features/convo_simulation.html')



def personalized_lessons(request):
    return render(request, 'features/personalized_lessons.html')


def gamefication(request):
    return render(request, 'features/gamification.html')


def about(request):
    return render(request, 'features/about.html')
