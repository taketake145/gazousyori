# 動画をjupyterにいれてOpenCVをimportして画像キャプチャーを作成するプログラム

# -*- coding: utf-8 -*-
import cv2
import os
#動画ファイルを読み込む
file_name = u"images/PCvideo.mp4"
video = cv2.VideoCapture(file_name)
#スクリーンキャプチャを保存するディレクトリ
dir_name = "screen_caps"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
#フレーム数を取得
frame_count = int(video.get(7))
for i in range(frame_count):
    _, frame = video.read()
    cv2.imwrite(dir_name+ "/" + str(i) + ".png", frame)
     
     
# 輝度値を計算してそれぞれの平均値をグラフにプロットするプログラム
im0 = imread('screen_caps/0.png')
im1 = imread('screen_caps/1.png')
im2 = imread('screen_caps/2.png')
im3 = imread('screen_caps/3.png')
im4 = imread('screen_caps/4.png')
im5 = imread('screen_caps/5.png')
im6 = imread('screen_caps/6.png')
im7 = imread('screen_caps/7.png')
im8 = imread('screen_caps/8.png')
im9 = imread('screen_caps/9.png')
im10 = imread('screen_caps/10.png')
im11 = imread('screen_caps/11.png')
im12 = imread('screen_caps/12.png')
im13 = imread('screen_caps/13.png')
im14 = imread('screen_caps/14.png')
im15 = imread('screen_caps/15.png')
im16 = imread('screen_caps/16.png')
im17 = imread('screen_caps/17.png')
im18 = imread('screen_caps/18.png')
im19 = imread('screen_caps/19.png')
im20= imread('screen_caps/20.png')
im21= imread('screen_caps/21.png')
im22= imread('screen_caps/22.png')
im23= imread('screen_caps/23.png')
im24= imread('screen_caps/24.png')
im25= imread('screen_caps/25.png')
im26= imread('screen_caps/26.png')
im27= imread('screen_caps/27.png')
im28= imread('screen_caps/28.png')
im29= imread('screen_caps/29.png')
im30= imread('screen_caps/30.png')
im31= imread('screen_caps/31.png')
im32= imread('screen_caps/32.png')
im33= imread('screen_caps/33.png')
im34= imread('screen_caps/34.png')
im35= imread('screen_caps/35.png')
im36= imread('screen_caps/36.png')
im37= imread('screen_caps/37.png')
im38 = imread('screen_caps/38.png')
im39= imread('screen_caps/39.png')
im40= imread('screen_caps/40.png')
im41 =imread('screen_caps/41.png')
im42= imread('screen_caps/42.png')
im43= imread('screen_caps/43.png')
im44= imread('screen_caps/44.png')
im45 = imread('screen_caps/45.png')
im46= imread('screen_caps/46.png')
im47= imread('screen_caps/47.png')
im48= imread('screen_caps/48.png')
im49= imread('screen_caps/49.png')
im50 = imread('screen_caps/50.png')
im51= imread('screen_caps/51.png')
im52= imread('screen_caps/52.png')
im53= imread('screen_caps/53.png')

x = np.arange(0,54)
y = [im0.mean(),im1.mean(),im2.mean(),im3.mean(),
     im4.mean(),im5.mean(),im6.mean(),im7.mean(),
     im8.mean(),im9.mean(),im10.mean(),im11.mean(),
     im12.mean(),im13.mean(),im14.mean(),im15.mean(),
     im16.mean(),im17.mean(),im18.mean(),im19.mean(),
     im20.mean(),im21.mean(),im22.mean(),im23.mean(),
     im24.mean(),im25.mean(),im26.mean(),im27.mean(),
     im28.mean(),im29.mean(),im30.mean(),im31.mean(),
     im32.mean(),im33.mean(),im34.mean(),im35.mean(),
     im36.mean(),im37.mean(),im38.mean(),im39.mean(),
     im40.mean(),im41.mean(),im42.mean(),im43.mean(),
     im44.mean(),im45.mean(),im46.mean(),im47.mean(),
     im48.mean(),im49.mean(),im50.mean(),im51.mean(),
     im52.mean(),im53.mean()]



# プロット
plt.plot(x,y)
plt.xlim(0,54)
plt.ylim(0,100)
plt.ylabel("blightness value")
plt.title("pulse")
plt.show()
plt.savefig("mypulse.png")
