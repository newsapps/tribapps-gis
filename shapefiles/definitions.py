"""
Configuration describing the shapefiles to be loaded for django-boundaryservice.
"""
from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal

import utils

SHAPEFILES = {
    'Community Areas': {
        'file': 'community_areas/CommAreas.shp',
        'singular': 'Community Area',
        'kind_first': False,
        'ider': utils.simple_namer(['AREA_NUMBE']),
        'namer': utils.simple_namer(['COMMUNITY'], normalizer=lambda s: s.title()),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Neighborhoods': {
        'file': 'neighborhoods/Neighboorhoods.shp',
        'singular': 'Neighborhood',
        'kind_first': False,
        'ider': utils.simple_namer(['PRI_NEIGH_']),
        'namer': utils.simple_namer(['PRI_NEIGH']),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Voter Precincts': {
        'file': 'voter_precincts/Precincts.shp',
        'singular': 'Voter Precinct',
        'kind_first': True,
        'ider': utils.simple_namer(['WARD_PRECI']),
        'namer': utils.simple_namer(['WARD_PRECI'], normalizer=lambda s: '#%s' % s),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 13),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    '2010 Police Beats': {
        'file': 'cpd_beats_2010/cpd_beats.shp',
        'singular': 'Police Beat (2010)',
        'kind_first': True,
        'ider': utils.simple_namer(['BEAT_NUM']),
        'namer': utils.simple_namer(['BEAT_NUM'], normalizer=lambda s: '#%s' % s),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 13),
        'href': 'http://gis.chicagopolice.org/',
        'notes': '',
        'encoding': ''
    },
    '2010 Police Areas': {
        'file': 'cpd_areas_2010/cpd_areas.shp',
        'singular': 'Police Area (2010)',
        'kind_first': True,
        'ider': utils.simple_namer(['AREA_NUM']),
        'namer': utils.simple_namer(['AREA_NUM'], normalizer=lambda s: '#%s' % s),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 13),
        'href': 'http://gis.chicagopolice.org/',
        'notes': 'Removed polygons with AREA_NUM set to NULL as they were outside the city.',
        'encoding': ''
    },
    '2010 Police Districts': {
        'file': 'cpd_districts_2010/cpd_districts.shp',
        'singular': 'Police District (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['DIST_NUM']),
        'namer': utils.simple_namer(['DIST_NUM'], normalizer=lambda s: ordinal(s)),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 13),
        'href': 'http://gis.chicagopolice.org/',
        'notes': '',
        'encoding': ''
    },
    'Police Beats': {
        'file': 'cpd_beats_2012/cpd_beats.shp',
        'singular': 'Police Beat',
        'kind_first': True,
        'ider': utils.simple_namer(['BEAT_NUM']),
        'namer': utils.simple_namer(['BEAT_NUM'], normalizer=lambda s: '#%s' % s),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2012, 12, 21),
        'href': 'http://gis.chicagopolice.org/',
        'notes': '',
        'encoding': ''
    },
    'Police Areas': {
        'file': 'cpd_areas_2012/cpd_areas.shp',
        'singular': 'Police Area',
        'kind_first': True,
        'ider': utils.simple_namer(['AREA_NUM']),
        'namer': utils.simple_namer(['AREA_NUM'], normalizer=lambda s: '#%s' % s),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2012, 3, 2),
        'href': 'http://gis.chicagopolice.org/',
        'notes': '',
        'encoding': ''
    },
    'Police Districts': {
        'file': 'cpd_districts_2012/cpd_districts.shp',
        'singular': 'Police District',
        'kind_first': False,
        'ider': utils.simple_namer(['DIST_NUM']),
        'namer': utils.simple_namer(['DIST_NUM'], normalizer=lambda s: ordinal(s)),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2012, 12, 21),
        'href': 'http://gis.chicagopolice.org/',
        'notes': '',
        'encoding': ''
    },
    'Police Sectors': {
        'file': 'cpd_sectors_2012/cpd_sectors.shp',
        'singular': 'Police Sector',
        'kind_first': False,
        'ider': utils.simple_namer(['SECTOR']),
        'namer': utils.simple_namer(['SECTOR'], normalizer=lambda s: ordinal(s)),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2012, 12, 21),
        'href': 'http://gis.chicagopolice.org/',
        'notes': '',
        'encoding': ''
    },
    'Census Tracts': {
        'file': 'census_tracts/tl_2010_17_tract10.shp',
        'singular': 'Census Tract',
        'kind_first': True,
        'ider': utils.simple_namer(['GEOID10']),
        'namer': utils.simple_namer(['NAME10']),
        'authority': 'U.S. Census Bureau',
        'domain': 'Illinois',
        'last_updated': date(2011, 1, 8),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': 'Shapes used for 2010 census.',
        'encoding': ''
    },
    'Wards': {
        'file': 'wards/Wards.shp',
        'singular': 'Ward',
        'kind_first': False,
        'ider': utils.simple_namer(['WARD']),
        'namer': utils.simple_namer(['WARD'], normalizer=lambda s: ordinal(s)),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 15),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': 'Metadata is far out of date, but shapes should be correct until next redistricting.',
        'encoding': ''
    },
    '2012 Wards': {
        'file': 'wards2012/CouncilPassedWards_11192012.shp',
        'singular': 'Ward (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['District_N']),
        'namer': utils.simple_namer(['District_N'], normalizer=lambda s: ordinal(s)),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2012, 1, 20),
        'href': 'http://chicityclerk.com/2012_redistrict.php',
        'notes': 'Passed by City Council, Jan. 19, 2012',
        'encoding': ''
    },
    'Zip Code Areas': {
        'file': 'zip_codes/Zip_Codes.shp',
        'singular': 'Zip Code Area',
        'kind_first': False,
        'ider': utils.simple_namer(['ZIP']),
        'namer': utils.simple_namer(['ZIP']),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 15),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': 'Five-digit zip codes only. (No Zip+4)',
        'encoding': ''
    },
    'State House of Representatives Districts': {
        'file': 'ilga_2011_redistricted/PA 97-6 House Districts.shp',
        'singular': 'State House of Representatives District',
        'kind_first': True,
        'ider': utils.simple_namer(['District_N']),
        'namer': utils.simple_namer(['District_N']),
        'authority': 'Illinois Speaker of the House',
        'domain': 'Illinois',
        'last_updated': date(2012, 10, 01),
        'href': 'http://www.ilhousedems.com/redistricting/?page_id=554',
        'notes': '',
        'encoding': ''
    },
    'State Senate Districts': {
        'file': 'ilga_2011_redistricted/PA 97-6 Senate Districts.shp',
        'singular': 'State Senate District',
        'kind_first': True,
        'ider': utils.simple_namer(['District_N']),
        'namer': utils.simple_namer(['District_N']),
        'authority': 'Illinois Speaker of the House',
        'domain': 'Illinois',
        'last_updated': date(2012, 10, 01),
        'href': 'http://www.ilhousedems.com/redistricting/?page_id=554',
        'notes': '',
        'encoding': ''
    },
    'TIF Districts': {
        'file': 'tif_districts/TIFs.shp',
        'singular': 'TIF District',
        'kind_first': False,
        'ider': utils.simple_namer(['REF'], normalizer=lambda s: s.replace(' ', '')),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 15),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Counties': {
        'file': 'counties/tl_2009_17_county.shp',
        'singular': 'County',
        'kind_first': False,
        'ider': utils.simple_namer(['COUNTYFP']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census Bureau',
        'domain': 'Illinois',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17',
        'notes': '',
        'encoding': ''
    },
    'Conservation Areas': {
        'file': 'conservation_areas/Conservation_Areas.shp',
        'singular': 'Conservation Area',
        'kind_first': False,
        'ider': utils.simple_namer(['REF__'], normalizer=lambda s: s[-1]),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Empowerment Zones': {
        'file': 'empowerment_zones/Empowerment_Zones.shp',
        'singular': 'Empowerment Zone',
        'kind_first': False,
        'ider': utils.index_namer(''),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': 'Multi-polygons stored as single polygons in the original shapefile have been merged.',
        'encoding': ''
    },
    'Enterprise Communities': {
        'file': 'enterprise_communities/Enterprises Communities.shp',
        'singular': 'Enterprise Community',
        'kind_first': False,
        'ider': utils.index_namer(''),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': 'Multi-polygons stored as single polygons in the original shapefile have been merged.',
        'encoding': ''
    },
    'Enterprise Zones': {
        'file': 'enterprise_zones/Enterprise_Zones.shp',
        'singular': 'Enterprise Zone',
        'kind_first': True,
        'ider':utils.simple_namer(['NAME']),
        'namer': utils.simple_namer(['NAME'], normalizer=lambda s: '#%s' % s),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Industrial Corridors': {
        'file': 'industrial_corridors/Industrial_Corridors.shp',
        'singular': 'Industrial Corridor',
        'kind_first': False,
        'ider':utils.simple_namer(['NO']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Planning Districts': {
        'file': 'planning_districts/Planning_Districts.shp',
        'singular': 'Planning District',
        'kind_first': False,
        'ider':utils.simple_namer(['NUM']),
        'namer': utils.simple_namer(['NAME'], normalizer=lambda s: '%sern' % s if s != 'Central' else s),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Planning Regions': {
        'file': 'planning_regions/Planning_Regions.shp',
        'singular': 'Planning Region',
        'kind_first': False,
        'ider':utils.simple_namer(['NUM']),
        'namer': utils.simple_namer(['NAME'], normalizer=lambda s: '%sern' % s if s != 'Central' else s),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Census Places': {
        'file': 'census_places/tl_2009_17_place.shp',
        'singular': 'Census Place',
        'kind_first': False,
        'ider':utils.simple_namer(['PLACEFP']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census Bureau',
        'domain': 'Illinois',
        'last_updated': date(2010, 12, 27),
        'href': 'http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17',
        'notes': '',
        'encoding': ''
    },
    'U.S. Congressional Districts': {
        'file': 'us_congressional_districts/PA 97-14 Congressional Districts.shp',
        'singular': 'U.S. Congressional District',
        'kind_first': False,
        'ider':utils.simple_namer(['District_N']),
        'namer': utils.simple_namer(['District_N'], normalizer=lambda s: ordinal(s)),
        'authority': 'Illinois Speaker of the House',
        'domain': 'Illinois',
        'last_updated': date(2012, 9, 28),
        'href': 'http://www.ilhousedems.com/redistricting/?page_id=554',
        'notes': '',
        'encoding': ''
    },
    'Elementary School Districts': {
        'file': 'elementary_school_districts/tl_2009_17_elsd.shp',
        'singular': 'Elementary School District',
        'kind_first': False,
        'ider':utils.simple_namer(['ELSDLEA']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census Bureau',
        'domain': 'Illinois',
        'last_updated': date(2010, 12, 28),
        'href': 'http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17',
        'notes': '',
        'encoding': ''
    },
    'Secondary School Districts': {
        'file': 'secondary_school_districts/tl_2009_17_scsd.shp',
        'singular': 'Secondary School District',
        'kind_first': False,
        'ider':utils.simple_namer(['SCSDLEA']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census Bureau',
        'domain': 'Illinois',
        'last_updated': date(2010, 12, 28),
        'href': 'http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17',
        'notes': '',
        'encoding': ''
    },
    'Unified School Districts': {
        'file': 'unified_school_districts/tl_2009_17_unsd.shp',
        'singular': 'Unified School District',
        'kind_first': False,
        'ider':utils.simple_namer(['UNSDLEA']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'U.S. Census Bureau',
        'domain': 'Illinois',
        'last_updated': date(2010, 12, 28),
        'href': 'http://www2.census.gov/cgi-bin/shapefiles2009/state-files?state=17',
        'notes': '',
        'encoding': ''
    },
    'Parks': {
        'file': 'parks/parks.shp',
        'singular': 'Park',
        'kind_first': False,
        'ider':utils.simple_namer(['PARK_NO']),
        'namer': utils.simple_namer(['PARK'], normalizer=lambda s: s.title()),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2011, 1, 8),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Judicial Districts': {
        'file': 'judicial_districts/districts.shp',
        'singular': 'Judicial District',
        'kind_first': False,
        'ider':utils.simple_namer(['id']),
        'namer': utils.simple_namer(['name']),
        'authority': 'State of Illinois',
        'domain': 'Illinois',
        'last_updated': date(2012, 10, 1),
        'href': 'http://www.state.il.us/court/appellatecourt/DistrictMap.asp',
        'notes': 'Created by Chicago Tribune by combining counties as specified at http://www.state.il.us/court/appellatecourt/DistrictMap.asp',
        'encoding': ''
    },
    'Kendall County Board Districts': {
        'file': 'kendall_county_board/KendallCoIL_2010CountyBoardDistricts.shp',
        'singular': 'Kendall County Board District',
        'kind_first': False,
        'ider':utils.simple_namer(['District']),
        'namer': utils.simple_namer(['District'], normalizer=lambda s: ordinal(s)),
        'authority': 'Kendall County',
        'domain': 'Kendall County',
        'last_updated': date(2012, 10, 1),
        'href': '',
        'notes': 'Obtained by Chicago Tribune request from the Kendall County GIS Coordinator.',
        'encoding': ''
    },
    'Will County Board Districts': {
        'file': 'will_county_board/WillCounty_Board.shp',
        'singular': 'Will County Board District',
        'kind_first': False,
        'ider':utils.simple_namer(['CTY_BRD_NU']),
        'namer': utils.simple_namer(['CTY_BRD_NU'], normalizer=lambda s: ordinal(s)),
        'authority': 'Will County',
        'domain': 'Will County',
        'last_updated': date(2012, 10, 1),
        'href': 'http://www.willcogis.org',
        'notes': 'Obtained by Chicago Tribune request from the Will County GIS Department.',
        'encoding': ''
    },
    'McHenry County Board Districts': {
        'file': 'mchenry_county_board/McHenryCounty_Board_Districts.shp',
        'singular': 'McHenry County Board District',
        'kind_first': False,
        'ider':utils.simple_namer(['Id']),
        'namer': utils.simple_namer(['District']),
        'authority': 'McHenry County',
        'domain': 'McHenry County',
        'last_updated': date(2012, 10, 1),
        'href': 'http://www.co.mchenry.il.us/departments/gis/Pages/index.aspx',
        'notes': 'Obtained by Chicago Tribune request from the McHenry County GIS Department.',
        'encoding': ''
    },
    'DuPage County Board Districts': {
        'file': 'dupage_county_board/DuPageCoBoardDist2011.shp',
        'singular': 'DuPage County Board District',
        'kind_first': False,
        'ider':utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT'], normalizer=lambda s: ordinal(s)),
        'authority': 'DuPage County',
        'domain': 'DuPage County',
        'last_updated': date(2012, 10, 1),
        'href': 'http://www.dupageco.org/gis/',
        'notes': 'Obtained by Chicago Tribune request from the DuPage County GIS Department.',
        'encoding': ''
    },
    'Cook County Board of Review Districts': {
        'file': 'cook_board_of_review/cook_bor.shp',
        'singular': 'Cook County Board of Review District',
        'kind_first': False,
        'ider':utils.simple_namer(['District_N']),
        'namer': utils.simple_namer(['District_N'], normalizer=lambda s: ordinal(s)),
        'authority': 'Illinois Speaker of the House',
        'domain': 'Illinois',
        'last_updated': date(2012, 10, 1),
        'href': 'http://www.ilhousedems.com/redistricting/?page_id=554',
        'notes': '',
        'encoding': ''
    },
    'Forest Preserves': {
        'file': 'forest_preserves/Forestry.shp',
        'singular': 'Forest Preserve',
        'kind_first': False,
        'ider':utils.simple_namer(['FOREST_ID']),
        'namer': utils.simple_namer(['NAME'], normalizer=lambda s: s.title()),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2011, 1, 8),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'County Subdivisions': {
        'file': 'county_subdivisions/tl_2010_17_cousub10.shp',
        'singular': 'County Subdivision',
        'kind_first': False,
        'ider':utils.simple_namer(['GEOID10']),
        'namer': utils.simple_namer(['NAMELSAD10']),
        'authority': 'U.S. Census Bureau',
        'domain': 'Illinois',
        'last_updated': date(2012, 10, 4),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': 'Shapes used for 2010 census.',
        'encoding': ''
    },
    'Judicial Circuits': {
        'file': 'judicial_circuits/judicial_circuit.shp',
        'singular': 'Judicial Circuit',
        'kind_first': False,
        'ider': utils.simple_namer(['CIRCUIT']),
        'namer': utils.simple_namer(['CIRCUIT'], normalizer=lambda s: ordinal(s)),
        'authority': 'State of Illinois',
        'domain': 'Illinois',
        'last_updated': date(2012, 10, 11),
        'href': 'http://www.state.il.us/court/circuitcourt/circuitmap/map1.asp',
        'notes': 'Created by Chicago Tribune by combining counties as specified at http://www.state.il.us/court/circuitcourt/circuitmap/map1.asp',
        'encoding': ''
    },
    'States': {
        'file': 'states/tl_2010_us_state10.shp',
        'singular': 'State',
        'kind_first': False,
        'ider': utils.simple_namer(['GEOID10']),
        'namer': utils.simple_namer(['NAME10']),
        'authority': 'U.S. Census Bureau',
        'domain': 'U.S.',
        'last_updated': date(2012, 10, 12),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': 'Shapes used for 2010 census.',
        'encoding': ''
    },
    'Lake County Board Districts': {
        'file': 'lake_county_board/lake_county_board.shp',
        'singular': 'Lake County Board District',
        'kind_first': False,
        'ider': utils.simple_namer(['dist_num']),
        'namer': utils.simple_namer(['dist_num'],normalizer=lambda s: ordinal(s)),
        'authority': 'Lake County',
        'domain': 'Lake County',
        'last_updated': date(2012, 10, 17),
        'href': 'http://gis2.co.lake.il.us/output/kmz/cboard2012.kml',
        'notes': 'Converted to shapefile with ogr2ogr.',
        'encoding': ''
    },
    'Cook County Board of Commissioners Districts': {
        'file': 'cook_commissioner/planim_GIS_Comm2010.shp',
        'singular': 'Cook County Board of Commissioners District',
        'kind_first': False,
        'ider':utils.simple_namer(['District_N']),
        'namer': utils.simple_namer(['District_N'], normalizer=lambda s: ordinal(s)),
        'authority': 'Cook County Board',
        'domain': 'Cook County',
        'last_updated': date(2012, 10, 23),
        'href': '',
        'notes': 'Obtained via FOIA request',
        'encoding': ''
    },
    'Cook Judicial Subcircuits': {
        'file': 'cook_subcircuits/cook_subcircuits.shp',
        'singular': 'Cook Judicial Subcircuit',
        'kind_first': False,
        'ider':utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT'], normalizer=lambda s: "Cook Circuit, %s subcircuit" % ordinal(s)),
        'authority': 'Cook County Board',
        'domain': 'Cook County',
        'last_updated': date(2012, 10, 23),
        'href': '',
        'notes': 'Obtained via FOIA request',
        'encoding': ''
    },
    'Cook County Municipal Wards': {
        'file': 'cook_muni_wards/planim_GIS_MuniWards2011.shp',
        'singular': 'Cook County Municipal Ward',
        'kind_first': False,
        'ider': utils.simple_namer(['OBJECTID']),
        'namer': utils.muni_ward_namer,
        'authority': 'Cook County Board',
        'domain': 'Cook County',
        'last_updated': date(2012, 10, 23),
        'href': '',
        'notes': 'Obtained via FOIA request',
        'encoding': ''
    },
    'Cook County Fire Protection Tax Districts': {
        'file': 'cook_fire_prot_tax_district/gis_GIS_FireProTaxDist.shp',
        'singular': 'Cook County Fire Protection Tax District',
        'kind_first': False,
        'ider': utils.simple_namer(['OBJECTID']),
        'namer': utils.simple_namer(['AGENCY_DES'], normalizer=lambda s: s.title()),
        'authority': 'Cook County Board',
        'domain': 'Cook County',
        'last_updated': date(2012, 10, 23),
        'href': '',
        'notes': 'Obtained via FOIA request',
        'encoding': ''
    },
    'Cook County Library Tax Districts': {
        'file': 'cook_library_tax_district/gis_GIS_LibrTaxDist.shp',
        'singular': 'Cook County Library Tax District',
        'kind_first': False,
        'ider': utils.simple_namer(['OBJECTID']),
        'namer': utils.simple_namer(['MAX_AGENCY'], normalizer=lambda s: s.title()),
        'authority': 'Cook County Board',
        'domain': 'Cook County',
        'last_updated': date(2012, 10, 23),
        'href': '',
        'notes': 'Obtained via FOIA request',
        'encoding': ''
    },
    'Cook County Park Tax Districts': {
        'file': 'cook_park_tax_district/gis_GIS_ParkTaxDist.shp',
        'singular': 'Cook County Park Tax District',
        'kind_first': False,
        'ider': utils.simple_namer(['OBJECTID']),
        'namer': utils.simple_namer(['AGENCY_DES'], normalizer=lambda s: s.title()),
        'authority': 'Cook County Board',
        'domain': 'Cook County',
        'last_updated': date(2012, 10, 23),
        'href': '',
        'notes': 'Obtained via FOIA request',
        'encoding': ''
    },
}
