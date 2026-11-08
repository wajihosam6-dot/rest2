import urllib.request

urls = [
    'https://assets.mixkit.co/videos/preview/mixkit-curved-swimming-pool-in-a-luxury-hotel-resort-41315-large.mp4',
    'https://assets.mixkit.co/videos/preview/mixkit-swimming-pool-in-a-luxury-resort-hotel-41314-large.mp4',
    'https://assets.mixkit.co/videos/preview/mixkit-beautiful-swimming-pool-of-a-luxury-hotel-41313-large.mp4',
    'https://videos.pexels.com/video-files/3125448/3125448-hd_1920_1080_24fps.mp4',
    'https://videos.pexels.com/video-files/4430322/4430322-hd_1920_1080_25fps.mp4',
    'https://videos.pexels.com/video-files/7578552/7578552-uhd_2560_1440_30fps.mp4'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        print(f"STATUS {res.status} | Content-Type: {res.headers.get('Content-Type')} | Length: {res.headers.get('Content-Length')}")
        print(f"URL: {u}\n")
    except Exception as e:
        print(f"FAILED {u}: {e}\n")

