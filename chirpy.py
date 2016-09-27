import sys
import re

""" chirpy welcomes you to the land of regular expressions. (:
	It will happily receive the well-formed and assumed file with
	formatting agreed upon offline.

	chirpy parses the file with a regular expression that works for all given
	cases (yay!), captures/stores the width, height of the thumbnail sizes,
	and counts the number of occurences of each.

	chirpy then displays a report of its findings. <3

	chirpy recommends a python3 venv
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
	tn_db_count = 0

	tn_pattern = re.compile(r'\.(?P<tn_width>\d{2,3})x(?P<tn_height>\d{2,3})_q85_crop_upscale\.\w+')
	tn_db = {}

	for line in input_obj:
		# print(line)
		count_lines += 1
		results = re.search(tn_pattern, line)
		if results is not None:
			tn_width = results.group('tn_width')
			tn_height = results.group('tn_height')
			tn_count += 1
			if (int(tn_width), int(tn_height)) in tn_db:
				tn_db[(int(tn_width), int(tn_height))] = tn_db[(int(tn_width), int(tn_height))] + 1
			else:
				tn_db[(int(tn_width), int(tn_height))] = 1
		# else:
			# print(line)
	# print('number of lines:', count_lines)
	# print('number of thumbnails found:', tn_count)
	# print('number thumbnails recorded:', tn_db_count)
	return tn_db


def print_report(tn_db, order_by):
	tn_db_count = 0

	if order_by == "none":
		for (width, height), count in tn_db.items():
			print('{0}x{1} thumbnail size occurs {2} times'.format(width, height, count))
			tn_db_count += count

	elif order_by == "width" or order_by == "height":
		sort_this_list = list()
		for (width, height), count in tn_db.items():
			sort_this_list.append((width, height))

		if order_by == "width":
			sort_this_list = sorted(sort_this_list)
		elif order_by == "height":
			sort_this_list = sorted(sort_this_list, key=lambda tup: tup[1])
		# print(sort_this_list)

		for (width, height) in sort_this_list:
			print('{0}x{1} thumbnail size occurs {2} times'
				.format(width, height, tn_db[(int(width), int(height))]))
			tn_db_count += tn_db[(int(width), int(height))]

	elif order_by == "count":
		for (width, height), count in sorted(tn_db.items(), key=lambda x: x[1]):
			print('{0}x{1} thumbnail size occurs {2} times'.format(width, height, count))
			tn_db_count += count

	print('number thumbnails recorded:', tn_db_count)


# acquire command line arguments for filename and order_by for sorting results
# error handling for sorting options
sort_values = ["height", "width", "count", "none"]
for value in sort_values:
	if sys.argv[-1] == value:
		order_by = sys.argv[-1]
		break
	if value == sort_values[-1]:
		print("'{0}' is not a valid sort option".format(sys.argv[-1]))
		exit()

# foregoing error-handling for input filename
input_filename = sys.argv[-2]

#  print (text_filename)
print_chirpy()
print("Importing text file: '{0}' ...".format(input_filename))
input_obj = open(input_filename, "r")

tn_db = parse_file(input_obj)
print_report(tn_db, order_by)
