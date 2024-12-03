# asgmt-6-programming-and-data-analysis-2024

> Assignment 6: Programming and Data Analysis 2024.

- Define functions or classes in `asgmt.py` given their names, templates, and docstrings.
- Use file name as a relative path rather than using an absolute path when you import data.
- Run `test-runner.py` to validate your functions or classes.
- Upload `asgmt.py` to [NTU COOL](https://cool.ntu.edu.tw).

## 01. Define a function `import_teams_json` which imports the `teams_nba.json` as a `dict` in working directory.

```python
def import_teams_nba_json() -> dict:
    """
    >>> teams_nba_json = import_teams_nba_json()
    >>> type(teams_nba_json)
    dict
    >>> len(teams_nba_json["data"])
    30
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `find_teams_conference_division` which returns a team's conference and division in a `tuple` given team's abbreviation, based on `teams_nba.json` in working directory.

```python
def find_teams_conference_division(team_abb: str) -> tuple:
    """
    >>> find_teams_conference_division("BOS")
    ('East', 'Atlantic')
    >>> find_teams_conference_division("MIA")
    ('East', 'Southeast')
    >>> find_teams_conference_division("LAL")
    ('West', 'Pacific')
    >>> find_teams_conference_division("DEN")
    ('West', 'Northwest')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `find_teams_city` which returns a team's city given team's name, based on `teams_nba.json` in working directory.

```python
def find_teams_city(team_name: str) -> str:
    """
    >>> find_teams_city("Celtics")
    'Boston'
    >>> find_teams_city("Heat")
    'Miami'
    >>> find_teams_city("Lakers")
    'Los Angeles'
    >>> find_teams_city("Nuggets")
    'Denver'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `import_movies_csv()` which creates a DataFrame of IMDb's top 250 rated movies of all time given `movies.csv` in working directory.

```python
def import_movies_csv() -> pd.core.frame.DataFrame:
    """
    >>> movies = import_movies_csv()
    >>> type(movies)
    pandas.core.frame.DataFrame
    >>> movies.shape
    (250, 5)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 05. Define a function `find_top_gun_maverick()` which finds out "Top Gun: Maverick" given `movies.csv` in working directory.

```python
def find_top_gun_maverick() -> pd.core.frame.DataFrame:
    """
    >>> top_gun_maverick = find_top_gun_maverick()
    >>> type(top_gun_maverick)
    pandas.core.frame.DataFrame
    >>> top_gun_maverick.shape
    (1, 5)
    >>> print(top_gun_maverick)
          id              title  release_year  runtime  rating
    126  127  Top Gun: Maverick          2022      130     8.3
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `find_starwars_episodes()` which finds out "Star Wars" episodes given `movies.csv` in working directory.

```python
def find_starwars_episodes() -> pd.core.frame.DataFrame:
    """
    >>> starwars_episodes = find_starwars_episodes()
    >>> type(starwars_episodes)
    pandas.core.frame.DataFrame
    >>> starwars_episodes.shape
    (3, 5)
    >>> print(starwars_episodes)
        id                                           title  release_year  runtime  rating
    15  16  Star Wars: Episode V - The Empire Strikes Back          1980      124     8.7
    29  30              Star Wars: Episode IV - A New Hope          1977      121     8.6
    91  92      Star Wars: Episode VI - Return of the Jedi          1983      131     8.3
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `import_team_taiwan()` which creates a DataFrame of Taiwan's roster in Premier 12 2024 given `team_taiwan.csv` in working directory.

```python
def import_team_taiwan() -> pd.core.frame.DataFrame:
    """
    >>> team_taiwan = import_team_taiwan()
    >>> type(team_taiwan)
    pandas.core.frame.DataFrame
    >>> team_taiwan.shape
    (36, 7)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 08. Define a function `get_roster()` which returns player or coach names as a `list` given `team_taiwan.csv` in working directory.

```python
def get_roster(roster_type: str) -> list:
    """
    >>> roster_players = get_roster("players")
    >>> type(roster_players)
    list
    >>> len(roster_players)
    28
    >>> "CHEN Chieh-Hsien" in roster_players
    True
    >>> roster_coaches = get_roster("coaches")
    >>> type(roster_coaches)
    list
    >>> len(roster_coaches)
    8
    >>> "PENG Cheng-Min" in roster_coaches
    True
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 09. Define a function `get_information()` which returns player or coach information as a `tuple` based on his number given `team_taiwan.csv` in working directory.

```python
def get_information(number: int) -> tuple:
    """
    >>> get_information(24)
    ('CHEN Chieh-Hsien', 'OF', 'L/R', 173.0, 73.0, 1994.0)
    >>> get_information(45)
    ('LIN Yu-Min', 'P', 'L/L', 180.0, 82.0, 2003.0)
    >>> get_information(27)
    ('LIN Chia-Cheng', 'C', 'R/R', 185.0, 91.0, 1997.0)
    >>> get_information(40)
    ('WANG Chien-Ming', 'Pitching Coach')
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 10. Define a class `DataframeAttrs` which instantiates objects with 3 methods `get_shape()`, `get_dtypes()`, and `get_summary()`.

```python
class DataframeAttrs:
    """
    >>> movies = import_movies_csv()
    >>> dfa = DataframeAttrs(movies)
    >>> dfa.get_shape()
    (250, 5)
    >>> dfa.get_dtypes()
    id                int64
    title            object
    release_year      int64
    runtime           int64
    rating          float64
    dtype: object
    >>> dfa.get_summary()
                   id  release_year     runtime      rating
    count  250.000000    250.000000  250.000000  250.000000
    mean   125.500000   1986.816000  129.052000    8.309600
    std     72.312977     25.387086   29.916505    0.234538
    min      1.000000   1921.000000   45.000000    8.000000
    25%     63.250000   1966.250000  107.250000    8.100000
    50%    125.500000   1994.500000  126.500000    8.200000
    75%    187.750000   2007.000000  145.750000    8.400000
    max    250.000000   2023.000000  238.000000    9.300000
    >>> team_taiwan = import_team_taiwan()
    >>> dfa = DataframeAttrs(team_taiwan)
    >>> dfa.get_shape()
    (36, 7)
    >>> dfa.get_dtypes()
    number           int64
    name            object
    postion         object
    bats_throws     object
    height         float64
    weight         float64
    birth_year     float64
    dtype: object
    >>> dfa.get_summary()
              number      height      weight   birth_year
    count  36.000000   28.000000   28.000000    28.000000
    mean   46.555556  179.178571   82.607143  1996.678571
    std    28.872572    4.455987   10.314820     3.151173
    min     4.000000  168.000000   70.000000  1990.000000
    25%    22.500000  175.000000   75.000000  1994.000000
    50%    37.000000  179.000000   80.000000  1997.000000
    75%    70.250000  182.250000   90.250000  2000.000000
    max    99.000000  188.000000  110.000000  2003.000000
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```