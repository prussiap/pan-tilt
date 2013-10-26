import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os
from Adafruit_PWM_Servo_Driver import PWM
import time
from tornado.options import define, options
# start servo stuff
pwm = PWM(0x40, debug=True)

angleMin = 0
angleMax = 180
angleRange = angleMax - angleMin

tickMinTower = 110
tickMaxTower = 650
tickRange = tickMaxTower - tickMinTower

tickMin = 140
tickMax = 690
tickRange = tickMax - tickMin

frequency = 60
pwm.setPWMFreq(frequency)

def angleToms(angle):
  ticksOut = ((angle * tickRange) / angleRange) + tickMin
  return float(ticksOut)

def setPulseDegree(channel, freq, angle):
  ticksOn = angleToms(angle)
  print "%.2f ticksOn for 90 angle" % float(ticksOn)
  pwm.setPWM(channel, 0, int(ticksOn))

# Stop servo stuff
define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message("Hello World")

    def on_message(self, message):
        print 'message received %s' % message
        setPulseDegree(14, 60, int(message))

    def on_close(self):
      print 'connection closed'

#settings = dict(template_path=os.path.join(os.path.dirname(__file__), "static"))



def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WSHandler)],
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
