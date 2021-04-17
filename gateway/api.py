from fastapi import FastAPI 
from pydantic import BaseModel
from nameko.standalone.rpc import ClusterRpcProxy

# broker_cfg = {'AMQP_URI': 'amqp://guest:guest@localhost'}
broker_cfg = {'AMQP_URI': 'amqp://guest:guest@rabbitmq'}

class Person(BaseModel):
    cardid:str
    studentname:str
    studentid:str
    studentaccount:str

app = FastAPI()

@app.get("/info")
def api():
    ret = {
        "info": "gateway"
    }
    return ret

@app.post("/createdb")
def create_db():
    with ClusterRpcProxy(broker_cfg) as rpc:
        ret = rpc.dbservices.create()
    
    return ret

@app.post("/insert")
def insert_db(payload: Person):
    with ClusterRpcProxy(broker_cfg) as rpc:
        ret = rpc.dbservices.insert(payload.cardid, payload.studentname, payload.studentid, payload.studentaccount)
    return ret

@app.get("/select")
def select_db():
    with ClusterRpcProxy(broker_cfg) as rpc:
        ret = rpc.dbservices.select()
    # print(ret)
    return ret

@app.delete("/delete/{id}")
def delete_id(id):
    with ClusterRpcProxy(broker_cfg) as rpc:
        ret = rpc.dbservices.delete(id)
    return ret

@app.delete("/drop")
def drop_table():
    with ClusterRpcProxy(broker_cfg) as rpc:
        ret = rpc.dbservices.drop()
    return ret
