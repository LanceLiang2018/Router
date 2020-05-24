import importlib
import os
import sys
from flask import *
from base_logger import get_logger
import markdown


logger = get_logger()

app = Flask('manager')


def parse_router_json(name: str):
    path_app = os.path.join('apps', name)
    path_json = os.path.join(path_app, 'router.json')
    if not os.path.exists(path_app) or not os.path.exists(path_json):
        return None
    data = {}
    with open(path_json, encoding='utf8', errors='ignore') as f:
        try:
            data = json.load(f)
        except Exception as e:
            logger.error(str(e))
            return None
    logger.info(json.dumps(data))
    try:
        logger.info("requirements: " + str(data['requirements']))
        logger.info("description: " + str(data['description']))
        name = data['name']
        # data['name'] = name.lower()
        script = data['script']
        # app = data['app']
    except KeyError as e:
        logger.error('Key Error: ' + str(e))
        return None
    return data


dispatcher = {}
apps = []

settings = {
    'HOST_BASE': 'app.lanceliang2001.top'
}


for directory in os.listdir('apps'):
    data = parse_router_json(directory)
    if data is None:
        logger.error('App %s router.json error')
        continue
    sys.path.insert(1, 'apps/%s' % directory)
    pak = importlib.import_module("apps.%s.%s" % (data['name'], data['script']))
    dispatcher['/' + data['name']] = pak.app
    apps.append(data)


@app.route('/')
def index():
    print(request.host)
    if settings['HOST_BASE'] in request.host and settings['HOST_BASE'] != request.host:
        app_name = request.host.split(settings['HOST_BASE'])[0][:-1]
        for a in apps:
            if a['name'].lower() == app_name:
                app_name = a['name']
        return redirect('//%s/%s' % (settings['HOST_BASE'], app_name))

    res = '# Lance App Router\n\n在这里你可以检索、上传、管理你自己的Flask应用程序。\n\n'
    for a in apps:
        res = res + '- [%s](%s): %s\n' % (a['name'], '/' + a['name'], a['description']['description'])
    return markdown.markdown(res)


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=False)
