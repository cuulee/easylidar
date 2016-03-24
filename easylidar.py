import laspy
import itertools
import pyproj
import pandas as pd
import os

#takes a dataframe and turns it into a list
def df2list(df):
    df = [df.columns.values.tolist()]+df.values.tolist()
    return df


#takes a list and turns it into a datafrae
def list2df(df):
    df = pd.DataFrame(df[1:], columns=df[0])
    return df


# checks to see if a number is in a single character
def check_num(byte):
	numbers = ['0','1','2','3','4','5','6','7','8','9']
	for row in numbers:
		if row == str(byte):
			return True
	return False


# parse through xml meta data to find espg
def parse_find_projection(xmlfile):
	with open(xmlfile,'r') as f:
		f=f.read()
		f=str.split(str(f),'\n')
	
	for row in f:
		if 'MapProjectionDefinition' in str(row):
			finding = str.split(row,">")[1]
			finding = str.split(finding,"<")[0]
			finding = str.split(str.lower(finding),'epsg')[-1]
			startind = 0
			for row in finding:
				if check_num(row)==True:
					if startind == 0:
						startind = 1
						total = str(row)
					else:
						total += str(row)
				elif check_num(row) == False and startind == 1:
					total = int(total)
					return total


# reads and returns a filename given a crs
def read_return(filename,CRS):
	# reading file to memory
	infile = laspy.file.File(filename, mode="r")

	# getting points and color
	lats = infile.x.tolist()
	longs = infile.y.tolist()
	elevations = infile.z.tolist()
	intensity = infile.intensity.tolist()

	# reprojecting point
	lats,longs =project_point(lats,longs,CRS)
	data=[infile.x.tolist(),infile.y.tolist(),infile.z.tolist()]
	newdata=[['LAT','LONG','ELEVATION','INTENSITY']]

	# iterating through each point
	for x,y,z,intens in itertools.izip(lats,longs,elevations,intensity):
		newdata.append([x,y,z,intens])
	
	# converting to dataframe
	newdata = list2df(newdata)

	return newdata


# projects points to the correct cordinate system
def project_point(pointX,pointY,crs):
	# Spatial Reference System
	inputEPSG = crs
	outputEPSG = 4326

	p1 = pyproj.Proj(init='epsg:'+str(inputEPSG), preserve_units=True)
	p2 = pyproj.Proj(init='epsg:'+str(outputEPSG),proj='latlong')

	#pointX,pointY=p1(pointX,pointY)
	x,y = pyproj.transform(p1,p2,pointX,pointY)

	return [x,y]


#returns a list with geojson in the current directory
def get_filetype(src,filetype):
	filetypes=[]
	for dirpath, subdirs, files in os.walk(os.getcwd()+'/'+src):
	    for x in files:
	        if x.endswith('.'+str(filetype)):
	        	if src == '':
	        		filetypes.append(src+x)
	        	else:
	        		filetypes.append(src+'/'+x)
	return filetypes


# traverses the current directory for a las file and xml file 
# reads the xml file to look for ESPG then projects the lidar file and returns a pandas dataframe
def get_lidar(**kwargs):
	folder = False
	for key,value in kwargs.iteritems():
		if key == 'folder':
			folder = value
	if not folder == False:
		# getting filenames
		lasfilename = get_filetype(folder,'las')[0]
		xmlfilename = get_filetype(folder,'xml')[0]
	else:
		# getting filenames
		lasfilename = get_filetype('','las')[0]
		xmlfilename = get_filetype('','xml')[0]

	# getting coordinate espg
	espg = parse_find_projection(xmlfilename)

	# getting lidar data
	data = read_return(lasfilename,espg)

	return data



