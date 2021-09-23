from flask import Blueprint, json, request, jsonify , current_app
from datetime import datetime
from app.models.vaccine_model import VaccineModel
import datetime 
from datetime import datetime, timedelta
import time

bp_vaccine = Blueprint('vaccine', __name__, url_prefix='/api')


@bp_vaccine.route('/vaccination',methods = ['POST'])
def post_add_person_vaccinated():
    
    data = request.get_json()
    
    if data['cpf'].isdigit() and len(data['cpf']) == 11 :
        
        today = time.strftime(f'%a, %d  %b %Y %H:%M:%S %z ')
        next_vaccine = (datetime.now() + timedelta(hours=2160)).strftime("%a, %d %b, %Y %H:%M:%S %z")
        
        
        new_vac = VaccineModel( 
                cpf = data["cpf"],
                name = data["name"],
                first_shot_date= today,
                second_shot_date= next_vaccine,
                vaccine_name = data["vaccine_name"],
                health_unit_name= data["health_unit_name"],                                                   
            )
        
        from app.configs.database import db 
        db.session.add(new_vac)
        db.session.commit()
       
        return jsonify(new_vac.to_json())

    
    return {"msg":"cpf deve conter 11 caracteres"},400
    
     
@bp_vaccine.route('/vaccination',methods = ['GET'])
def get_all_vaccinated():
    
    query = VaccineModel.query.all()
    
    list_json = [ person.to_json() for person in query]
    print(list_json)
    
    return jsonify(list_json)
