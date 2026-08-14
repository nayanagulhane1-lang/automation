#Given the string 'Paytm-Transaction: Rs.500 credited on 2024-06-18', 
# extract the transaction amount ('Rs.500') and the date ('2024-06-18')
# using string indexing and slicing.<br><br><em><strong>Hint:</strong> 
# Find the start and end positions of each part before slicing.</em>

my_string='Paytm-Transaction: Rs.500 credited on 2024-06-18'
print(my_string[19:25])
print(my_string[38:48])