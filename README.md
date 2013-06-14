tribapps-gis
============  

A repo storing various GIS data we've made or use in our hacking that we'd like to make publicly available.

* DuPage County Board shapefiles -- found in Tribune data archives
* Kendall County Board shapefiles -- received from Kendall County's GIS office
* Lake County Board shapefiles -- made from a KML file found at http://gis2.co.lake.il.us/output/kmz/cboard2012.kml
* McHenry County Board shapefiles -- found in Tribune data archives
* Will County Board shapefiles -- received from Will County's GIS office
* Our custom-made Illinois judicial shapefiles, which we built by hand looking at individual counties on maps located at http://www.state.il.us/court/circuitcourt/circuitmap/map1.asp

Many other shapefiles are included, most are included unaltered from public sources.

Also included is a definitions.py file which is used by [django-boundaryservice](https://github.com/newsapps/django-boundaryservice).

All shapefiles:

* County Subdivisions [source](http://www.census.gov/cgi-bin/geo/shapefiles2010/main) [map](shapefiles/county_subdivisions/tl_2010_17_cousub10.geojson)
* Secondary School Districts [source](http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17) [map](shapefiles/secondary_school_districts/tl_2009_17_scsd.geojson)
* Cook County Park Tax Districts [source]() [map](shapefiles/cook_park_tax_district/gis_GIS_ParkTaxDist.geojson)
* Police Districts [source](http://gis.chicagopolice.org/) [map](shapefiles/cpd_districts/cpd_districts.geojson)
* Cook County Fire Protection Tax Districts [source]() [map](shapefiles/cook_fire_prot_tax_district/gis_GIS_FireProTaxDist.geojson)
* Census Tracts [source](http://www.census.gov/cgi-bin/geo/shapefiles2010/main) [map](shapefiles/census_tracts/tl_2010_17_tract10.geojson)
* Conservation Areas [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/conservation_areas/Conservation_Areas.geojson)
* Counties [source](http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17) [map](shapefiles/counties/tl_2009_17_county.geojson)
* State House of Representatives Districts [source](http://www.ilhousedems.com/redistricting/?page_id=554) [map](shapefiles/ilga_2011_redistricted/PA 97-6 House Districts.geojson)
* Cook County Board of Review Districts [source](http://www.ilhousedems.com/redistricting/?page_id=554) [map](shapefiles/cook_board_of_review/cook_bor.geojson)
* Voter Precincts [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/voter_precincts/Precincts.geojson)
* Forest Preserves [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/forest_preserves/Forestry.geojson)
* Zip Code Areas [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/zip_codes/Zip_Codes.geojson)
* Planning Regions [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/planning_regions/Planning_Regions.geojson)
* Industrial Corridors [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/industrial_corridors/Industrial_Corridors.geojson)
* TIF Districts [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/tif_districts/TIFs.geojson)
* Kendall County Board Districts [source]() [map](shapefiles/kendall_county_board/KendallCoIL_2010CountyBoardDistricts.geojson)
* Judicial Circuits [source](http://www.state.il.us/court/circuitcourt/circuitmap/map1.asp) [map](shapefiles/judicial_circuits/judicial_circuit.geojson)
* Unified School Districts [source](http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17) [map](shapefiles/unified_school_districts/tl_2009_17_unsd.geojson)
* Parks [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/parks/parks.geojson)
* Cook County Municipal Wards [source]() [map](shapefiles/cook_muni_wards/planim_GIS_MuniWards2011.geojson)
* U.S. Congressional Districts [source](http://www.ilhousedems.com/redistricting/?page_id=554) [map](shapefiles/us_congressional_districts/PA 97-14 Congressional Districts.geojson)
* Police Areas [source](http://gis.chicagopolice.org/) [map](shapefiles/cpd_areas/cpd_areas.geojson)
* Cook County Board of Commissioners Districts [source]() [map](shapefiles/cook_commissioner/planim_GIS_Comm2010.geojson)
* Enterprise Zones [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/enterprise_zones/Enterprise_Zones.geojson)
* 2012 Wards [source](http://chicityclerk.com/2012_redistrict.php) [map](shapefiles/wards2012/CouncilPassedWards_11192012.geojson)
* Judicial Districts [source](http://www.state.il.us/court/appellatecourt/DistrictMap.asp) [map](shapefiles/judicial_districts/districts.geojson)
* Cook County Library Tax Districts [source]() [map](shapefiles/cook_library_tax_district/gis_GIS_LibrTaxDist.geojson)
* Enterprise Communities [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/enterprise_communities/Enterprises Communities.geojson)
* Neighborhoods [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/neighborhoods/Neighboorhoods.geojson)
* Wards [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/wards/Wards.geojson)
* State Senate Districts [source](http://www.ilhousedems.com/redistricting/?page_id=554) [map](shapefiles/ilga_2011_redistricted/PA 97-6 Senate Districts.geojson)
* Police Beats [source](http://gis.chicagopolice.org/) [map](shapefiles/cpd_beats/cpd_beats.geojson)
* DuPage County Board Districts [source](http://www.dupageco.org/gis/) [map](shapefiles/dupage_county_board/DuPageCoBoardDist2011.geojson)
* Will County Board Districts [source](http://www.willcogis.org) [map](shapefiles/will_county_board/WillCounty_Board.geojson)
* Lake County Board Districts [source](http://gis2.co.lake.il.us/output/kmz/cboard2012.kml) [map](shapefiles/lake_county_board/lake_county_board.geojson)
* Elementary School Districts [source](http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17) [map](shapefiles/elementary_school_districts/tl_2009_17_elsd.geojson)
* States [source](http://www.census.gov/cgi-bin/geo/shapefiles2010/main) [map](shapefiles/states/tl_2010_us_state10.geojson)
* Planning Districts [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/planning_districts/Planning_Districts.geojson)
* Community Areas [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/community_areas/CommAreas.geojson)
* Empowerment Zones [source](http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html) [map](shapefiles/empowerment_zones/Empowerment_Zones.geojson)
* McHenry County Board Districts [source](http://www.co.mchenry.il.us/departments/gis/Pages/index.aspx) [map](shapefiles/mchenry_county_board/McHenryCounty_Board_Districts.geojson)
* Census Places [source](http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17) [map](shapefiles/census_places/tl_2009_17_place.geojson)
* Cook Judicial Subcircuits [source]() [map](shapefiles/cook_subcircuits/cook_subcircuits.geojson)
