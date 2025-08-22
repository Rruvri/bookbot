def get_book_text(path_to_file): 
	with open(path_to_file) as f:
		file_contents = f.read()
		return file_contents 

from stats import word_count
from stats import character_count
from stats import dict_sort
from stats import search_func
	
def main():
	import sys
	if len(sys.argv)<2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	file_contents = get_book_text(f"{sys.argv[1]}")

	count = word_count(file_contents)
	chr_dict = character_count(file_contents)
	sorted_list = dict_sort(chr_dict)

	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {sys.argv[1]}")
	print ("----------- Word Count ----------")
	print (f"Found {count} total words")
	print ("--------- Character Count -------")

	for chr in sorted_list:
		test_value = chr["char"]
		if test_value.isalpha():
			print (f'{test_value}: {chr["num"]}')
		else:
			pass
	print ("=================================")
	search_func(file_contents)
	


	
main()


