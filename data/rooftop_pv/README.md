# Processed rooftop PV files - explainer

AEMO publishes *actual* rooftop PV production data, obtained using one of two different methods :
- Measurements submitted directly from smart meters (MEASUREMENT)
- Estimates calculated using satellite observations of cloud cover (SATELLITE)

The two different datasets have been kept completely separate at the file level.

## The **key processed PV data files are**:
- rooftop_pv_measurement_full_set.csv: Direct measurements only ('MEASUREMENT') for March 2018 to March 2022 in 30 min intervals, all AEMO columns, for all state and sub-state regions. 708710 records, ascending by date.
- rooftop_pv_measurement_wholestate.csv: Direct measurements for only whole-state regions (ie: no sub-state regions) March 2018 to March 2022 in 30 min intervals, all AEMO columns, 354355 records, ascending by date.
- max_daily.csv: Maximum daily direct-measured PV output for only whole-state regions for March 2018 to March 2022. Columns are INTERVAL_DATETIME, REGIONID, POWER. Ascending by date.

## TODO: NEEDS TO BE RE-PROCESSED USING THE UPDATED 2018-2022 DATASETS DESCRIBED ABOVE
## The key **combined PV data file is**:
- pv_demand_forecast_combined.csv: Merged state-level MEASUREMENT type PV data from the 'rooftop_pv_measurement_wholestate.csv' file with Rahul's previously combined 'combined_fd_Avg.csv' file. This now yields one file with full rooftop PV output, actual demand, forecast demand, temperature, and various other engineered features per 30 minute interval. **NB: because there is only rooftop PV data for 2021-2022 and this file is the result of a left-join on the PV data, only rows for which PV data was observed are here**
