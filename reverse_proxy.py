from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route('/rms', defaults={'path': ''})
@app.route('/rms/<path:path>')
def proxy(path):
    url = 'https://rms.roomraccoon.com/admin/reservations/' + path
    headers = {
        'Referer': 'https://rms.roomraccoon.com/admin/reservations/',
        'User-Agent': request.headers.get('User-Agent')
    }
    cookies = request.cookies
    resp = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        cookies=cookies,
        data=request.get_data(),
        allow_redirects=False
    )
    excluded_headers = ['content-encoding',
                        'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)
    return response


if __name__ == '__main__':
    app.run()
