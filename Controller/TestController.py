from datetime import datetime
import json
from aiohttp import web
from ConfigurationManager import ConfigurationManager

configuration_manager = ConfigurationManager.get_instance()
mykey = configuration_manager.get_app_settings("mykey1")

recording_data = {}

class TestController():

    def __init__(self):
        app = web.Application()
        app.add_routes([web.get('/getUser', TestController.get_data)])
        app.add_routes([web.put('/updateUser', TestController.update_user)])
        app.add_routes([web.post('/addUser', TestController.add_user)])
        app.add_routes([web.delete('/deleteUser', TestController.delete_user)])
        app.add_routes([web.get('/', TestController.startup)])
        web.run_app(app, port=5000)

    async def get_data(request):
        try:
            response_obj = { 'request_type' : 'Get request received', 'username':'test' }
            return web.Response(text=json.dumps(response_obj), status=200)

        except Exception as ex:
            return web.Response(text=str(ex), status=500)

    async def update_user(request):
        try:
            response_obj = { 'request_type' : 'Update request received' }
            return web.Response(text=json.dumps(response_obj), status=200)

        except Exception as ex:
            return web.Response(text=str(ex), status=500)


    async def add_user(request):
        try:
            user = request.query['name']
            print("Creating new user with name: " , user)
            response_obj = { 'status' : 'Post request succeed' }
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as e:
            ## Bad path where name is not set
            response_obj = { 'status' : 'failed', 'reason': str(e) }
            ## return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)

    async def delete_user(request):
        try:
            response_obj = { 'request_type' : 'Delete request received' }
            return web.Response(text=json.dumps(response_obj), status=200)

        except Exception as ex:
            return web.Response(text=str(ex), status=500)


    def startup(request):
        return web.Response(text="App is running....." + '\n\n\ntime is = ' + str(datetime.now()) + '\n\n\nmy config key value is = ' + mykey)

