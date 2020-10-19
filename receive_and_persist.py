from pathlib import Path

from werkzeug import run_simple, Request, Response


server = None


@Request.application
def application(request):
    token = request.args.get('token')
    if token:
        Path('/tmp/oauth2.token').write_text(token)
        raise KeyboardInterrupt
    return Response('No token received, serving...')


if __name__ == '__main__':
    server = run_simple('localhost', 4000, application)

