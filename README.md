get_routes CLI
=====
Get routes with a number of transfers from the data file.

**Example of data:** https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat

**Description:** https://openflights.org/data.html

Usage
======
Run main.py from **/get_routes** directory

`python -m src.main path_to_file source_airport destination_airport number_of_tranfers`

Where **source_airport** and **destination_airport** are 3-letter (IATA) or 4-letter (ICAO) code, **maximum number** of transfers is 3.
