Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

It should be O(1). All I'm doing is setting a value in an array, and increasing my `self.current` counter by 1.

2. What is the space complexity of your ring buffer's `append` function?

The space complexity should also be O(1). No new variables are being created, it is only accessing already-present variables of the RingBuffer class, as well as the input of the method.

3. What is the runtime complexity of your ring buffer's `get` method?

The runtime complexity should be O(n). I am filtering the list for any `None` values before I return it, which means I have to loop through it. Looping through a list once is O(n) runtime.

4. What is the space complexity of your ring buffer's `get` method?

The space complexity should be O(1). I am creating a single variable, which is equal to the filter object returned from filtering my RingBuffer's storage.

5. What is the runtime complexity of the provided code in `names.py`?

The runtime of the provided code is O(n^2). For every name in `names_1`, it is looping through the entire `names_2` array in order to check for a duplicate using a simple equality check. So you are running a loop of length n, n number of times.

6. What is the space complexity of the provided code in `names.py`?

The space complexity of the provided code should be O(1). There are only 3 variables. A list of all the names in `names_1.txt`, a list of all the names in `names_2.txt`, and a list of all the duplicates.

7. What is the runtime complexity of your optimized code in `names.py`?

The runtime of my optimized code is O(n). I am creating a dictionary, and looping through `names_2` to fill the dictionary with values. I then do a second, separate for loop, which will loop through `names_1`, and check if that name is in `names_2`. If it is, that name gets added to the duplicates list. The 2 for loops are of O(n) runtime. Checking if a name exists in a dictionary is O(1) runtime. O(1 * n * n) = O(2n) = O(n).

8. What is the space complexity of your optimized code in `names.py`?

The space complexity of my optimized code is O(1). I am only allocating memory to 4 variables. The list of names in `names1.txt`, the list of names in `names2.txt`, a dictionary of names in `names_2`, and a list of duplicates.