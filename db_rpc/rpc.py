from nameko.rpc import rpc
import db 

class Services:
    name = "dbservices"

    @rpc
    def create(self):
        ret = db.create_db()
        return ret

    @rpc
    def insert(self, cardid, studentname, studentid, studentaccount):
        params = [ cardid, studentname, studentid, studentaccount]
        ret = db.insert_db(params)
        return ret

    @rpc
    def select(self):
        ret = db.select_db()
        return ret
    
    @rpc
    def delete(self, id):
        ret = db.delete_db(id)
        return ret
    
    @rpc
    def drop(self):
        ret = db.drop_table()
        return ret