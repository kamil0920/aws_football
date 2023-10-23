import os
import sqlite3
import pandas as pd

SQL_QUERY_MATCH = "SELECT m.match_api_id," \
                  " League.name AS league_name," \
                  " season," \
                  " stage," \
                  " m.date," \
                  " AT.team_api_id AS away_team," \
                  " HT.team_api_id AS home_team," \
                  " home_team_goal," \
                  " away_team_goal," \
                  " m.possession," \
                  " m.shoton," \
                  " CASE" \
                  " WHEN m.home_team_goal > m.away_team_goal THEN 'H'" \
                  " WHEN m.home_team_goal < m.away_team_goal THEN 'A'" \
                  " WHEN m.home_team_goal = m.away_team_goal THEN 'D'" \
                  " END AS result_match," \
                  " H1.player_api_id as home_player_1," \
                  " H2.player_api_id as home_player_2," \
                  " H3.player_api_id as home_player_3," \
                  " H4.player_api_id as home_player_4," \
                  " H5.player_api_id as home_player_5," \
                  " H6.player_api_id as home_player_6," \
                  " H7.player_api_id as home_player_7," \
                  " H8.player_api_id as home_player_8," \
                  " H9.player_api_id as home_player_9," \
                  " H10.player_api_id as home_player_10," \
                  " H11.player_api_id as home_player_11," \
                  " A1.player_api_id as away_player_1," \
                  " A2.player_api_id as away_player_2," \
                  " A3.player_api_id as away_player_3," \
                  " A4.player_api_id as away_player_4," \
                  " A5.player_api_id as away_player_5," \
                  " A6.player_api_id as away_player_6," \
                  " A7.player_api_id as away_player_7," \
                  " A8.player_api_id as away_player_8," \
                  " A9.player_api_id as away_player_9," \
                  " A10.player_api_id as away_player_10," \
                  " A11.player_api_id as away_player_11" \
                  " FROM Match as m" \
                  " JOIN League on League.id = m.league_id" \
                  " LEFT JOIN Team AS HT on HT.team_api_id = m.home_team_api_id" \
                  " LEFT JOIN Team AS AT on AT.team_api_id = m.away_team_api_id" \
                  " LEFT JOIN Player AS H1 on H1.player_api_id = m.home_player_6" \
                  " LEFT JOIN Player AS H2 on H2.player_api_id = m.home_player_6" \
                  " LEFT JOIN Player AS H3 on H3.player_api_id = m.home_player_6" \
                  " LEFT JOIN Player AS H4 on H4.player_api_id = m.home_player_6" \
                  " LEFT JOIN Player AS H5 on H5.player_api_id = m.home_player_6" \
                  " LEFT JOIN Player AS H6 on H6.player_api_id = m.home_player_6" \
                  " LEFT JOIN Player AS H7 on H7.player_api_id = m.home_player_7" \
                  " LEFT JOIN Player AS H8 on H8.player_api_id = m.home_player_8" \
                  " LEFT JOIN Player AS H9 on H9.player_api_id = m.home_player_9" \
                  " LEFT JOIN Player AS H10 on H10.player_api_id = m.home_player_10" \
                  " LEFT JOIN Player AS H11 on H11.player_api_id = m.home_player_11" \
                  " LEFT JOIN Player AS A1 on A1.player_api_id = m.away_player_6" \
                  " LEFT JOIN Player AS A2 on A2.player_api_id = m.away_player_6" \
                  " LEFT JOIN Player AS A3 on A3.player_api_id = m.away_player_6" \
                  " LEFT JOIN Player AS A4 on A4.player_api_id = m.away_player_6" \
                  " LEFT JOIN Player AS A5 on A5.player_api_id = m.away_player_6" \
                  " LEFT JOIN Player AS A6 on A6.player_api_id = m.away_player_6" \
                  " LEFT JOIN Player AS A7 on A7.player_api_id = m.away_player_7" \
                  " LEFT JOIN Player AS A8 on A8.player_api_id = m.away_player_8" \
                  " LEFT JOIN Player AS A9 on A9.player_api_id = m.away_player_9" \
                  " LEFT JOIN Player AS A10 on A10.player_api_id = m.away_player_10" \
                  " LEFT JOIN Player AS A11 on A11.player_api_id = m.away_player_11" \
                  " WHERE League.name LIKE 'England Premier League'" \
                  " AND m.possession IS NOT NULL" \
                  " ORDER by date"
SQL_QUERY_PLAYERS = f"SELECT * FROM Player_Attributes"

PATH_DB = r"C:/Users/kamil/Documents/eu_soccer_ml/eu_soccer_database/database.sqlite"
CSV_PATH_MATCH = "../data/match_details.csv"
CSV_PATH_PLAYER_ATTR = "../data/player_attributes.csv"


def table_to_csv(db_path, csv_path, query):
    """Read a table from an SQLite database and save it to a CSV file."""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(query, conn)

    if not os.path.exists('../data'):
        os.makedirs('../data')

    df.to_csv(csv_path, index=False)
    conn.close()


def execute_data_loader():
    table_to_csv(PATH_DB, CSV_PATH_MATCH, SQL_QUERY_MATCH)
    table_to_csv(PATH_DB, CSV_PATH_PLAYER_ATTR, SQL_QUERY_PLAYERS)


if __name__ == "__main__":
    execute_data_loader()
