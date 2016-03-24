# easylidar - Lidar data to dataframe, made simple. 
# What is it?
Easylidar is a tool I made to speed up dealing with lidar data, and metadata files. All I really wanted was the point data transformed to 4326 projection while I wanted the elevation data to stay in meters and also to bring in the color intensity into one dataframe. So essentially this script assumes you have a a lidar file (las) and a lidar metadata file (xml) in your current directory. (or a explicitly stated folder) Simply call one function it traverses the current directory for an xml file from that metadata file parses and searches for the projections ESPG and sends that into a function to transform it into ESPG 4326 and return it all as dataframe. 

**NOTE: Currently Assumes you have only 1 xml file and 1 las file in your current directory if not the case use the folder = folder location kwarg and put the two files in the folder sent in as an argument.**

# Example Output
This example assumes you have the to files in the examples folder.
```python
import easylidar as el

data = el.get_lidar()
print data

'''
              LAT       LONG  ELEVATION  INTENSITY
0      -81.566921  38.391032     966.02        135
1      -81.566927  38.391032     965.92        165
2      -81.566921  38.391042     965.68        118
3      -81.566920  38.391071     964.08         18
4      -81.566926  38.391061     964.38         25
5      -81.566920  38.391071    1015.32         13
6      -81.566922  38.391066    1004.21         11
7      -81.566925  38.391061     990.51         57
8      -81.566931  38.391051     965.10          0
9      -81.566937  38.391041     965.42        121
10     -81.566943  38.391031     965.40        144
11     -81.566943  38.391041     965.32        157
12     -81.566926  38.391071    1015.27         15
13     -81.566929  38.391065    1000.83         14
14     -81.566931  38.391062     991.92         22
15     -81.566937  38.391051     964.79          0
16     -81.566923  38.391075    1000.30         11
17     -81.566932  38.391061     964.51          0
18     -81.566920  38.391081     989.83         13
19     -81.566926  38.391071     965.01         98
20     -81.566920  38.391082     965.38          0
21     -81.566921  38.391106     977.60         37
22     -81.566924  38.391101     965.32        158
23     -81.566920  38.391107    1006.60         23
24     -81.566926  38.391097     980.01         15
25     -81.566930  38.391091     965.13        123
26     -81.566924  38.391101    1015.18         24
27     -81.566936  38.391081     964.94        109
28     -81.566931  38.391089    1012.33         21
29     -81.566936  38.391080     989.80         12
...           ...        ...        ...        ...
749456 -81.555496  38.386386     878.70         16
749457 -81.555500  38.386375     784.63        129
749458 -81.555490  38.386390     811.18         14
749459 -81.555491  38.386388     793.32         29
749460 -81.555492  38.386387     782.05        137
749461 -81.555483  38.386400     782.82        178
749462 -81.555497  38.386396     780.41        181
749463 -81.555506  38.386384     782.17        157
749464 -81.555510  38.386383     878.80         18
749465 -81.555514  38.386372     783.36        121
749466 -81.555523  38.386359     785.71         75
749467 -81.555526  38.386358     875.33         34
749468 -81.555531  38.386347     788.48         89
749469 -81.555534  38.386346     881.63         17
749470 -81.555539  38.386335     791.04         74
749471 -81.555537  38.386358     889.24         21
749472 -81.555529  38.386369     881.98         20
749473 -81.555532  38.386363     830.26          6
749474 -81.555534  38.386357     784.95         92
749475 -81.555526  38.386369     782.55        201
749476 -81.555517  38.386382     780.85        221
749477 -81.555509  38.386394     780.16        187
749478 -81.555519  38.386399     779.63        190
749479 -81.555527  38.386386     780.21        232
749480 -81.555533  38.386381     840.04          7
749481 -81.555536  38.386374     781.40        168
749482 -81.555539  38.386374     883.42         18
749483 -81.555539  38.386385     825.74         22
749484 -81.555533  38.386392     778.61        255
749485 -81.555525  38.386404     777.39        218

[749486 rows x 4 columns]
[Finished in 3.3s]
'''
```

# Functionality 
Supports a folder kwarg argument to look only inside of one folder.
