from Stadium.models import Stadium


class StadiumDao:
    def add_stadium(
            self,
            potential,
            address,
            name,
    ):
        stadium = Stadium.objects.create(
        potential=potential,
        address=address,
        name=name,
        )
        return stadium
    def get_all_stadiums(self):
        stadiums = Stadium.objects.all()
        return stadiums
    def get_stadium_by_id(self,stadium_id):
        stadium = Stadium.objects.filter(id=stadium_id).first()
        return stadium