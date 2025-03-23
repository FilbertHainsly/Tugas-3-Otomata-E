import json

with open('input.json', 'r') as f:
	system = json.load(f)
	
	all_states = system['states']
	curr_state = system['start_state']
	accept_states = system['accept_states']
	transitions = system['transitions']
	test = system['test_string']
	
	print(f'Path: {curr_state}', end='')

	for c in test:
		curr_state = transitions[curr_state][c]
		print(f' -> {curr_state}', end='')
	
	print(f"\nStatus: {'ACCEPTED' if curr_state in accept_states else 'REJECTED'}")