class StadiumLogic:
    def __init__(self):
        self.stadium_dao = StadiumDao()

    def add_stadium(
            self,
            potential,
            address,
            name,
    ):
        self.stadium_dao.add_stadium(
            potential=potential,
            address=address,
            name=name,)

    def get_all_stadiums(self):
        stadiums = self.stadium_dao.get_all_stadiums()
        stadiums_dict = [{
            "name": stadium.name,
            "potential": stadium.potential,
            "address": stadium.address
        } for stadium in stadiums]
        return stadiums_dict
