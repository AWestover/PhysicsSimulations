import psutil
for proc in psutil.process_iter():
	try:
		pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
	except psutil.NoSuchProcess:
		pass
	else:
		print(pinfo)
		if 'python' in pinfo['name']:
			print(pinfo['pid'])
			proc.kill()


