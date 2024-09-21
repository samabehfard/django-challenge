from match.models import Match


class MatchDao:
    def add_match(
            self,
            home_matches,
            away_matches,
            date,
            time,
            default_price,
    ):
        Match.objects.create(
            home_matches=home_matches,
            away_matches=away_matches,
            date=date,
            time=time,
            default_price=default_price,
        )

    def get_all_matches(self):
        matches = Match.objects.all()
        return matches
    def get_match_by_id(self,match_id):
        return Match.objects.filter(id=match_id).first()