from flask import Flask

def init_app(app: Flask):
    
    from app.views.vaccine import bp_vaccine
    app.register_blueprint(bp_vaccine)

