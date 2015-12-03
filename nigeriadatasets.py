# Lists
all_states = ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara", "FCT-Abuja"]
sharia_states = ['Bauchi', 'Borno', 'Gombe', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Niger', 'Sokoto', 'Yobe', 'Zamfara']
non_sharia_states = ['Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bayelsa', 'Benue', 'Cross River', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Imo', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Taraba', 'FCT-Abuja']
ne = ['Adamawa', 'Bauchi', 'Borno', 'Gombe', 'Taraba', 'Yobe']
nw = ['Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Sokoto', 'Zamfara']
nc = ['Benue', 'Kogi', 'Kwara', 'Nasarawa', 'Niger', 'Plateau', 'FCT-Abuja']
se = ['Abia', 'Anambra', 'Ebonyi', 'Enugu', 'Imo']
ss = ['Akwa Ibom', 'Bayelsa', 'Cross River', 'Delta', 'Edo', 'Rivers']
sw = ['Ekiti', 'Lagos', 'Ogun', 'Ondo', 'Osun', 'Oyo']

# Dictionaries
allStates = {1: 'Abia', 2: 'Adamawa', 3: 'Akwa Ibom', 4: 'Anambra', 5: 'Bauchi', 6: 'Bayelsa', 7: 'Benue', 8: 'Borno', 9: 'Cross River', 10: 'Delta', 11: 'Ebonyi', 12: 'Edo', 13: 'Ekiti', 14: 'Enugu', 15: 'Gombe', 16: 'Imo', 17: 'Jigawa', 18: 'Kaduna', 19: 'Kano', 20: 'Katsina', 21: 'Kebbi', 22: 'Kogi', 23: 'Kwara', 24: 'Lagos', 25: 'Nasarawa', 26: 'Niger', 27: 'Ogun', 28: 'Ondo', 29: 'Osun', 30: 'Oyo', 31: 'Plateau', 32: 'Rivers', 33: 'Sokoto', 34: 'Taraba', 35: 'Yobe', 36: 'Zamfara', 37: 'FCT-Abuja'}
shariaStates = {33: 'Sokoto', 35: 'Yobe', 36: 'Zamfara', 5: 'Bauchi', 8: 'Borno', 15: 'Gombe', 17: 'Jigawa', 18: 'Kaduna', 19: 'Kano', 20: 'Katsina', 21: 'Kebbi', 26: 'Niger'}
nonSharia    = {1: 'Abia', 2: 'Adamawa', 3: 'Akwa Ibom', 4: 'Anambra', 6: 'Bayelsa', 7: 'Benue', 9: 'Cross River', 10: 'Delta', 11: 'Ebonyi', 12: 'Edo', 13: 'Ekiti', 14: 'Enugu', 16: 'Imo', 22: 'Kogi', 23: 'Kwara', 24: 'Lagos', 25: 'Nasarawa', 27: 'Ogun', 28: 'Ondo', 29: 'Osun', 30: 'Oyo', 31: 'Plateau', 32: 'Rivers', 34: 'Taraba', 37: 'FCT-Abuja'}

north_east    = {2: 'Adamawa', 35: 'Yobe', 5: 'Bauchi', 8: 'Borno', 34: 'Taraba', 15: 'Gombe'}
north_west    = {33: 'Sokoto', 36: 'Zamfara', 17: 'Jigawa', 18: 'Kaduna', 19: 'Kano', 20: 'Katsina', 21: 'Kebbi'}
north_central = {37: 'FCT-Abuja', 7: 'Benue', 22: 'Kogi', 23: 'Kwara', 25: 'Nasarawa', 26: 'Niger', 31: 'Plateau'}
south_east    = {16: 'Imo', 1: 'Abia', 11: 'Ebonyi', 4: 'Anambra', 14: 'Enugu'}
south_south   = {32: 'Rivers', 3: 'Akwa Ibom', 6: 'Bayelsa', 9: 'Cross River', 10: 'Delta', 12: 'Edo'}
south_west    = {13: 'Ekiti', 24: 'Lagos', 27: 'Ogun', 28: 'Ondo', 29: 'Osun', 30: 'Oyo'}


def make_dics(keys,values):
	dictionary = dict(zip(keys, values))
	print dictionary

