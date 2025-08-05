import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time, TimeDelta
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
import astropy.units as u
import matplotlib.dates as mdates

# Define your observation location
latitude1 = 19.09300278  # GMRT
longitude1 = 74.05656116
height1 = 650* u.m  # Elevation in meters

latitude2 = 11.38340402  # ORT
longitude2 = 76.66616004
height2 = 2239.99963923* u.m  # Elevation in meters

#latitude2 = 18.5610555  # NCRA
#longitude2 = 73.814917
#height2 = 549* u.m  # Elevation in meters

# Define your source coordinates

#3C147 : 85.8891567, 49.8520093
#PSR B0950+08: 148.70 , 7.92677777


right_ascension = 148.70* u.deg  
declination = 7.92677777* u.deg  

# Define observation parameters
#3C147 : 2024-06-28T05:00:00 - 06:00 to 06:30
#PSR B0950+08: 2024-06-06T11:00:00 - 11:30 to 12:00

observation_start = Time('2024-06-06T11:00:00')  # Start time
observation_end = observation_start + 2 * u.hr  # End time (1 day observation)
observation_interval = TimeDelta(4 * u.min)  # Time interval (every 10 minutes)
observation_times = observation_start + np.arange(0, (observation_end - observation_start).sec, observation_interval.sec) * u.s

# Define the location
location1 = EarthLocation(lat=latitude1*u.deg, lon=longitude1*u.deg, height=height1)
location2 = EarthLocation(lat=latitude2*u.deg, lon=longitude2*u.deg, height=height2)

# Define the source
source = SkyCoord(ra=right_ascension, dec=declination)

# Calculate the AltAz coordinates for each observation time
altaz_frame1 = AltAz(obstime=observation_times, location=location1)
source_altaz1 = source.transform_to(altaz_frame1)

altaz_frame2 = AltAz(obstime=observation_times, location=location2)
source_altaz2 = source.transform_to(altaz_frame2)

## Plot azimuth with time
#plt.figure(figsize=(14, 4))
#plt.subplot(2, 1, 1)
#plt.plot(observation_times.datetime, source_altaz.az, 'b-', label='Azimuth')
#plt.xlabel('Time (UTC)')
#plt.ylabel('Azimuth (degrees)')
#plt.title('Azimuth of 3C147 Over Time')
#plt.grid(True)
#plt.legend()

# Plot elevation with time


#plt.subplot(2, 1, 2)
plt.plot(observation_times.datetime, source_altaz1.alt, label='Elevation at GMRT', color = 'green', linewidth = 2)
plt.plot(observation_times.datetime, source_altaz2.alt, label='Elevation at ORT', color = 'blueviolet', linewidth = 2)

plt.xlabel('Time (UTC)', fontsize=16, fontweight='bold')
plt.ylabel('Elevation (degrees)', fontsize=16, fontweight='bold')
plt.title('Elevation of PSR B0950+08 on 2024-06-06', fontsize=20, fontweight='bold')

# Increase tick size and make them bold
plt.xticks(fontsize=18, fontweight='bold')
plt.yticks(fontsize=18, fontweight='bold')

# Make axis lines bold
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)

# Add vertical lines between 06:00 and 06:30
obs_start = Time('2024-06-06T11:30:00')
obs_end = Time('2024-06-06T12:00:00')
current_time = obs_start
while current_time < obs_end:
    plt.axvline(current_time.datetime, color='red', linestyle='--', linewidth=2)
    current_time += observation_interval

plt.grid(True)
plt.legend(fontsize=14, loc='lower right')

plt.tight_layout()
plt.show()

plot_filename = '3c147.png' 
#plt.savefig(plot_filename)

# Determine when the source is above the horizon (elevation > 0 degrees)
#above_horizon = source_altaz.alt > 0*u.deg
#visible_times = observation_times[above_horizon]

# Print the times when the source is visible
#if len(visible_times) > 0:
#    print(f"The source is visible from {visible_times[0].iso} to {visible_times[-1].iso}")
#else:
#    print("The source is not visible during the observation period.")

