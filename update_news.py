import requests
import datetime
import re

def get_data():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 코인 정보
    res_c = requests.get("https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH").json()
    btc = format(int(res_c[0]['trade_price']), ',')
    # 뉴스 정보 (단순 추출)
    res_n = requests.get("https://news.google.com/rss/search?q=경제&hl=ko&gl=KR&ceid=KR:ko")
    titles = re.findall('<title>(.*?)</title>', res_n.text)[1:6]
    news_html = "".join([f"<p>• {t}</p>" for t in titles])
    
    html = f"<html><body style='background:#000;color:#0f0;padding:20px;font-family:monospace;'>"
    html += f"<h1>[ JARVIS SYSTEM v2.5 ]</h1><p>Sync: {now}</p><hr>"
    html += f"<h3>💰 CRYPTO</h3><p>BTC: {btc} KRW</p><hr>"
    html += f"<h3>📡 NEWS</h3>{news_html}</body></html>"
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

get_data()
