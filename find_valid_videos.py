import urllib.request

candidates = [
    'https://videos.pexels.com/video-files/7578552/7578552-hd_1920_1080_30fps.mp4',
    'https://videos.pexels.com/video-files/7578552/7578552-uhd_2560_1440_30fps.mp4',
    'https://videos.pexels.com/video-files/6873552/6873552-hd_1920_1080_25fps.mp4',
    'https://videos.pexels.com/video-files/5856417/5856417-hd_1920_1080_25fps.mp4',
    'https://videos.pexels.com/video-files/856973/856973-hd_1920_1080_25fps.mp4',
    'https://videos.pexels.com/video-files/2499611/2499611-hd_1920_1080_30fps.mp4',
    'https://videos.pexels.com/video-files/1409899/1409899-hd_1920_1080_25fps.mp4',
    'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4' # control
]

valid = []
for u in candidates:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=4)
        if res.status == 200:
            print(f"VALID: {res.headers.get('Content-Length')} bytes -> {u}")
            valid.append(u)
    except Exception as e:
        pass

print(f"\nTotal valid: {len(valid)}")

