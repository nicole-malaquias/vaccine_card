from sqlalchemy import Column,String,DateTime, select
from dataclasses import dataclass
import datetime

from app.configs.database import db

@dataclass
class VaccineModel(db.Model):
    
    __tablename__ = 'vaccine_card'
    
    cpf = Column(String,primary_key=True)
    name =  Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String,nullable=False)
    health_unit_name = Column(String)
    


    def to_json(self):
        return {"cpf": self.cpf, "Name":self.name,"first_shot_date":self.first_shot_date, "second_shot_date":self.second_shot_date, "vaccine_name": self.vaccine_name, "health_unit_name":self.health_unit_name} 
        
       








