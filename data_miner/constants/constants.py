OUTPUT_DATA_FOLDER = "data"
HOURLY = "hourly"
SUB_HOURLY = "sub_hourly"
TRACKER_FOLDER = "tracker"

MODES = {
  HOURLY: {
    "URL": "/history/hourly",
    "TRACKER": f"{TRACKER_FOLDER}/data_tracker_{HOURLY}.json"
  },
  SUB_HOURLY: {
    "URL": "/history/subhourly",
    "TRACKER": f"{TRACKER_FOLDER}/data_tracker_{SUB_HOURLY}.json"
  },
}
