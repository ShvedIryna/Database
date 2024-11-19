from my_project.db_init import db
from my_project.auth.models.actor import Actor


class ActorDAO:
    def get_all(self):
        return Actor.query.all()


    def get_by_id(self, actor_id):
        return Actor.query.get(actor_id)


    def create(self, data):
        new_actor = Actor(**data)
        db.session.add(new_actor)
        db.session.commit()
        return new_actor


    def update(self, actor_id, data):
        actor = Actor.query.get(actor_id)
        if actor:
            for key, value in data.items():
                setattr(actor, key, value)
            db.session.commit()
            return actor
        return None


    def delete(self, actor_id):
        actor = Actor.query.get(actor_id)
        if actor:
            db.session.delete(actor)
            db.session.commit()
            return True
        return False
