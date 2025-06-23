from flask import render_template
import random
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/welcome/<string:name>')
def welcome(name='Team'):
    return render_template('welcome.html', title="Welcome", name=name.title(), group='Everyone')


@app.route('/joke')
def joke():
    joke_number = random.randrange(len(joke_dict))
    joke_question = joke_dict[joke_number][0]
    joke_answer = joke_dict[joke_number][1]
    return render_template('joke.html', title="Joke Time", joke_question=joke_question, joke_answer=joke_answer, number_of_jokes=len(joke_dict))


joke_dict = {0: ["Why was Cinderella so bad a football?", "She kept running away from the ball!"],
             1: ["What do you call a pile of cats?", "A meow-ntain"],
             2: ["Why did the bicycle fall over?", "Because it was two tired"],
             3: ["What do you call a sad strawberry?", "A blueberry!"],
             4: ["How do you organise a space party?", "You planet."],
             5: ["What do cows read the most?", "Cattle-logs."]
             }
