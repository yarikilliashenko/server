import time
import pandas as pd
import cv2

class dt():
    folder = "C:/Users\YIllia01\Documents\mego/ntn/"
    url = "https://vs843.vcdn.biz/20f653851fab4bd0a8b63e49edf56869_megogo/live/hls/b/700_2490_4000/vo/629d33954cf0dd575b3bfdfe/o/25455141/u_uid/1105352916/u_vod/4/u_device/cms_html5/u_devicekey/_site/lip/62.205.130.2*asn/u_srvc/2741/te/1655465224/u_did/MToxMTA1MzUyOTE2OjE2NTUxOTMzMzA6OmIxODdlYTM2YTlhNjMyMjIyNTE3OGRjODlkNjMyNzZm/type.live/media-sid1985976332170550116-b4000000_4671567731_83754940_2100900_0000000000.ts"
    def __init__(self,date:str, url=None, folder=None):
        if not url is None:
            self.url = url
        if not folder is None:
            self.folder = folder
        if isinstance(date,int): date = date.__str__()
        if date.__len__() == 10:
            self.date = pd.to_datetime(date,unit='s')
        else:
            self.date = pd.to_datetime(date)
        self.int = self.date.timestamp().__int__()
        self.str = self.int.__str__()
        self.url = self.url[:-13] + self.str + self.url[-3:]
        self.filename = self.date.__str__().replace(':','-')
        self.path = self.folder+self.filename+".mp4"
        self.img_path = self.folder+"img/"+self.filename+".jpg"

    def request(self, save_im=False, save_mp4=False):
        self.video = cv2.VideoCapture(self.url)
        self.image = self.video.read()[1]
        if save_im:
            cv2.imwrite(self.img_path, self.image)

        print(self.date, end=" ")
        timee(total=True)

def timee(pr = True,total = False, st = [time.time(),0]):
    delta = time.time() - st[0]
    st[0] = time.time()
    st[1] += delta
    if pr:
        print(delta)
    if total:
        print(st[1])


timee(pr=False)

date = "2022-06-05 23:00:00"
start_time=dt(date).int
period = 60
count = 6*600

for i in [j for j in range(start_time,start_time+period*count,period) if -1*60<j%3600<-1*60 or -1*60<j%3600<61*60]:
    dt_novy = dt(i,
                 url="https://vs840.vcdn.biz/deed7b6f64f6db5b57f312d7bb9d4846_megogo/live/hls/b/700_2490_4000/vo/62a39ea34cf0dd575b4f5116/o/25401191/rsid/268dac77-e716-421a-8d61-428a35d075fc/u_uid/1105352916/u_vod/4/u_device/cms_html5/u_devicekey/_site/lip/62.205.130.2*asn/u_srvc/2741/te/1655465224/u_did/MToxMTA1MzUyOTE2OjE2NTUyODIxODY6OjlhYzRlMjdhMGIxMmUzMGJmYjRjNWRkYmE4YzM3NzNj/type.live/media-sid4289809489462861518-b4000000-a4521_4682326571_355470588_2379892_1655205952.ts",
                 folder="C:/Users\YIllia01\Documents\mego/novy/")
    dt_ntn = dt(i)
    dt_use = dt_novy

    try:
        dt_use.request(save_im=False)
        # print(dt_use.image)
    except Exception:
        print('catch')
