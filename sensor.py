# OUT - sensor_out.csv
# cols - Timestamp, Speed

# timestamp - float [us], start 100s -> 100 000 000us, increment 200ms ->200 000 us +- 10ms -> 10 000us, 6 decimal places
#           - (> 160) s -> 160 000 000 us - stop generating
# speed - float [kmph], start 60 kmph, increment 0.56 kmph every row (<= every new timestamp), when 120 kmph, keep 120 +- 0.1kmph
