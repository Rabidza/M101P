import bottle

@bottle.route('/')
# NH - this function can be called anything
def home_page():
    return "Hello World\n"
    
@ bottle.route('/testpage')
def test_page():
    return "this is a test page"
    
bottle.debug(True)
bottle.run(hots='localhost', port=8080)