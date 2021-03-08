def file_read_from_head(name, n):
        from itertools import islice
        with open(name) as f:
                for line in islice(f, n):
                        print(line)
file_read_from_head('Test1.txt',2)