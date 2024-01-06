#!/usr/bin/env python3


"""Test the submitted solutions for exercise 2, problem 1 of AutoGIS."""

import pathlib
import tempfile

import dhash
import PIL

import geopandas
import pyproj
import shapely.wkt

from points_decorator import points


POLYGON_WKT = (
    "POLYGON ((29.99671173095703 63.748023986816406, "
    "31.58196258544922 62.90789794921875, 27.738052368164062 "
    "60.511383056640625, 26.50013542175293 60.44499588012695, "
    "26.652359008789062 60.646385192871094, 25.921663284301758 "
    "60.243743896484375, 22.90027618408203 59.806800842285156, "
    "23.257217407226562 59.91944122314453, 23.335693359375 "
    "60.02395248413086, 22.87444305419922 60.14555358886719, "
    "23.08465003967285 60.3452033996582, 22.565473556518555 "
    "60.211936950683594, 21.452774047851562 60.56249237060547, "
    "21.66388702392578 61.54027557373047, 21.065969467163086 "
    "62.59798049926758, 21.67659568786621 63.02013397216797, "
    "21.496871948242188 63.20353698730469, 22.339998245239258 "
    "63.27652359008789, 22.288192749023438 63.525691986083984, "
    "24.539581298828125 64.79915618896484, 25.444232940673828 "
    "64.9533920288086, 25.303749084472656 65.51513671875, "
    "24.669166564941406 65.65470886230469, 24.689163208007812 "
    "65.89610290527344, 24.174999237060547 65.79151916503906, "
    "23.68471908569336 66.26332092285156, 24.000761032104492 "
    "66.80228424072266, 23.57332992553711 67.1570053100586, "
    "23.76513671875 67.4168701171875, 23.430830001831055 "
    "67.47978210449219, 23.6597900390625 67.94589233398438, "
    "20.580928802490234 69.060302734375, 21.320831298828125 "
    "69.32611083984375, 22.398330688476562 68.71110534667969, "
    "23.97638702392578 68.83248901367188, 24.934917449951172 "
    "68.580810546875, 25.7611083984375 68.98916625976562, "
    "25.95930290222168 69.68568420410156, 26.476804733276367 "
    "69.9363784790039, 27.91069221496582 70.08860778808594, "
    "29.1027774810791 69.70597076416016, 29.29846954345703 "
    "69.48533630371094, 28.4355525970459 68.90263366699219, "
    "28.817358016967773 68.84700012207031, 28.459857940673828 "
    "68.53485107421875, 30.028610229492188 67.69471740722656, "
    "29.075136184692383 66.90360260009766, 30.13492774963379 "
    "65.70887756347656, 29.818885803222656 65.6533203125, "
    "29.640830993652344 64.92096710205078, 30.57735824584961 "
    "64.22373962402344, 29.99671173095703 63.748023986816406))"
)


class Test_Exercise_2_Problem_1:
    @points(1, "Problem 1: Not sure whether your `coordinate_pair` list is okay?")
    def test_coordinate_pair(self, problem1):
        assert problem1.coordinate_pairs == [
            (29.99671173095703, 63.748023986816406),
            (31.58196258544922, 62.90789794921875),
            (27.738052368164062, 60.511383056640625),
            (26.50013542175293, 60.44499588012695),
            (26.652359008789062, 60.646385192871094),
            (25.921663284301758, 60.243743896484375),
            (22.90027618408203, 59.806800842285156),
            (23.257217407226562, 59.91944122314453),
            (23.335693359375, 60.02395248413086),
            (22.87444305419922, 60.14555358886719),
            (23.08465003967285, 60.3452033996582),
            (22.565473556518555, 60.211936950683594),
            (21.452774047851562, 60.56249237060547),
            (21.66388702392578, 61.54027557373047),
            (21.065969467163086, 62.59798049926758),
            (21.67659568786621, 63.02013397216797),
            (21.496871948242188, 63.20353698730469),
            (22.339998245239258, 63.27652359008789),
            (22.288192749023438, 63.525691986083984),
            (24.539581298828125, 64.79915618896484),
            (25.444232940673828, 64.9533920288086),
            (25.303749084472656, 65.51513671875),
            (24.669166564941406, 65.65470886230469),
            (24.689163208007812, 65.89610290527344),
            (24.174999237060547, 65.79151916503906),
            (23.68471908569336, 66.26332092285156),
            (24.000761032104492, 66.80228424072266),
            (23.57332992553711, 67.1570053100586),
            (23.76513671875, 67.4168701171875),
            (23.430830001831055, 67.47978210449219),
            (23.6597900390625, 67.94589233398438),
            (20.580928802490234, 69.060302734375),
            (21.320831298828125, 69.32611083984375),
            (22.398330688476562, 68.71110534667969),
            (23.97638702392578, 68.83248901367188),
            (24.934917449951172, 68.580810546875),
            (25.7611083984375, 68.98916625976562),
            (25.95930290222168, 69.68568420410156),
            (26.476804733276367, 69.9363784790039),
            (27.91069221496582, 70.08860778808594),
            (29.1027774810791, 69.70597076416016),
            (29.29846954345703, 69.48533630371094),
            (28.4355525970459, 68.90263366699219),
            (28.817358016967773, 68.84700012207031),
            (28.459857940673828, 68.53485107421875),
            (30.028610229492188, 67.69471740722656),
            (29.075136184692383, 66.90360260009766),
            (30.13492774963379, 65.70887756347656),
            (29.818885803222656, 65.6533203125),
            (29.640830993652344, 64.92096710205078),
            (30.57735824584961, 64.22373962402344),
            (29.99671173095703, 63.748023986816406)
        ]

    @points(1, "Problem 1: Something is not quite right with `polygon`")
    def test_polygon(self, problem1):
        assert problem1.polygon.wkt == POLYGON_WKT

    @points(
        0.5,
        (
            "Problem 1: `geo` is not a `GeoDataFrame`, or it "
            "contains the wrong data"
        )
    )
    def test_gdf_geo(self, problem1):
        assert isinstance(problem1.geo, geopandas.GeoDataFrame)
        assert problem1.geo.at[0, "geometry"] == shapely.wkt.loads(POLYGON_WKT)

    @points(0.5, "Problem 1: The geo-data frame `geo` does not have a CRS")
    def test_gdf_crs(self, problem1):
        assert isinstance(problem1.geo, geopandas.GeoDataFrame)
        assert problem1.geo.crs == pyproj.CRS("EPSG:4326")

    @points(1, "Problem 1: Did you plot the data set?")
    def test_plot(self, problem1):
        with tempfile.TemporaryDirectory() as temp_dir:
            figure_path = pathlib.Path(temp_dir) / "plot.png"
            problem1._PLOT_1.get_figure().savefig(figure_path)
            image_hash = dhash.dhash_int(PIL.Image.open(figure_path))
        assert image_hash == 21330220210094937413253399277172186490

    @points(
        1,
        "Problem 1: Save the data to a GeoPackage "
        "`mysterious-polygon.gpkg` in `DATA_DIRECTORY`"
    )
    def test_shapefile(self, problem1):
        assert (problem1.DATA_DIRECTORY / "mysterious-polygon.gpkg").exists()
        df = geopandas.read_file(problem1.DATA_DIRECTORY / "mysterious-polygon.gpkg")
        assert len(df) == 1
