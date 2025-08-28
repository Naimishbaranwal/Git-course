from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

import wikipedia, requests


Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        # get user query fro text input
        query=self.manager.current_screen.ids.user_query.text
        #get wiki page and list of image urls
        page=wikipedia.page(query,auto_suggest=False)
        image_link=page.images[0]
        return image_link
    
    def download_image(self):
        headers = {
            'User-Agent': 'My Wikipedia App (myemail@example.com)'
        }
        #download image
        req=requests.get(self.get_image_link(),headers=headers)
        path="files/image.jpg"
        with open(path,'wb') as file:
            file.write(req.content)
        return path

    def set_image(self):
        # set the image in image widget
        self.manager.current_screen.ids.img.source=self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()
    
    
if __name__ == '__main__':
    MainApp().run()


# import wikipedia


# page = wikipedia.page(title='Beach',auto_suggest=False)
# print(page.summary)
# link=page.images[0]
# headers = {
#     'User-Agent': 'My Wikipedia App (myemail@example.com)'
# }
# import requests
# req=requests.get(link,headers=headers)
# req.content #convert to bytes
# with open("Beach.jpg",'wb') as file:
#     file.write(req.content)

