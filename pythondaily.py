from datetime import datetime
with open(datetime.now().strftime("%d-%m=%Y"),"w") as file:
	file.write("We automated this using python and pythonanywhere")