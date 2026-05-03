from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord

# Test units
distance = 4.2 * u.lightyear
print("Distance:", distance)
print("Distance in km:", distance.to(u.km))

#Test time
t = Time("2025-01-01 00:00:00", scale="utc")
print("UTC Time:", t.iso)
print("Julian Date:", t.jd)

#Test coordinates
coord = SkyCoord(ra=83.6331 * u.deg, dec=22.0145 * u.deg, frame="icrs")
print("Object coordinates:")
print("RA:", coord.ra)
print("DEC:", coord.dec)

#Convert to Galactic coordinates
galactic = coord.galactic
print("Galactic Longitude:", galactic.l)
print("Galactic Latitude:", galactic.b)
