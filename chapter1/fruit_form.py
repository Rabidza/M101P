import bottle

@bottle.route('/')
def home_page():
    my_things = ['apple', 'orange', 'banana', 'peach']
    # return bottle.template('hello_world', username="Neill", things=mythings)
    return bottle.template('hello_world', {username:"Sibyl", 
                            'things':mythings})
                            
@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit = "No Fruit Selected"
        
    # NH - Add cookie to website
    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect("/show_fruit")
    
    # NH - They removed this return from the video when they added the cookie   
    # NH - I think this was done because of the redirect function
    # NH - show_fruit() now returns the template 
    #return bottle.template('fruit_selection.tpl', {'fruit':fruit})
    
@bottle.rout('/show_fruit')
def show_fruit():
    fruit = bottle.request.getCookie("fruit")
    
    return bottle.template('fruit_selection.tpl'), {'fruit':fruit})_
    
    
bottle.debug(True)
bottle.run(host='localhost', port=8080)

