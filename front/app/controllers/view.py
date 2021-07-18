
from app import app
from .api import WebService
from flask import render_template, redirect, request
 
@app.route('/', methods=['GET', 'POST'])
def Authentication():

    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        if 'login-submit' in request.form:
            res = WebService().loginUser(username, password)
            if not hasattr(res, "status_code"):
                return redirect(f'/notes/?refresh={res}')


        if 'register-submit' in request.form:
            created_user = WebService().createUser(username, password)

            if created_user.status_code == 201:
                res = WebService().loginUser(username, password)
                return redirect(f'/notes/?refresh={res}')

        
    return render_template('authentication.html')

@app.route('/notes/', methods=['GET', 'POST'])
def index():
    refresh = request.args.get('refresh') or request.values.get('refresh')
    if request.args.get('logout'):
        return redirect('/')

    page = request.args.get('page')
    if page:
        data = WebService().getData(refresh ,int(page))
        if data == 'denied':
            return redirect('/')
    else:
        page = 1
        data = WebService().getData(refresh ,page)
        if data == 'denied':
            return redirect('/')
    # breakpoint()
    pagenext = data['next']
    pageprev = data['previous']

    if request.method == 'POST':
        pk = request.values.get('pk')
        title = request.values.get('title')
        body = request.values.get('body')

        if 'delete' in request.form:
            WebService().delData(refresh, pk)

        elif 'save'  in request.form:
            WebService().putData(refresh, pk, title, body)

        elif 'create' in request.form:
            WebService().createData(refresh, title, body)

        return redirect(f'/notes/?page={page}&refresh={refresh}')

    
    return render_template('index.html', data=data,
         pagenext=pagenext, pageprev=pageprev, page=int(page),refresh=refresh  )
