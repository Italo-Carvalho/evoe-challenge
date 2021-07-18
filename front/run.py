from app import app

if __name__ == "__main__":
    app.secret_key = 'd*421341a==d.21=sa12;;.'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()