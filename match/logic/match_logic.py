from Stadium.dao.stadium_dao import StadiumDao
from match.dao.match_dao import MatchDao


class MatchLogic:
    def __init__(self):
        self.match_dao = MatchDao()
        self.stadium_dao = StadiumDao()
    def add_match(
            self,
            home_matches,
            away_matches,
            date,
            time,
            default_price,
            stadium_id
    ):
        stadium = self.stadium_dao.get_stadium_by_id(stadium_id)
        self.match_dao.add_match(
            home_matches=home_matches,
            away_matches=away_matches,
            date=date,
            time=time,
            default_price=default_price,
            stadium=stadium
        )

    def get_all_matches(self):
        all_matches = self.match_dao.get_all_matches()
        matches_dicts = [
            {
                "home_matches": match.home_matches,
                "away_matches": match.away_matches,
                "date": match.date,
                "time": match.time,
                "default_price": match.default_price,
            }
            for match in all_matches
        ]
        return matches_dicts
