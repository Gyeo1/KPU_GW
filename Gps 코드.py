import serial, time, pynmea2, sys

port = '/dev/ttyS0' #맞는 포트 번호 입력.
baud = 9600
count = 0
sum_lat = 0
sum_lon = 0
avg_lat = 0
avg_lon = 0

serialPort = serial.Serial(port, baudrate=baud, timeout=0.5)

while True:
    str = serialPort.readline().decode().strip()

    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print("  Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s -- Satellites: %s" % (
        msg.timestamp, msg.latitude, msg.lat_dir, msg.longitude, msg.lon_dir, msg.altitude, msg.altitude_units,
        msg.num_sats))
        sum_lat += float(msg.latitude)
        sum_lon += float(msg.longitude)
        print(" sum_lat: %f -- sum_lon: %f" % (sum_lat, sum_lon))
        count += 1
    time.sleep(0.1)

    if count > 9:
        avg_lat = sum_lat / 10
        avg_lon = sum_lon / 10
        print("avg_lat : %s -- avg_lon : %s" % (avg_lat, avg_lon))

        # tip dormitory gps cordination
        if avg_lat > 37.3417 and avg_lat < 37.3419 and avg_lon > 126.7327 and avg_lon < 126.7329:
            print("Start point set complete! point: TIP")
            sys.exit()

        # demo point A
        elif avg_lat > 37.3417 and avg_lat < 37.3419 and avg_lon > 126.7327 and avg_lon < 126.7329:
            print("Start point set complete! point: TIP")
            sys.exit()

        # demo point B
        elif avg_lat > 37.3417 and avg_lat < 37.3419 and avg_lon > 126.7327 and avg_lon < 126.7329:
            print("Start point set complete! point: TIP")
            sys.exit()

        # demo point C
        elif avg_lat > 37.3417 and avg_lat < 37.3419 and avg_lon > 126.7327 and avg_lon < 126.7329:
            print("Start point set complete! point: TIP")
            sys.exit()