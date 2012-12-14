
#__author__ = 'liuchang
import requests as rq
import sys
import time



class downer():
    cookie = None
    def init(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
    def login(self):
        url = 'http://lightoj.com/login_check.php'
        info = {
            'myuserid':'nfcj000@qq.com',
            'mypassword':'757695453',
            'Submit':'Login'
        }
        r = rq.post(url,info)
        self.cookie = r.cookies
        print r.text
        print '================================'
        url = 'http://lightoj.com/login_success.php'
        r = rq.get(url,cookies=self.cookie)
        print r.text

    def down_1000(self):
        url = 'http://lightoj.com/volume_showproblem.php?problem=1000&language=english&type=pdf'
        r = rq.get(url,cookies=self.cookie)
        f = open('problem1000.pdf','wb')
    #   // print r.content
        f.write(r.content)
        f.close()
    def down_by_id(self,id):
        url_pat = 'http://lightoj.com/volume_showproblem.php?problem=%d&language=english&type=pdf'
        url = url_pat%id;
#        //print url
        filename = './down/lightoj%d.pdf'%id

        f = open(filename , 'wb')
        r = rq.get(url,cookies=self.cookie)
        f.write(r.content)
        f.close()
        print "ok %d"%id
        time.sleep(4)
    def down_all(self):
        for i in range(1355,1435):
            self.down_by_id(i)
        #for i in range(2000,3000):
        #    self.down_by_id(i)
        #for i in range(3000,4000):
        #    self.down_by_id(i)
        #for i in range(4000,4035):
        #    self.down_by_id(i)
if __name__ == '__main__':
    down = downer()
    #down.init()
    down.login()
    down.down_all()
