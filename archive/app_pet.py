from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route("/")
@app.route("/index") 
def index():
    return '''
    <h1> Adopt a pet!</h1>
    <p>Browse through the links below to find your new furry friend</p>
    <ul><li><a href = "/animals/dogs">Dogs</a></li>
        <li><a href = "/animals/cats">Cats</a></li>
        <li><a href = "/animals/rabbits">Rabbits</a></li>
    </ul>
    '''

@app.route("/animals/<pet_type>")
def animals(pet_type):
    html =f'<h1>List of {pet_type}</h1>'
    for pos,pet in enumerate(pets[pet_type]):
        html+=f'<li><a href="/animals/{pet_type}/{pos}">'+pet['name']+'</li>'
    html = '<ul>'+html+'</ul>'    
    return html

@app.route("/animals/<pet_type>/<int:pet_id>") 
def pet(pet_type,pet_id):
    pet=pets[pet_type][pet_id]
    return f'''
    <h1>{pet["name"]}</h1>
    <img src ="{pet['url']}" >
    <p>{pet["url"]}</p>
    <ul><li>It is {pet["age"]}pet</li>
        <li>{pet["breed"]}</li>
    </ul>    
    '''

if __name__ == "__main__":
    app.run()