import sys
import re

""" chirpy welcomes you to the land of regular expressions. (:
	It will happily receive the well-formed and assumed file with 
	formatting agreed upon offline. 

"""

def print_chirpy():
	""" original source: http://around140.en.utf8art.com/arc/pig_102.html
		modified for command line fit and fun ;p
	"""
	print("\n\
　　~ﾍ⌒ヽﾌ~\t\tHi there, I'm chirpy.\n\
.  ( ・ω・）\t\tLet's parse a file\n\
　 ﾉ\")   )\t\t    and...\n\
  彡ノ,,ノ\t\tprint a report! Yay!\n\
---―〃-〃――――\n\
　　ﾚ,,/\n\n")

def parse_file(input_obj):
	count_lines = 0
	tn_count = 0

	tn_pattern = re.compile(r'\.(?P<tn_size>\d{2,3}x\d{2,3})_q85_crop_upscale\.\w+')
	
	for line in input_obj:
		# print(line)
		count_lines += 1
		results = re.search(tn_pattern, line)
		if results is not None:
			# print(results.group('tn_size'))
			tn_count += 1
		# else:
			# print(line)
	print('number of lines:', count_lines)
	print('number of thumbnails:', tn_count)

print_chirpy()

input_filename = sys.argv[-1]
#  print (text_filename)
print("Importing text file: '{0}' ...".format(input_filename))
input_obj = open(input_filename, "r")

parse_file(input_obj)


