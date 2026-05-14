import requests
import re
import datetime

def run():
    try:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 코인 정보
        res_c = requests.get("https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-SOL").json()
        coins = "".join([f"<p>{c['market']}: {format(int(c['trade_price']), ',')}원</p>" for c in res_c])
        # 수익 뉴스
        res_n = requests.get("https://news.google.com/rss/search?q=급등+수익+반도체&hl=ko&gl=KR&ceid=KR:ko")
        titles = re.findall('<title>(.*?)</title>', res_n.text)[1:6]
        news = "".join([f"<p>🔥 {t}</p>" for t in titles])
        
        html = f"<html><body style='background:#000;color:#0f0;padding:20px;'><h1>[ JARVIS v4.0 MONEY SCANNER ]</h1><p>{now}</p><hr><h3>COIN</h3>{coins}<h3>NEWS</h3>{news}</body></html>"
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Success: v4.0 File Created")
    except Exception as e:
        print(f"Error: {e}")

run()
