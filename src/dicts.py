# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
waypoints.append({"lat":50, "lon":100, "name":"The best place"})

# Write a loop that prints out all the field values for all the waypoints
for wp in waypoints:
    # How to check if a property exists
    if 'name' in wp: 
        if 'lat' in wp: 
            if 'lon' in wp: 
                print("name: {2}\nlat: {0}\nlon: {1}\n".format(wp['lat'], wp['lon'],wp['name']))
