import json  # Mengimpor library JSON untuk membaca file JSON

# Membuka dan membaca file JSON yang berisi definisi DFA
with open('input.json', 'r') as f:
	system = json.load(f)  # Mengubah isi file JSON menjadi dictionary (kamus) di Python

	# Mengambil informasi DFA dari file JSON
	all_states = system['states'] # Daftar semua state
	curr_state = system['start_state'] # State awal
	accept_states = system['accept_states'] # Daftar state yang menerima (accepting states)
	transitions = system['transitions'] # Transisi antar state berdasarkan input
	test = system['test_string'] # String yang akan diuji

	# Mencetak state awal dalam jalur DFA
	print(f'Path: {curr_state}', end='')

	# Melakukan iterasi setiap karakter dalam test_string
	for c in test:
		curr_state = transitions[curr_state][c] # Pindah ke state berikutnya berdasarkan transisi DFA
		print(f' -> {curr_state}', end='') # Mencetak jalur state yang dilewati
	
	print(f"\nStatus: {'ACCEPTED' if curr_state in accept_states else 'REJECTED'}") # Jika state akhir ada di accept_states akan diterima, jika tidak maka akan ditolak

