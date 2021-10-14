import hashlib



# encode to bytes using UTF-8 encoding

password = "hangry".encode()

# hash with SHA-2 (SHA-256 & SHA-512)

print("SHA-256:", hashlib.sha256(password).hexdigest())




V_CREDENTIALS = [
		{'username' : 'adrian',
		'password_hash' : 'ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae'
		},

		{'username': 'boo44', 
		 'password_hash': '894092b3e1c50bd2daf6818d7c0d67a6eb32cd33691d6cbf224cba1dd45e6d30'
		 },

		 {'username' : 'lastfirst34',
		  'password_hash' : '0cdc689ad28440a2488392f60bb4e852e120fde295420fb560f1c5da21c1003c'
		  },
		]
