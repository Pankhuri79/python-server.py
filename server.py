import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        title = "HELLO MATES,PANKHURI HERE"
        bgcolor = "dodgerbblue"
        self.render("template.html", title=title, bgcolor=bgcolor)
        print(self.request)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
