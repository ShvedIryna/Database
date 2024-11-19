from my_project.auth.dao.ActorDAO import ActorDAO

class ActorService:
    def __init__(self):
        self.actor_dao = ActorDAO()

    def get_all_actors(self):
        return self.actor_dao.get_all()

    def get_actor_by_id(self, actor_id):
        return self.actor_dao.get_by_id(actor_id)

    def create_actor(self, data):
        return self.actor_dao.create(data)

    def update_actor(self, actor_id, data):
        return self.actor_dao.update(actor_id, data)

    def delete_actor(self, actor_id):
        return self.actor_dao.delete(actor_id)
