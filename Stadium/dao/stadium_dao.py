from Stadium.models import Stadium


class StadiumDao:
    def add_stadium(
            self,
            potential,
            address,
            name,
    ):
        Stadium.objects.create(
        potential=potential,
        address=address,
        name=name,
        )
