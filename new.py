sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
min_value = True
for key,val in sample_dict.items():
    if val<min_value:
        val = min_value
