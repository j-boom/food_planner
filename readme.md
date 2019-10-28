This is my readme file.

The purpose of this project is to create a food planner that, given the goals for the daily macro counts in a week, and a set of planned dinners,
Will return a macro-balanced food plan and grocery list.

SQLite Database Construct:

Index | Name | Base Serving | Carbs (g) | Fat (g) | Protein (g) | Fiber (g) | Breakfast | Lunch | Dinner | Snacks | Last Used | Times Logged
--------------------------------------------------------------------------------------------------------------------------------------------
INT   | TEXT |     TEXT     |    REAL   |  REAL   |   REAL      |   REAL    |   BOOL    |  BOOL |  BOOL  |  BOOL  |   TEXT    |     INT