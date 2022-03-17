# Processed rooftop PV files - explainer

AEMO publishes *actual* rooftop PV production data, obtained using one of two different methods :
- Measurements submitted directly from smart meters (MEASUREMENT)
- Estimates calculated using satellite observations of cloud cover (SATELLITE)

The two different datasets have been kept completely separate at the file level.

## The **key processed data files are**:
- rooftop_pv_measurement.csv: Smart meter direct-measurements for both 2021 and 2022, with all original AEMO data columns, all regions, ascending.
- rooftop_pv_satellite.csv: Satellite estimates for both 2021 and 2022, with all original AEMO data columns, all regions, ascending.
- rooftop_pv_measurement_wholestate.csv: Direct measurements for only whole-state regions (ie: no sub-state regions) for both 2021/2022, all AEMO columns, ascending.
- max_daily.csv: Maximum daily direct-measured PV output for only whole-state regions for 2021/22. Columns are INTERVAL_DATETIME, REGIONID, POWER
- 
