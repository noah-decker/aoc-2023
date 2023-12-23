with open('inputs\day4_input.txt') as f:
    text = f.read()
atext = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''
def get_range(start_range,len_range):
	return [x for x in range(start_range,start_range+len_range)]
def in_range(dest_range,source_range,start):
      if start in source_range:
            return dest_range[source_range.index(start)]
      else:
            return start
      
seeds = [79, 14, 55, 13]
fmap = [[50, 98, 2],
[52, 50, 48]]

minn = float("inf")
for seed in seeds:
      for arange in fmap:
            dest_start,source_start,len_range = arange
            source_range = get_range(source_start,len_range)
            dest_range = get_range(dest_start,len_range)
            
